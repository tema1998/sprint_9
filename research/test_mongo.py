import time
from typing import Callable

from pymongo import MongoClient

from research.fake_data import create_fake_like
from settings import settings
from multiprocessing import Process


mongo_host = settings.mongo_host
mongo_port = settings.mongo_port
mongo_db = settings.mongo_db
number_of_entries = settings.number_of_entries

client = MongoClient(mongo_host, mongo_port, connect=True)
mongo_db = client[mongo_db]


def test_insert(
        faker: Callable,
        collection_name: str
) -> None:
    collection = mongo_db.get_collection(collection_name)
    start_time = time.time()
    for _ in range(number_of_entries):
        collection.insert_one(faker())
    end_time = time.time()
    print(f"Total time of loading collection '{collection_name}' with {number_of_entries} entries = "
          f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)"
    )

if __name__ == "__main__":
    test_insert(create_fake_like, "likes")

    # p1 = Process(target=test_insert, args=('bob',), daemon=True)
    # p2 = Process(target=test_insert, args=('alice',), daemon=True)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()