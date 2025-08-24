#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]



session.query(Game).delete()
session.commit()


# Single object
botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
session.add(botw)
session.commit()

# Multiple objects
ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
session.bulk_save_objects([ffvii, mk8])
session.commit()
