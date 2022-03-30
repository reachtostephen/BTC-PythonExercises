import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            port=os.getenv('port')
        )
df = pd.read_sql_query("select * from customer2", conn)
print(df.head())

data = {'id': 5, 'name': 'MNO', 'age': [34], 'address': 'DEL', 'loan_amount': [150000]}
df1 = pd.DataFrame(data)
df.to_sql('customer2', con=conn, index=False)
conn.close()
