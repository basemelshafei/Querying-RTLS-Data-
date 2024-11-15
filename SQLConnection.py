import pandas as pd
import pyodbc
pyodbc.drivers()

conn = pyodbc.connect(
    r'DRIVER={xxxx};'
    r'SERVER=xxxx;'
    r'DATABASE=Master;'
    r'TrustedServerCertificate=yes;'
    r'UID=xxxx;'
    r'PWD=xxxxxx'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM ;")
row = cursor.fetchone()
print(row)
cursor.close()

df = pd.read_sql_query("SELECT * FROM ;", conn)
print(df.head())
print(df)

conn.close()
