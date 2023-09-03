import json
import pathlib
import logging
from errno import errorcode

# import pymysql
import mysql.connector
from flask import jsonify, current_app
from sqlalchemy import create_engine, text

from src import config
from src.classes.Pet import PetDecoder

logger = logging.getLogger("pets_db_service_logger")

DB_FILEPATH = pathlib.Path(__file__).parent.parent / "temp_dbs"

pet_ids = []


def connect_to_db():
    engine = create_engine(
        "mysql+pymysql://" + config.mysql_user + ":" + config.mysql_pw + "@" + config.mysql_host)
    cursor = engine.connect()
    cursor.execute(text("USE %s" % config.mysql_db))
    return cursor


#db_cursor = get_db_connection(db_config=current_app.get("db_config"))


def get_pet(pet_id: str):

    if pet_id not in get_id_list():
        raise FileNotFoundError(f"id: {pet_id} Not found")

    with open(f"{DB_FILEPATH}/{pet_id}.json", "r") as f:
        return json.loads(f.read(), cls=PetDecoder)


def create_pet(pet):

    db_cursor = connect_to_db()

    try:
        insert_query = text(
            "INSERT INTO pets_table (name, dob, gender, creation_timestamp, age, total_clicks) "
            "VALUES (:name, :dob, :gender, :creation_timestamp, :age, :total_clicks)"
        )
        pet_data = {
            "name": pet.name,
            "dob": pet.dob.strftime('%Y-%m-%d'),  # Convert to MySQL DATE format
            "gender": pet.gender,
            "creation_timestamp": pet.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # Convert to MySQL TIMESTAMP format
            "age": pet.age,
            "total_clicks": pet.total_clicks
        }
        db_cursor.execute(insert_query, pet_data)
        db_cursor.commit()
        logger.info("Pet added to the database successfully!")
    except Exception as e:
        logger.error(f"Error inserting pet into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()

# def create_pet(pet: Pet):
#     with open(f"{DB_FILEPATH}/{pet.pet_id}.json", "w+") as f:
#         f.write(json.dumps(pet, cls=PetEncoder))
#
#     add_id_to_id_list(get_id_list(), pet.pet_id)
#     return pet


def add_id_to_id_list(id_list: list, pet_id: str):
    id_list.append(pet_id)

    with open(f"{DB_FILEPATH}/id_list.json", "w") as f:
        f.write(json.dumps(id_list))


def get_id_list():
    with open(f"{DB_FILEPATH}/id_list.json", "r") as f:
        return json.loads(f.read())


def get_all_pets():
    pets = []

    for pet_id in get_id_list():
        with open(f"{DB_FILEPATH}/{pet_id}.json", "r") as f:
            pet = json.loads(f.read(), cls=PetDecoder)
            pets.append(pet)

    return pets


def update_pet(pet_id, pet_obj):
    # TODO implement when db set up
    return pet_obj


def delete_pet(pet_id):
    # TODO implement when db set up

    return pet_id