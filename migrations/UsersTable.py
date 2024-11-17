from services.DatabaseService import db_conn

def create_users_table():
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, username VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)''')
  conn.commit()
  cur.close()
  conn.close()