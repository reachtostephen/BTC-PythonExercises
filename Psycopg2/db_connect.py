import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DB:
    def __init__(self):
        self.db = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            port=os.getenv('port')
        )
        print(self.db)

    def __del__(self):
        self.db.close()
