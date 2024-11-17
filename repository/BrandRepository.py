from services.DatabaseService import db_conn
from models.Brand import Brand

def get_all_brands():
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''SELECT * FROM brands''')
  data = cur.fetchall()
  cur.close()
  conn.close()

  brands = [Brand(id=brand[0], brand_name=brand[1], owner_name=brand[2], status=brand[3]) for brand in data]

  return brands

def get_brand_by_id(brand_id):
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''SELECT * FROM brands WHERE id = %s''', (brand_id,))
  data = cur.fetchone()
  cur.close()
  conn.close()
  
  if data:
    return Brand(id=data[0], brand_name=data[1], owner_name=data[2], status=data[3])
  else:
    None

def create_brand(brand_name, owner_name, status):
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''INSERT INTO brands (brand_name, owner_name, status) VALUES (%s, %s, %s) RETURNING *''', (brand_name, owner_name, status,))
  new_data = cur.fetchone()
  conn.commit()
  cur.close()
  conn.close()
    
  return Brand(id=new_data[0], brand_name=new_data[1], owner_name=new_data[2], status=new_data[3])

def update_brand(brand_id, brand_name, owner_name, status):
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''UPDATE brands SET brand_name=%s, owner_name=%s, status=%s WHERE id=%s RETURNING *''', (brand_name, owner_name, status, brand_id,))
  new_data = cur.fetchone()
  conn.commit()
  cur.close()
  conn.close()
    
  return Brand(id=new_data[0], brand_name=new_data[1], owner_name=new_data[2], status=new_data[3])

def delete_brand(brand_id):
  conn = db_conn()
  cur = conn.cursor()
  cur.execute('''DELETE FROM brands WHERE id = %s''', (brand_id,))
  conn.commit()
  cur.close()
  conn.close()