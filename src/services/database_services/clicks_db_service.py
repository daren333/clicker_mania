import logging
import sqlalchemy

from src import config
from src.classes.Click import Click

logger = logging.getLogger("clicks_db_service_logger")


def connect_to_db():
    engine = sqlalchemy.create_engine(
        "mysql+pymysql://" + config.mysql_user + ":" + config.mysql_pw + "@" + config.mysql_host)
    cursor = engine.connect()
    cursor.execute(sqlalchemy.text("USE %s" % config.mysql_db))
    return cursor


def get_click(click_timestamp: str):
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text(f"SELECT * FROM clicks_table WHERE click_timestamp = '{click_timestamp}'")
        result = db_cursor.execute(sql).fetchone()
        if result:
            click = Click(
                timestamp=result[0],
                treat_likelihood=result[1],
                treated=result[2],
                user_id=result[3],
                pet_id=result[4],
                trick_id=result[5]
            )
            logger.debug(f"Clicks DB Service: click found with timestamp: {click_timestamp}")
            return click
        else:
            logger.info(f"Clicks DB Service: no click found with timestamp: {click_timestamp}")
            return None
    except Exception as e:
        logger.error(f"Error getting click with click timestamp: {click_timestamp} from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def get_all_clicks_by_trick(trick_id: str):
    db_cursor = connect_to_db()

    try:
        sql = sqlalchemy.text(f"SELECT * FROM clicks_table WHERE trick_id = '{trick_id}'")
        results = db_cursor.execute(sql).fetchall()
        clicks_list = []
        for result in results:
            click = Click(
                timestamp=result[0],
                treat_likelihood=result[1],
                treated=result[2],
                user_id=result[3],
                pet_id=result[4],
                trick_id=result[5]
            )
            clicks_list.append(click)
        return clicks_list
    except Exception as e:
        logger.error(f"Error getting clicks from database: {str(e)}")
        raise e
    finally:
        db_cursor.close()


def create_click(click):

    db_cursor = connect_to_db()

    try:
        insert_query = sqlalchemy.text(
            "INSERT INTO clicks_table (click_timestamp, treat_likelihood, treated, user_id, pet_id, trick_id) "
            "VALUES (:click_timestamp, :treat_likelihood, :treated, :user_id, :pet_id, :trick_id)"
        )
        click_data = {
            "click_timestamp": click.timestamp,
            "treat_likelihood": click.treat_likelihood,
            "treated": click.treated,
            "user_id": click.user_id,
            "pet_id": click.pet_id,
            "trick_id": click.trick_id
        }
        db_cursor.execute(insert_query, click_data)
        db_cursor.commit()
        logger.info("Click added to the database successfully!")
        return click
    except Exception as e:
        logger.error(f"Error inserting click into the database: {str(e)}")
        raise e
    finally:
        db_cursor.close()

