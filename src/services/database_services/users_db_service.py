import logging
import sqlalchemy

from src import config
from src.classes.Pet import Pet
from src.classes.User import User
from src.services.database_services.pets_db_service import get_all_pets

logger = logging.getLogger("pets_db_service_logger")


def connect_to_db():
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://" + config.mysql_user + ":" + config.mysql_pw + "@" + config.mysql_host)
    cursor = engine.connect()
    cursor.execute(sqlalchemy.text("USE %s" % config.mysql_db))
    return cursor


def get_user(user_id: str):
    db_cursor = connect_to_db()

    try:
        user_sql = sqlalchemy.text(f"SELECT * FROM users_table WHERE user_id = '{user_id}'")
        user_result = db_cursor.execute(user_sql).fetchone()

        if user_result:
            user = User(
                user_id=user_result[0],
                name=user_result[1],
                dob=user_result[2],
                email=user_result[3],
                phone_number=user_result[4],
                creation_timestamp=user_result[5],
                pets={pet.pet_id: pet for pet in get_all_pets(user_id=user_id)}
            )

            logger.debug(f"Users DB Service: user named {user.name} found with id: {user_id}")
            return user
        else:
            logger.info(f"User DB Service: no user found with id: {user_id}")
            return None
    except Exception as e:
        logger.error(f"Error getting user with user id: {user_id} from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def get_all_users():
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text("SELECT * FROM users_table")
        results = db_cursor.execute(sql).fetchall()
        users_list = []
        for user_result in results:
            user = User(
                user_id=user_result[0],
                name=user_result[1],
                dob=user_result[2],
                email=user_result[3],
                phone_number=user_result[4],
                creation_timestamp=user_result[5],
                pets={pet.pet_id: pet for pet in get_all_pets(user_id=user_result[0])}
            )
            users_list.append(user)
        return users_list
    except Exception as e:
        logger.error(f"Error getting users from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def create_user(user):
    db_cursor = connect_to_db()

    try:
        insert_query = sqlalchemy.text(
            "INSERT INTO users_table (user_id, name, dob, email, phone_number, creation_timestamp) "
            "VALUES (:user_id, :name, :dob, :email, :phone_number, :creation_timestamp)"
        )
        user_data = {
            "pet_id": user.user_id,
            "name": user.name,
            "dob": user.dob.strftime('%Y-%m-%d'),  # Convert to MySQL DATE format
            "email": user.email,
            "phone_number": user.phone_number,
            "creation_timestamp": user.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # Convert to MySQL TIMESTAMP format
        }
        db_cursor.execute(insert_query, user_data)
        db_cursor.commit()
        logger.info("User added to the database successfully!")
        return user
    except Exception as e:
        logger.error(f"Error inserting user into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def update_user(user_id, new_user_obj):
    db_cursor = connect_to_db()

    try:
        # If the User exists, update their information
        update_sql = sqlalchemy.text(f"""
                UPDATE user_table
                SET name = '{new_user_obj.name}', dob = '{new_user_obj.dob.strftime('%Y-%m-%d')}', email = '{new_user_obj.email}', phone_number = '{new_user_obj.phone_number}'
                WHERE user_id = '{user_id}'
            """)
        db_cursor.execute(update_sql)
        db_cursor.commit()

        return new_user_obj
    except Exception as e:
        logger.error(f"Error inserting user into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def delete_user(user_id):
    db_cursor = connect_to_db()

    try:
        # Check if the pet with the given pet_id exists
        existing_user = get_user(user_id=user_id)

        if not existing_user:
            logger.error(f"User DB Service: No user found with id: {user_id}")
            return None

        logger.info(f"User DB Service: Deleting user with user_id {user_id} from database")

        deletion_ops = {
            'delete_user_sql': sqlalchemy.text(f"DELETE FROM users_table WHERE user_id = '{user_id}'"),
            'delete_pets_sql': sqlalchemy.text(f"DELETE FROM pets_table WHERE user_id = '{user_id}'"),
            'delete_tricks_sql': sqlalchemy.text(f"DELETE FROM tricks_table WHERE user_id = '{user_id}'"),
            'delete_clicks_sql': sqlalchemy.text(f"DELETE FROM clicks_table WHERE user_id = '{user_id}'")
        }

        for sql_stmt in deletion_ops.values():
            db_cursor.execute(sql_stmt)
            db_cursor.commit()
        return existing_user
    except Exception as e:
        logger.error(f"Error deleting pet from the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()
