import pandas as pd


class Queries:
    def __init__(self, db_conn):
        self.db = db_conn

    def create(self, table_name, df):
        try:
            frame = df.to_sql(table_name, self.db, if_exists='fail')
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("PostgreSQL Table {} has been created successfully.".format(table_name))

    def select(self, database):
        data_frame = pd.read_sql("select * from \"{}\"".format(database), self.db)
        pd.set_option('display.expand_frame_repr', False)

        print(data_frame)
