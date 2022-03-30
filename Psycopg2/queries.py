import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG)


class Queries:
    def __init__(self, db):
        self.db = db
        self.pointer = db.cursor()

    def db_select(self, query, fetch, number=None):
        try:
            self.pointer.execute(query)
            self.db.commit()
            file = open('data.txt', 'w')
            file.write('Usernames' + '\n')
            if fetch == "fetchall":
                rows = self.pointer.fetchall()
            elif fetch == "fetchone":
                rows = self.pointer.fetchone()
                file.write(rows[1])
                return
            elif fetch == "fetchmany":
                rows = self.pointer.fetchmany(number)
            for row in rows:
                file.writelines(row[1] + '\n')
            logging.info("data were written to the file")
        except Exception as e:
            logging.error("Insertion failed ", e)

    def db_operation(self,  operation, query, fetch=None):
        try:
            self.pointer.execute(query)
            self.db.commit()
            logging.info(operation + " is done")
        except Exception as e:
            logging.error(operation + " failed ", e)

    def rollback(self):
        self.pointer.execute("ROLLBACK")
        self.db.commit()

    def __del__(self):
        self.pointer.close()
