import db_connect
import queries

db_object = db_connect.DB()
query_object = queries.Queries(db_object.db)
query_object.db_operation('create', '''    CREATE TABLE Customer2(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(100),
    LOAN_AMOUNT REAL
    )
    ''')

query_object.db_operation('insert', '''        insert into Customer2(ID, name, age, address, LOAN_AMOUNT)
        values(1,'ABC',24,'MDU',100000)''')
query_object.db_operation('insert', '''        insert into Customer2(ID, name, age, address, LOAN_AMOUNT)
        values(2,'DEF',30,'CHN',200000)''')
query_object.db_operation('insert', '''        insert into Customer2(ID, name, age, address, LOAN_AMOUNT)
        values(3,'GHI',27,'BAN',300000)''')
query_object.db_operation('insert', '''        insert into Customer2(ID, name, age, address, LOAN_AMOUNT)
        values(4,'JKL',21,'SON',100000)''')

query_object.db_operation('delete', '''delete from Customer2 where id = 3''')


query_object.db_operation('insert', '''        insert into Customer2(ID, name, age, address, LOAN_AMOUNT)
             values(3,'GHI',27,'BAN',300000)''')

query_object.db_select('''select * from Customer2''', 'fetchall')


del db_object
del query_object
