from services.DatabaseService import db_conn

def create_brands_table():
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS brands(id SERIAL PRIMARY KEY, brand_name VARCHAR(255) NOT NULL, owner_name VARCHAR(255) NOT NULL, status VARCHAR(255) NOT NULL)''')
  conn.commit()
  cur.close()
  conn.close()