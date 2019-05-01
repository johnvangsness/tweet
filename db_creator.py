from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///trump.db', echo=True)
Base = declarative_base()


class Tweets(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __repr__(self):
        return "<Tweets: {}>".format(self.name)

class Speeches(Base):
    __tablename__ = "speeches"

    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __repr__(self):
        return "<Speeches: {}>".format(self.name)

class Interviews(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __repr__(self):
        return "<Interviews: {}>".format(self.name)

# create tables
Base.metadata.create_all(engine)
