import json
import pathlib
import uuid
from typing import List

import pymysql
from flask import jsonify, current_app

from src.classes.Pet import Pet, PetEncoder, PetDecoder

DB_FILEPATH = pathlib.Path(__file__).parent.parent / "temp_dbs"

pet_ids = []


def get_db_connection(db_config):
    connection = pymysql.connect(**db_config)
    return connection


def get_pet(pet_id : str):
    get_db_connection(current_app.config.get("db_config"))

    if pet_id not in get_id_list():
        raise FileNotFoundError(f"id: {pet_id} Not found")

    with open(f"{DB_FILEPATH}/{pet_id}.json", "r") as f:
        return json.loads(f.read(), cls=PetDecoder)


def create_pet(pet : Pet):
    with open(f"{DB_FILEPATH}/{pet.uuid}.json", "w+") as f:
        f.write(json.dumps(pet, cls=PetEncoder))

    add_id_to_id_list(get_id_list(), pet.uuid)


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
