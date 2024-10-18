import os
import time
import logging
from typing import Callable

import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

from research.fake_data import create_fake_like, create_fake_review, create_fake_bookmark
from research.settings import settings
from multiprocessing import Process

# Set logger level to INFO.
logging.getLogger().setLevel(logging.INFO)

number_of_entries = settings.number_of_entries

def create_tables():
    with psycopg.connect(**settings.get_pg_dsn(), row_factory=dict_row,
                         cursor_factory=ClientCursor) as conn, conn.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS likes (id serial PRIMARY KEY, user_id UUID, film_id UUID, type smallserial, datetime timestamp);")
        cursor.execute("CREATE TABLE IF NOT EXISTS reviews (id serial PRIMARY KEY, user_id UUID, film_id UUID, text text, rating smallserial, datetime timestamp);")
        cursor.execute("CREATE TABLE IF NOT EXISTS bookmarks (id serial PRIMARY KEY, user_id UUID, film_id UUID, datetime timestamp);")
def insert(
        faker: Callable,
        collection_name: str
) -> None:
    with psycopg.connect(**settings.get_pg_dsn(), row_factory=dict_row, cursor_factory=ClientCursor) as conn, conn.cursor() as cursor:
        start_time = time.time()
        for _ in range(number_of_entries):
            fake_data = faker()
            data_columns = ", ".join(list(fake_data.keys()))
            data_values = ", ".join(map(lambda x: f"'{str(x)}'", list(fake_data.values())))
            query = f"INSERT INTO {collection_name} ({data_columns}) VALUES ({data_values})"
            cursor.execute(query)

        end_time = time.time()

    logging.info(f"Total time of loading collection '{collection_name}' with {number_of_entries} entries = "
             f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)")


if __name__ == "__main__":
    # Create tables for data.
    create_tables()

    # Run multiprocessing of adding data to PostgreSQL.
    p1 = Process(target=insert, args=(create_fake_like, 'likes'), daemon=True)
    p2 = Process(target=insert, args=(create_fake_review, 'reviews'), daemon=True)
    p3 = Process(target=insert, args=(create_fake_bookmark, 'bookmarks'), daemon=True)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()