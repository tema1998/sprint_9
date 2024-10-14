from random import choice, randint
from uuid import uuid4

from faker import Faker

fake = Faker()


def create_fake_like() -> dict:
    return {
        "user_id": str(uuid4()),
        "film_id": str(uuid4()),
        "type": choice([10, 0]), # Like - 10, Dislike - 0
        "datetime": fake.date_time_between(start_date="-10d", end_date="now"),
    }


def create_fake_review() -> dict:
    return {
        "user_id": str(uuid4()),
        "film_id": str(uuid4()),
        "text": fake.text(),
        "rating": randint(0, 10),
        "datetime": fake.date_time_between(start_date="-10d", end_date="now"),
    }

def create_fake_bookmark() -> dict:
    return {
        "user_id": str(uuid4()),
        "film_id": str(uuid4()),
        "datetime": fake.date_time_between(start_date="-10d", end_date="now"),
    }
