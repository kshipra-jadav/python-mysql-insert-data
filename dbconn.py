import mysql.connector
import pandas as pd

def start(filename):
    df = pd.read_excel(filename)

    from datetime import datetime

    now = datetime.now()

    # Format 2022-09-04 01:15:00
    curr_dt = now.strftime("%Y-%m-%d %H:%M:%S")

    curr_dt # this is in mysql datetime format

    df['dt'] = curr_dt

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Student_details"
    )

    cursor = db.cursor()

    student_stmt = (
        "INSERT INTO Students (id, prn, student_fname, student_mname, student_lname, student_email, student_batch, created_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    student_det = list(df.itertuples(index=False, name=None))

    cursor.executemany(student_stmt, student_det)

    db.commit()