class Item:
    name_group: str
    name_subgroup: str
    name_id: str
    count: int

    def __str__(self):
        return f'{self.name_group}\n' \
               f'{self.name_subgroup}\n' \
               f'{self.name_id}\n' \
               f'{self.count}\n'

    def init_db_storage(self, db_line: dict):
        try:
            self.name_group = db_line.get('name_group')
            self.name_subgroup = db_line.get('name_subgroup')
            self.name_id = db_line.get('name_id')
            self.count = db_line.get('count')
            return self
        except Exception as e:
            return None

    def init_str(self, line: str):
        try:
            str_item = line.split(' ')
            self.name_group = str_item[0]
            self.name_subgroup = str_item[1]
            self.name_id = str_item[2]
            self.count = int(str_item[3])
            return self
        except Exception as e:
            return None
