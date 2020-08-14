from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship

from .database import Base


class Paste(Base):
    '''Represents a loaded paste'''
    __tablename__ = "pastes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    content = Column(String)
    expires = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="pastes")


association_table = Table('users_groups_association', Base.metadata,  # table for many-to-many relation
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)


class User(Base):
    '''Represents a single user'''
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    groups = relationship("Group",
                          secondary=association_table,
                          backref="users")
    pastes = relationship("Paste", back_populates="owner")


class Group(Base):
    '''Represents a group with specifies users assigned to it'''
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    groupname = Column(String, unique=True, index=True)