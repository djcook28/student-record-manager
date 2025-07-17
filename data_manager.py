import sqlite3

DATABASE = "school_master.db"

def add_student(name, mobile_number):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (student_name, mobile_number) VALUES (?, ?)",
                   (name, mobile_number))
    connection.commit()
    cursor.close()
    connection.close()

# write new enrollment record to the database
def enroll_student(student_id, course_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO student_enrollment (student_id, course_id) values (?, ?)",
                   (student_id, course_id))
    # commit the draft change to the database
    connection.commit()
    cursor.close()
    connection.close()

def update_enrollment(student_name, course_id, enrollment_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    student_id = cursor.execute(f"SELECT student_id FROM students WHERE student_name = ?", (student_name,)).fetchone()[0]
    cursor.execute(f"UPDATE student_enrollment SET student_id = ?, course_id = ? WHERE id = ?",
                   (student_id, course_id, enrollment_id))
    # commit the draft change to the database
    connection.commit()
    cursor.close()
    connection.close()

# loads master list of courses from database
def load_courses():
    connection = sqlite3.connect(DATABASE)
    results = connection.execute("SELECT course_id FROM courses")
    # results is a database object that consists of a list of tuples
    results = list(results)
    connection.close()

    # loop through the list of tuples to create just a list
    courses = []
    for tuple in results:
        for item in tuple:
            courses.append(item)
    return courses

    # loads master list of student from database
def load_students():
    connection = sqlite3.connect(DATABASE)
    results = connection.execute("SELECT student_id, student_name FROM students")
    # results is a database object that consists of a list of tuples
    results = list(results)
    connection.close()

    # loop through the list of tuples to create just a list
    return results

def load_main_table(name=""):
    load_text = ("SELECT a.id, a.student_id, b.student_name, a.course_id, c.course_title, b.mobile_number "
                 "FROM student_enrollment a "
                 "LEFT JOIN students b on a.student_id = b.student_id "
                 "LEFT JOIN courses c on a.course_id = c.course_id")
    # loads current student enrollment records from the database
    connection = sqlite3.connect(DATABASE)
    if name == "":
        results = connection.execute(load_text)
    else:
        name = (name,)
        results = connection.execute(f"{load_text} WHERE b.student_name = (?)", name)
    if results:
        results = list(results)
        connection.close()
        # loop through the list of tuples to create just a list
        return results
    else:
        connection.close()
        return None