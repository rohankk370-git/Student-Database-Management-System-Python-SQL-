import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Asdf900@",
    database="student_db"
)

cursor = conn.cursor()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    query = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
    values = (name, age, course, marks)

    cursor.execute(query, values)
    conn.commit()
    print("Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def delete_student():
    sid = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
    conn.commit()

# add_student()
# view_students()
# delete_student()

while True:
    print("\n1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        break
