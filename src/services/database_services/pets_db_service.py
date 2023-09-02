import json
import pathlib
import logging

import pymysql
from flask import jsonify, current_app

from src.classes.Pet import Pet, PetEncoder, PetDecoder

logger = logging.getLogger("pets_db_service_logger")

DB_FILEPATH = pathlib.Path(__file__).parent.parent / "temp_dbs"

pet_ids = []


def get_db_connection(db_config):
    connection = pymysql.connect(**db_config)
    return connection


db_client = get_db_connection(db_config=current_app.get("db_config"))


def get_pet(pet_id: str):

    if pet_id not in get_id_list():
        raise FileNotFoundError(f"id: {pet_id} Not found")

    with open(f"{DB_FILEPATH}/{pet_id}.json", "r") as f:
        return json.loads(f.read(), cls=PetDecoder)


def create_pet(pet: Pet):
    with open(f"{DB_FILEPATH}/{pet.pet_id}.json", "w+") as f:
        f.write(json.dumps(pet, cls=PetEncoder))

    add_id_to_id_list(get_id_list(), pet.pet_id)
    return pet


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