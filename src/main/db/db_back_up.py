import datetime

import sqlalchemy.engine.row
from sqlalchemy.ext.serializer import loads, dumps
from db import db_map

db_for_backup = {
    # 'requests_table': db_map.requests_table,
    'users_table': db_map.user_table}


def backup_db():
    for db_name, db_data in db_for_backup.items():

        db = db_map.session.query(db_data)

        dump = dumps(db.all())
        data = datetime.datetime.today().strftime(r'%Y_%m_%d_%H_%M')
        with open(f'db/back_up/{db_name}/{str(data)}.pickle', 'wb') as file:
            file.write(dump)


def load_backup(data=None):
    data_backup = {}
    root_symbol = '!'

    if data is None:
        print(f'Enter "{root_symbol}" after the required backup date,'
              f' unless you want to configure backups more precisely.')
        data = input('Data:')

    if root_symbol not in data:
        for key in db_for_backup.keys():
            data_backup.update({key: input(f'{key}:')})
    else:
        data = data.replace(root_symbol, '')
        for key in db_for_backup.keys():
            data_backup.update({key: data})

    for db_name, db_data in db_for_backup.items():
        data = data_backup.get(db_name)
        with open(f'db/back_up/{db_name}/{data}.pickle', 'rb') as file:
            dump = file.read()
        restore_q = loads(dump, db_data, db_map.session)
        db_map.conn.execute(db_data.insert().values(*restore_q))
        db_map.session.commit()



