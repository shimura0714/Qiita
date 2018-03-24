import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'test'
}

con = mysql.connector.connect(**config)
cursor = con.cursor(buffered=True)

stmt = "select * from test"
cursor.execute(stmt)
results = cursor.fetchall()
for result in results:
  print(result)

sql = "insert into test (name) values (%s)"

data = {
  ("001"),
  ("002"),
  ("003"),
  ("004")
}
cursor.execute(sql, data, True)
con.commit()
cursor.close()
con.close()