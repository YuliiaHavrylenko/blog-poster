from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:your_password@localhost:5432/blog_poster")

Base = declarative_base()


class Topic(Base):
    __tablename__ = "topics"
    topic_id = Column(Integer)

