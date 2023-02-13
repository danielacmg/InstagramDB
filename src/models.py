import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

follower = Table(
    "follower",
    Base.metadata,
    Column("follower", ForeignKey("user.id")),
    Column("following", ForeignKey("user.id")),
)

class User(Base):
    __tablename__ = 'user'
    # id = Column(Integer, primary_key=True)
    id = Column(String(250), primary_key=True)
    first_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id")) 
    post_id = Column(Integer, ForeignKey("post.id"), index=True) 
    body = Column(String(250), nullable=False)
    user = relationship("User")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("user.id")) 
    image = Column(String(300))
    date = Column(String(300))

    # Relationships
    author = relationship("User")
    comments = relationship("Comment")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
