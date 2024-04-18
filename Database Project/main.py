import psycopg2

conn = psycopg2.connect(database="python_demo",
                        user="postgres",
                        host='localhost',
                        password="ansahmd123",
                        port=5432)

print("Database connected")

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
# cur.execute("""CREATE TABLE student(
#             student_id SERIAL PRIMARY KEY,
#             student_name VARCHAR (50) NOT NULL,
#             percentage int NOT NULL);
#             """)


# cur.execute(
#     "INSERT INTO student(student_id, student_name, percentage) VALUES(1,'Anas Ahmad',100)")
# cur.execute(
#     "INSERT INTO student(student_id, student_name, percentage) VALUES(2,'Ammar Ahmad',100)")
# cur.execute(
#     "INSERT INTO student(student_id, student_name, percentage) VALUES(3,'Jawwad Ahmad',100)")
# cur.execute(
#     "INSERT INTO student(student_id, student_name, percentage) VALUES(4,'Zimad Ahmad',100)")
# cur.execute(
#     "INSERT INTO student(student_id, student_name, percentage) VALUES(5,'Saad Ahmad',100)")

cur.execute("select * from student where percentage = 100")
rows = cur.fetchall()

names = []
# print(type(rows))
for row in rows:
    names.append(row[1])

print(names)

conn.commit()
cur.close()
conn.close()
print("DB connection closed")
