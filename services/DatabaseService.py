import os
import psycopg2

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

def db_conn():
  return psycopg2.connect(database=DB_DATABASE, host=DB_HOST, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD)