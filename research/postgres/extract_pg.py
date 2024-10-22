import os
import time
import logging

import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

from research.settings import settings
from research.fake_data import const_film_id, const_user_id


# Set logger level to INFOs
logging.getLogger().setLevel(logging.INFO)

# Get data from settings.
number_of_entries = settings.number_of_entries


def count_likes_of_film() -> None:
    """
    Function count the number of likes for a film.
    """
    start_time = time.time()
    with psycopg.connect(
        **settings.get_pg_dsn(), row_factory=dict_row, cursor_factory=ClientCursor
    ) as conn, conn.cursor() as cursor:
        cursor.execute(
            f"SELECT COUNT(*) FROM likes WHERE film_id='{const_film_id}' AND type=10;"
        )
        cursor.fetchall()
    end_time = time.time()
    logging.info(
        f"Total time of counting likes of the film = "
        f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)"
    )


def count_average_film_rating() -> None:
    """
    Function count the number of bookmarks of user.
    """
    start_time = time.time()
    # TODO Write aggregation.
    with psycopg.connect(
        **settings.get_pg_dsn(), row_factory=dict_row, cursor_factory=ClientCursor
    ) as conn, conn.cursor() as cursor:
        cursor.execute(
            f"SELECT AVG(rating) FROM reviews WHERE film_id='{const_film_id}' GROUP BY film_id;"
        )
        cursor.fetchall()
        end_time = time.time()
    logging.info(
        f"Total time of counting average rating of the film = "
        f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)"
    )


def count_number_of_bookmarks() -> None:
    """
    Function count the number of bookmarks of the user.
    """
    start_time = time.time()
    with psycopg.connect(
        **settings.get_pg_dsn(), row_factory=dict_row, cursor_factory=ClientCursor
    ) as conn, conn.cursor() as cursor:
        cursor.execute(
            f"SELECT COUNT(*) FROM bookmarks WHERE user_id='{const_user_id}';"
        )
        cursor.fetchall()
    end_time = time.time()
    logging.info(
        f"Total time of counting bookmarks of the user = "
        f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)"
    )


if __name__ == "__main__":
    count_likes_of_film()
    count_average_film_rating()
    count_number_of_bookmarks()
