import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="myProject",
    user="postgres",
    password="admin@123",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT version();")
print(cur.fetchone())