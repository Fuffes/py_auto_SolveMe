from sqlalchemy import Column,Boolean, Integer, String, Text, BigInteger
from db import Model


class User(Model):

    __tablename__ = "dbusers"

    id = Column(BigInteger, primary_key=True)
    age = Column(BigInteger)
    name = Column(Text)


