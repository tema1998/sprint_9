import os
import time
import logging

from pymongo import MongoClient

from research.settings import settings
from research.fake_data import const_film_id, const_user_id


# Set logger level to INFO.
logging.getLogger().setLevel(logging.INFO)

# Get data from settings.
mongo_host = settings.mongo_host
mongo_port = settings.mongo_port
mongo_db = settings.mongo_db
number_of_entries = settings.number_of_entries

client = MongoClient(mongo_host, mongo_port)
mongo_db = client[mongo_db]


def count_likes_of_film() -> None:
    """
     Function count the number of likes for a film.
    """
    start_time = time.time()
    mongo_db['likes'].count_documents({'film_id': const_film_id,
                                'type': 10})
    end_time = time.time()
    logging.info(f"Total time of counting likes of the film = "
             f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)")

def count_average_film_rating() -> None:
    """
     Function count the number of bookmarks of user.
    """
    start_time = time.time()
    mongo_db['review'].aggregate([
        {
            '$match': {'film_id': const_film_id}
        },
        {
            '$group': {'_id': "film_id",'average_rating': {'$avg': "$rating"}}
        }])
    end_time = time.time()
    logging.info(f"Total time of counting average rating of the film = "
             f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)")

def count_number_of_bookmarks() -> None:
    """
     Function count the number of bookmarks of the user.
    """
    start_time = time.time()
    mongo_db['bookmarks'].count_documents({'user_id': const_user_id})
    end_time = time.time()
    logging.info(f"Total time of counting bookmarks of the user = "
             f"{end_time-start_time} seconds ({(end_time-start_time)/60} minutes)")


if __name__ == "__main__":
    count_likes_of_film()
    count_average_film_rating()
    count_number_of_bookmarks()