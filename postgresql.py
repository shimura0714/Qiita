import psycopg2


def get_connection():
  return psycopg2.connect('postgresql://#####:@127.0.0.1:5432/python-dev')

conn = get_connection()
cur  = conn.cursor()
cur.execute("insert into exmaple (id, name) values('0005', 'test01')")
conn.commit()
cur.execute("select * from exmaple")

for row in cur:
  print(row)

cur.close()
conn.close()
