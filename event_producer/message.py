from random import seed, choice

from faker import Faker

STATUSES = [
    "Active",
    "Disabled",
    "Pending",
]


def generate_fake_message():
    fake = Faker()

    return {
        "name": fake.name(),
        "job": fake.job(),
        "age": fake.date_of_birth(minimum_age=18),
        "status": choice(STATUSES),
    }