# Student Database Application

```
Abdullah Mostafa
101008311
COMP 3005 Assignment 3.1
March 18, 2024
```

## Setup

You need the **psycopg** library installed to interface with a Postgres database. You can install this using:

```bash
pip install psycopg 
```

**To configure the database connection, go to line 121 in students.py**

```python
db = StudentDatabase(host='localhost', db='a3_1_students', user='', password='')
```

## Running

You can run the program using this command:

```bash
python3 students.py
```

Once running the program you'll be shown all records along with options to modify the records:

**[1]** Adds a new student record, following the input prompts for the first name, last name and email.

**[2]** Updates a student's email when given a student ID along with a new email, following the input prompts.

**[3]** Deletes a record when given a student ID following the input prompts.

**[x]** Exits the program.