import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


class Engine:
    def __init__(self):
        self.db = create_engine('postgresql://{}:{}@{}/{}'.format(os.getenv('user'), os.getenv('password'),
                                                                  os.getenv('host'), os.getenv('database'))).connect()

    def __del__(self):
        self.db.close()
        print('closed')
