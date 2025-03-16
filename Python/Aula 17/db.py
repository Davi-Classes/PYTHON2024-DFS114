import mysql.connector as mysql

# Criando Conexão
conn = mysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database='escola'
)

def get_cursor():
    return conn.cursor()

def commit():
    conn.commit()