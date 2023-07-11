import sqlite3

def create(db, row):
    db.execute('insert into test (Rno, name) values (?, ?)', (row['Rno'], row['name']))
    db.commit()

def retrieve(db, Rno):
    cursor = db.execute('select * from test where Rno = ?', (Rno,))
    return cursor.fetchall()

def update(db, row):
    db.execute('update test set name=? where Rno = ?', (row['name'], row['Rno']))
    db.commit()

def delete(db, Rno):
    db.execute('delete from test where Rno = ?', (Rno,))
    db.commit()

def disp_rows(db):
    cursor = db.execute('select * from test')
    for i in cursor:
        print(dict(i))
def main():
    db = sqlite3.connect('databases/crud.db')
    db.row_factory = sqlite3.Row
    print('CREATE TABLE NAMED TEST')
    db.execute('drop table if exists test')
    db.execute('create table test (Rno int, name text)')

    print('Table Created')
    disp_rows(db)

    print('After create Data')
    create(db, (dict(Rno=1, name='Hamza')))
    create(db, (dict(Rno=2, name='Khan')))
    create(db, (dict(Rno=3, name='Ahmad')))
    create(db, (dict(Rno=4, name='Ali')))
    disp_rows(db)

    print('\nRetrieving Data')
    print(dict(retrieve(db,2)))

    print('\nupdate roll no 2 to Nadan')
    update(db, dict(Rno=2, name='Nadan'))
    disp_rows(db)

    print('\nDeleting Data Rno 3')
    delete(db, 3)
    disp_rows(db)


if __name__ == '__main__': main()