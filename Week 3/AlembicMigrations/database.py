import psycopg2

from sqlalchemy import create_engine
# conn = psycopg2.connect(
#     host="localhost",
#     database="myProject",
#     user="postgres",
#     password="admin@123",
#     port="5432"
# )

# cur = conn.cursor()

DATABASE_URL = (
    "postgresql://postgres:admin%%40123@localhost:5432/myProject"
)



engine = create_engine(DATABASE_URL)

