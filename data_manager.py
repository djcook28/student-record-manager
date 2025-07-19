import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE = "school"
dbhost = "localhost"
dbuser = "root"
dbpassword = os.getenv("DATABASEPASS")

# adds a student to the student master.  Once a student is added they can be enrolled in courses
def add_student(name, mobile_number):
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (student_name, mobile_number) VALUES (%s, %s)",
                   (name, mobile_number))
    connection.commit()
    cursor.close()
    connection.close()

# write new enrollment record to the database
def enroll_student(student_id, course_id):
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO student_enrollment (student_id, course_id) values (%s, %s)",
                   (student_id, course_id))
    # commit the draft change to the database
    connection.commit()
    cursor.close()
    connection.close()

# updates a student enrollment record
def update_enrollment(student_name, course_id, enrollment_id):
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"SELECT student_id FROM students WHERE student_name = %s", (student_name,))
    student_id = cursor.fetchone()[0]
    cursor.execute(f"UPDATE student_enrollment SET student_id = %s, course_id = %s WHERE id = %s",
                   (student_id, course_id, enrollment_id))
    # commit the draft change to the database
    connection.commit()
    cursor.close()
    connection.close()

# deletes enrollment record from the database
def disenroll_student(enrollment_id):
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM student_enrollment WHERE id = %s", (enrollment_id,))
    connection.commit()
    cursor.close()
    connection.close()

# loads master list of courses from database
def load_courses():
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT course_id FROM courses")
    results = cursor.fetchall()
    # results is a database object that consists of a list of tuples
    results = list(results)
    cursor.close()
    connection.close()

    # loop through the list of tuples to create just a list
    courses = []
    for tuple in results:
        for item in tuple:
            courses.append(item)
    return courses

    # loads master list of student from database
def load_students():
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT student_id, student_name FROM students")
    results = cursor.fetchall()
    # results is a database object that consists of a list of tuples
    results = list(results)
    cursor.close()
    connection.close()

    # loop through the list of tuples to create just a list
    return results

def load_main_table(name=""):
    load_text = ("SELECT a.id, a.student_id, b.student_name, a.course_id, c.course_title, b.mobile_number "
                 "FROM student_enrollment a "
                 "LEFT JOIN students b on a.student_id = b.student_id "
                 "LEFT JOIN courses c on TRIM(LOWER(a.course_id)) = TRIM(LOWER(c.course_id))")
    # loads current student enrollment records from the database
    connection = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, database=DATABASE)
    cursor = connection.cursor()
    if name == "":
        cursor.execute(load_text)
        results = cursor.fetchall()
    else:
        name = (name,)
        cursor.execute(f"{load_text} WHERE b.student_name = (%s)", name)
        results = cursor.fetchall()
    if results:
        results = list(results)
        cursor.close()
        connection.close()
        # loop through the list of tuples to create just a list
        return results
    else:
        cursor.close()
        connection.close()
        return None