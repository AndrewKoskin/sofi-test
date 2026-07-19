import random
from datetime import UTC, datetime

import pytest
from faker.proxy import Faker

from framework.models.user import Gender, UserCreate

faker = Faker("ru_RU")


@pytest.fixture
def valid_user() -> UserCreate:
    age = random.randint(18, 100)
    return UserCreate(
        name=faker.name(),
        email=faker.email(safe=True),
        age=age,
        interests=faker.words(nb=5),
        gender=random.choice(list(Gender)),
        phone=faker.numerify("+7##########"),
        birth_date=datetime.combine(
            faker.date_of_birth(minimum_age=age, maximum_age=age),
            datetime.min.time(),
            tzinfo=UTC,
        ),
    )
