import datetime

from sqlalchemy.ext.serializer import loads, dumps
from db import db_map


def backup_db():
    db = db_map.session.query(db_map.requests_table)

    dump = dumps(db.all(), protocol=1)
    data = datetime.datetime.today()
    with open('db/back_up/' + str(data) + '.pickle', 'wb') as file:
        file.write(dump)


def load_backup(data: str):
    with open('back_up/' + data, 'r') as file:
        dump = file.read()
    restore_q = loads(data, db_map.metadata, db_map.metadata.Session)


