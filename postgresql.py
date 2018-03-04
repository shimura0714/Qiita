import psycopg2


def get_connection():
  return psycopg2.connect('postgresql://######:@127.0.0.1:5432/python-dev')

conn = get_connection()
cur  = conn.cursor()
cur.execute("insert into exmaple (id, name) values('0001', '########')")
conn.commit()
cur.close()
conn.close()
