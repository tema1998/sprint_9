from random import choice, randint, choices
from uuid import uuid4

from faker import Faker

fake = Faker()

# comment
const_film_id = 'fa93bca0-8849-4523-881d-a9c5793eaf77'
const_user_id = '39ea84fe-a241-4d7b-a4c0-cee32f9ceefa'

def create_fake_like() -> dict:
    return {
        "user_id": choices(population=[str(uuid4()), const_user_id], weights=[0.9, 0.1], k=1)[0],
        "film_id": choices(population=[str(uuid4()), const_film_id], weights=[0.9, 0.1], k=1)[0],
        "type": choice([10, 0]), # Like - 10, Dislike - 0
        "datetime": fake.date_time_between(start_date="-10d", end_date="now"),
    }


def create_fake_review() -> dict:
    return {
        "user_id": choices(population=(str(uuid4()), const_user_id), weights=[0.9, 0.1], k=1)[0],
        "film_id": choices(population=(str(uuid4()), const_film_id), weights=[0.9, 0.1], k=1)[0],
        "text": fake.text(),
        "rating": randint(0, 10),
        "datetime": fake.date_time_between(start_date="-10d", end_date="now"),
    }

def create_fake_bookmark() -> dict:
    return {
        "user_id": choices(population=[str(uuid4()), const_user_id], weights=[0.9, 0.1], k=1)[0],
        "film_id": choices(population=[str(uuid4()), const_film_id], weights=[0.9, 0.1], k=1)[0],
        "datetime": fake.date_time_between(start_date="-10d", end_date="now"),
    }
