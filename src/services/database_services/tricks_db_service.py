import logging
import sqlalchemy

from src import config
from src.classes.Trick import Trick

logger = logging.getLogger("tricks_db_service_logger")


def connect_to_db():
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://" + config.mysql_user + ":" + config.mysql_pw + "@" + config.mysql_host)
    cursor = engine.connect()
    cursor.execute(sqlalchemy.text("USE %s" % config.mysql_db))
    return cursor


def get_trick(trick_id: str):
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text(f"SELECT * FROM tricks_table WHERE trick_id = '{trick_id}'")
        result = db_cursor.execute(sql).fetchone()
        if result:
            trick = Trick(
                user_id=result[3],
                pet_id=result[2],
                name=result[1],
                trick_id=result[0]
            )
            logger.debug(f"Tricks DB Service: trick named {trick.name} found with id: {trick_id}")
            return trick
        else:
            logger.info(f"Tricks DB Service: no trick found with id: {trick_id}")
            return None
    except Exception as e:
        logger.error(f"Error getting trick with trick id: {trick_id} from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def get_all_tricks_by_pet(pet_id: str):
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text(f"SELECT * FROM tricks_table WHERE pet_id = '{pet_id}'")
        results = db_cursor.execute(sql).fetchall()
        tricks_list = []
        for result in results:
            trick = Trick(
                user_id=result[3],
                pet_id=result[2],
                name=result[1],
                trick_id=result[0]
            )
            tricks_list.append(trick)
        return tricks_list
    except Exception as e:
        logger.error(f"Error getting tricks from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def create_trick(trick):

    db_cursor = connect_to_db()

    try:
        insert_query = sqlalchemy.text(
            "INSERT INTO tricks_table (trick_id, trick_name, pet_id, user_id) "
            "VALUES (:trick_id, :name, :pet_id, :user_id)"
        )
        trick_data = {
            "trick_id": trick.trick_id,
            "name": trick.name,
            "pet_id": trick.pet_id,
            "user_id": trick.user_id
        }
        db_cursor.execute(insert_query, trick_data)
        db_cursor.commit()
        logger.info("Trick added to the database successfully!")
        return trick
    except Exception as e:
        logger.error(f"Error inserting trick into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def update_trick(trick_id, new_trick_obj):
    db_cursor = connect_to_db()

    try:
        # If the pet exists, update its information
        update_sql = sqlalchemy.text(f"""
                UPDATE tricks_table
                SET name = '{new_trick_obj.name}'
                WHERE trick_id = '{trick_id}'
            """)
        db_cursor.execute(update_sql)
        db_cursor.commit()

        return new_trick_obj
    except Exception as e:
        logger.error(f"Error insterting trick into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def delete_trick(trick_id):

    db_cursor = connect_to_db()

    try:
        # Check if the pet with the given pet_id exists
        existing_trick = get_trick(trick_id=trick_id)

        if not existing_trick:
            logger.error(f"Tricks DB Service: No trick found with id: {trick_id}")
            return None

        logger.info(f"Tricks DB Service: Deleting trick with trick_id {trick_id} from database")

        deletion_ops = {
            'delete_tricks_sql': sqlalchemy.text(f"DELETE FROM tricks_table WHERE user_id = '{trick_id}'"),
            'delete_clicks_sql': sqlalchemy.text(f"DELETE FROM clicks_table WHERE user_id = '{trick_id}'")
        }

        for sql_stmt in deletion_ops.values():
            db_cursor.execute(sql_stmt)
            db_cursor.commit()

        return existing_trick
    except Exception as e:
        logger.error(f"Error deleting trick from the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()
