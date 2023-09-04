import pathlib
import logging
import sqlalchemy

from src import config
from src.classes.Pet import Pet

logger = logging.getLogger("pets_db_service_logger")


def connect_to_db():
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://" + config.mysql_user + ":" + config.mysql_pw + "@" + config.mysql_host)
    cursor = engine.connect()
    cursor.execute(sqlalchemy.text("USE %s" % config.mysql_db))
    return cursor


def get_pet(pet_id: str):
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text(f"SELECT * FROM pets_table WHERE pet_id = '{pet_id}'")
        result = db_cursor.execute(sql).fetchone()
        if result:
            pet = Pet(
                pet_id=result[0],
                name=result[1],
                dob=result[2].strftime('%m/%d/%Y'),
                gender=result[3],
                creation_timestamp=result[4].strftime('%m/%d/%Y %H:%M:%S'),
                user_id=result[5]
            )
            logger.debug(f"Pets DB Service: pet named {pet.name} found with id: {pet_id}")
            return pet
        else:
            logger.info(f"Pets DB Service: no pet found with id: {pet_id}")
            return None
    except Exception as e:
        logger.error(f"Error getting pet with pet id: {pet_id} from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def get_all_pets(user_id: str):
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text(f"SELECT * FROM pets_table WHERE user_id = '{user_id}'")
        results = db_cursor.execute(sql).fetchall()
        pets_list = []
        for result in results:
            pet = Pet(
                pet_id=result[0],
                name=result[1],
                dob=result[2].strftime('%m/%d/%Y'),
                gender=result[3],
                creation_timestamp=result[4].strftime('%m/%d/%Y %H:%M:%S'),
                user_id=result[5]
            )
            pets_list.append(pet)
        return pets_list
    except Exception as e:
        logger.error(f"Error getting pets from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def create_pet(pet):

    db_cursor = connect_to_db()

    try:
        insert_query = sqlalchemy.text(
            "INSERT INTO pets_table (pet_id, name, dob, gender, creation_timestamp, user_id, age) "
            "VALUES (:pet_id, :name, :dob, :gender, :creation_timestamp, :user_id, :age)"
        )
        pet_data = {
            "pet_id": pet.pet_id,
            "name": pet.name,
            "dob": pet.dob.strftime('%Y-%m-%d'),  # Convert to MySQL DATE format
            "gender": pet.gender,
            "creation_timestamp": pet.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # Convert to MySQL TIMESTAMP format
            "age": pet.age,
            "user_id": pet.user_id
        }
        db_cursor.execute(insert_query, pet_data)
        db_cursor.commit()
        logger.info("Pet added to the database successfully!")
        return pet
    except Exception as e:
        logger.error(f"Error inserting pet into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def update_pet(pet_id, pet_obj):
    db_cursor = connect_to_db()

    try:
        # If the pet exists, update its information
        update_sql = sqlalchemy.text(f"""
                UPDATE pets_table
                SET name = '{pet_obj.name}', dob = '{pet_obj.dob.strftime('%Y-%m-%d')}', gender = '{pet_obj.gender}'
                WHERE pet_id = '{pet_id}'
            """)
        db_cursor.execute(update_sql)
        db_cursor.commit()

        return pet_obj
    except Exception as e:
        logger.error(f"Error upserting pet into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def delete_pet(pet_id):

    db_cursor = connect_to_db()

    try:
        # Check if the pet with the given pet_id exists
        existing_pet = get_pet(pet_id=pet_id)

        if not existing_pet:
            logger.error(f"Pets DB Service: No pet found with id: {pet_id}")
            return None

        logger.info(f"Pets DB Service: Deleting pet with pet_id {pet_id} from database")

        deletion_ops = {
            'delete_pets_sql': sqlalchemy.text(f"DELETE FROM pets_table WHERE pet_id = '{pet_id}'"),
            'delete_tricks_sql': sqlalchemy.text(f"DELETE FROM tricks_table WHERE user_id = '{pet_id}'"),
            'delete_clicks_sql': sqlalchemy.text(f"DELETE FROM clicks_table WHERE user_id = '{pet_id}'")
        }

        for sql_stmt in deletion_ops.values():
            db_cursor.execute(sql_stmt)
            db_cursor.commit()

        return existing_pet
    except Exception as e:
        logger.error(f"Error deleting pet from the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()
