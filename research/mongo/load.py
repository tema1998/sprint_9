import os
import time
import logging
from typing import Callable

from pymongo import MongoClient

from research.fake_data import create_fake_like, create_fake_review, create_fake_bookmark
from research.settings import settings
from multiprocessing import Process

# Set logger level to INFO.
logging.getLogger().setLevel(logging.INFO)

# Get data from settings.
mongo_host = settings.mongo_host
mongo_port = settings.mongo_port
mongo_db = settings.mongo_db
number_of_entries = settings.number_of_entries

# Solution of warning 'MongoClient opened before fork'
if os.getpid() == 0:
    client = MongoClient(mongo_host, mongo_port)
else:
    client = MongoClient(mongo_host, mongo_port, connect=False)

mongo_db = client[mongo_db]


def insert(
        faker: Callable,
        collection_name: str
) -> None:
    collection = mongo_db.get_collection(collection_name)

    start_time = time.time()
    for _ in range(number_of_entries):
        collection.insert_one(faker())
    end_time = time.time()

    logging.info(f"Total time of loading collection '{collection_name}' with {number_of_entries} entries = "
             f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)")


if __name__ == "__main__":

    # Run multiprocessing of adding data to MongoDB.
    p1 = Process(target=insert, args=(create_fake_like, 'likes'), daemon=True)
    p2 = Process(target=insert, args=(create_fake_review, 'reviews'), daemon=True)
    p3 = Process(target=insert, args=(create_fake_bookmark, 'bookmarks'), daemon=True)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()