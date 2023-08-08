import sqlite3

from typing import List

from Question import Question


#conn = sqlite3.connect("question.db")
from Reader import read_question_from_txt


def create_table(conn):
    cur = conn.cursor()
    sql = """
    create table IF NOT EXISTS question
    ( 
    id integer PRIMARY KEY,
    q_id integer,
    question text,
    answer text,
    choice text,
    choice_num integer,
    type varchar(50),
    difficulty varchar(20),
    source varchar(20),
    recent_answer varchar(20),
    wrong_times integer,
    right_times integer,
    last_wrong_date varchar(50),
    last_wrong_answer text
    )
    """
    cur.execute(sql)
    conn.commit()

def test_insert():
    conn = sqlite3.connect("question.db")
    file_names = ["./files/新员工上岗题库-操作类（138题）.txt", "./files/新员工上岗题库-理论类（666题+35题简答）.txt"]
    questions = read_question_from_txt(file_names)
    insert_question(questions,conn)

def insert_question(questions: List[Question],conn):
    cur = conn.cursor()
    for q in questions:

        insertQuery = """INSERT INTO question
            VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?,?);"""
        # insert the data into table
        cur.execute(insertQuery, (None, q.q_id,q.question,q.answer,q.choice,q.choice_num,q.type,q.difficulty,q.source,q.recent_answer,
                                  q.wrong_times,q.right_times,q.last_answer_date,q.last_wrong_answer))

    conn.commit()


def read_question_from_db(conn):
    cursor = conn.cursor()
    cursor.execute("select * from question")
    questions = []
    for row in cursor:
        questions.append(Question(*row))
    return questions


def update_right_question(conn,recent_answer,right_times,last_answer_date,id):
    cursor = conn.cursor()
    cursor.execute("update question set recent_answer=?,right_times=?,last_answer_date=? where id=?",(
        recent_answer,
        right_times,
        last_answer_date,
        id
    ))
    conn.commit()


def update_wrong_question(conn,recent_answer,wrong_times,last_answer_date,last_wrong_answer,id):
    cursor = conn.cursor()
    cursor.execute("update question set recent_answer=?,wrong_times=?,last_answer_date=? , last_wrong_answer=? where id=?",(
        recent_answer,
        wrong_times,
        last_answer_date,
        last_wrong_answer,
        id
    ))
    conn.commit()

