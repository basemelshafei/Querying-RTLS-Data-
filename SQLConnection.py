import pandas as pd
import pyodbc
pyodbc.drivers()

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=UON-RTLS01\SQLEXPRESS;'
    r'DATABASE=Master;'
    r'TrustedServerCertificate=yes;'
    r'UID=LocSystem;'
    r'PWD=SQLConnection1234'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM LocSystem.LocSystem.trackpos;")
row = cursor.fetchone()
print(row)
cursor.close()

df = pd.read_sql_query("SELECT xpos, ypos, zpos FROM LocSystem.LocSystem.trackpos;", conn)
print(df.head())
print(df)

conn.close()
