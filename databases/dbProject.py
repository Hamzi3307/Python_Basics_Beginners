import sqlite3

class database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'test')
        print(self.table,self.filename)
    @property
    def filename(self): self._filename

    @filename.setter
    def filename(self,fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): self._table
    @table.setter
    def table(self,t): self._table = t
    @table.deleter
    def table(self): self._table = 'test'

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by name'.format(self._table))
        for row in cursor:
            yield dict(row)

    def sql_do(self, sql, *params):
        self._db.execute(sql,params)
        self._db.commit()

    def insert(self, row):
        self._db.execute('insert into {} (id, name) values (?, ?)'.format(self._table), (row['id'], row['name']))
        self._db.commit()

    def retreive(self, key):
        cursor = self._db.execute('select * from {} where id = ?'.format(self._table),(key,))
        return dict(cursor.fetchone())

    def update(self, row):
        self._db.execute('update {} set name= ? where id = ?'.format(self._table),(row['name'], row['id']))
        self._db.commit()
    def delete(self,key):
        self._db.execute('delete from {} where id = ?'.format(self._table),(key,))

    def disp_rows(self):
        cursor = self._db.execute('select * from {}'.format(self._table))
        for a in cursor:
            print(dict(a))

def main():
    db = database(filename='project.db', table='BSCS')
    print('Create Table BSCS')
    db.sql_do('drop table if exists BSCS')
    db.sql_do('create table BSCS (id int, name text)')

    #Inserting data
    db.insert(dict(id=1, name='Hamza'))
    db.insert(dict(id=2, name='Ali'))
    db.insert(dict(id=3, name='Khan'))
    db.insert(dict(id=4, name='Ahmad'))

    #displaying rows
    db.disp_rows()

    #Retreiving data
    print('we have id : 1 , name : ', db.retreive(1))

    #Updating Data
    db.update(dict(id=1 , name='Saad'))

    #Deleting Data
    db.delete(2)

    #displaying rows
    for a in db : print(a)


if __name__=='__main__' : main()