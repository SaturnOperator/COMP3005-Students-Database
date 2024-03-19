# Abdullah Mostafa
# 101008311
# COMP 3005 Assignment 3.1
# March 18, 2024

import psycopg
import datetime
import os

class StudentDatabase:

    def __init__(self, host, db, user, password):
        self.host = host
        self.database = db
        self.user = user
        self.password = password
        self.last = False
        self.lastMsg = ""

    def connect_db(self):
        # Database credentials and address
        url = f"host={self.host} dbname={self.database}"

        # If username/password needed add them to the url
        if(self.user != ""):
            url += f" user={self.user}"
        if(self.password != ""):
            url += f" password={self.password}"

        try:
            return psycopg.connect(url)
        except Exception as error:
            print(error)
            return None


    def getAllStudents(self):
        conn = self.connect_db() # Connect to db
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM students') # Run query
                    records = cur.fetchall() # Get results
                    for row in records: # Print each line
                        print(row)
            except Exception as error:
                print(error)
            finally:
                conn.close()
                return True
        return False

    def addStudent(self, first, last, email):
        currentDate = datetime.date.today().isoformat() # Get current date
        conn = self.connect_db() # Connect to db
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute( # Insert new student's data into the db
                        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", 
                        (first, last, email, currentDate)
                    )
                    conn.commit() # Make changes
                    self.last = True
                    self.lastMsg = f"Rows affected (added): {cur.rowcount}"
                    print(lastMsg)
            except Exception as error:
                print(error)
            finally:
                conn.close()
                return True
        return False

    def updateStudentEmail(self, studentId, email):
        conn = self.connect_db() # Connect to db
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute( # Update email for the given student ID
                        "UPDATE students SET email = %s WHERE student_id = %s",
                        (email, studentId)
                    )
                    conn.commit() # Make changes
                    self.last = True
                    self.lastMsg = f"Rows affected (updated): {cur.rowcount}"
                    print(self.lastMsg)
            except Exception as error:
                print(error)
            finally:
                conn.close()
                return True
        return False

    def deleteStudent(self, studentId):
        conn = self.connect_db() # Connect to db
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute( # Delete row of matching student ID
                        "DELETE FROM students WHERE student_id = %s",
                        (studentId,)
                    )
                    conn.commit() # Make changes

                    self.last = True
                    self.lastMsg = f"Rows affected (deleted): {cur.rowcount}"
                    print(self.lastMsg)
            except Exception as error:
                print(error)
            finally:
                conn.close()
                return True
        return False

    def printLastMsg(self):
        if(self.last):
            print(self.lastMsg)
            self.last = False

def main():
    db = StudentDatabase(host='localhost', db='a3_1_students', user='', password='')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal

        db.getAllStudents()

        print()
        db.printLastMsg()

        option = input("\nChoose an operation [1: Add, 2: Update, 3: Delete, x: Exit]: ")

        if(option == 'x' or option == 'X'):
            return

        if option == "1":
            print("\n[ Adding new student to database ]")
            first = input("Student's first name: ")
            last = input("Student's last name: ")
            email = input("Student's email: ")
            db.addStudent(first, last, email)


        if option == "2":
            print("\n[ Updating student's email ]")
            studentId = input("Student's ID: ")
            email = input("New email: ")
            db.updateStudentEmail(studentId, email)

        if option == "3":
            print("\n[ Deleting student record ]")
            studentId = input("Student's ID: ")
            db.deleteStudent(studentId)

if __name__ == '__main__':
    main()