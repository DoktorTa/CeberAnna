from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


metadata = MetaData()
Base = declarative_base()

user_table = Table('user_table', metadata,
                   Column('user_id', Integer, primary_key=True),
                   Column('user_tag', String),
                   Column('user_name', String),
                   Column('user_status', String),
                   Column('chat_id', Integer),
                   Column('user_inviter', String),
                   )

requests_table = Table('requests_table', metadata,
                       Column('full_name', String),
                       Column('chat_id', Integer),
                       Column('user_tag', String),
                       Column('user_id', Integer, primary_key=True),
                       )

storage_table = Table('storage_table', metadata,
                      Column('name_group', String),
                      Column('name_subgroup', String),
                      Column('name_id', String, primary_key=True),
                      Column('count', Integer),
                      )

objects_name = Table('objects_name', metadata,
                     Column('objects_name', String))

engine = create_engine('sqlite:///:memory:', echo=True)

session = Session(engine)
metadata.create_all(engine)
conn = engine.connect()



