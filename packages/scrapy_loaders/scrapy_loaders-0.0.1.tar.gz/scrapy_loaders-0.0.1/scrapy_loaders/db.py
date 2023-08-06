from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
# from AttackMitre.models import DeclarativeBase


class Db(object):
    engine = None

    def __init__(self, settings, declarative_base):
        self.settings = settings
        self.declarative_base = declarative_base

    def connect(self):
        self.engine = create_engine(str(URL(**self.settings)))

    def create_all_tables(self):
        self.declarative_base.metadata.create_all(self.engine)
        return True

    def drop_all_tables(self):
        self.declarative_base.metadata.drop_all(self.engine)
        return True
