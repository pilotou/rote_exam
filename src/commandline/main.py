import os
import random
import argparse
import sqlite3
import time
from datetime import datetime

from Reader import read_question_from_txt
from Database import read_question_from_db,update_right_question,update_wrong_question


class DoExercercise:
    def __init__(self, questions, conn):
        self.questions = questions
        self.conn = conn

    def shuffle(self):
        random.shuffle(self.questions)

    def filter(self, type="单选题", source="all", shuffle=0):

        q_type = ["单选题","判断题","多选题","问答题"]

        if type in q_type:
            self.questions = [q for q in self.questions if q.type == type]
        else:
            raise Exception("type只能填单选题、判断题、多选题、问答题")

        if source != "all" and source in ["操作类","理论类"]:
            self.questions = [q for q in self.questions if q.source == source]

        elif source not in ["操作类","理论类","all"]:
            raise Exception("source只能填操作类、理论类")

        if shuffle:
            self.shuffle()


    def do_ex(self):
        os.system('cls')
        wrong_question = []
        cnt = 0
        for question in self.questions:
            if cnt % 3 == 0:
                os.system('cls')
            cnt += 1
            print(question.show())
            ans = input("你的答案是： >>>>>>>(  )<<<<<<").upper()
            if question.type=="判断题":
                if ans.upper() in ["1","T"]:
                    ans = "正确"
                elif ans.upper() in ["0","F"]:
                    ans = "错误"
            if ans == "EXIT":
                print("退出题库............")
                # 输出此次错误的题目
                with open("wrong_question.txt", "w", encoding="utf-8") as f:
                    for q in wrong_question:
                        f.write(q.note_question())
                break
            elif question.check(ans):
                print("正确\n")
                question.recent_answer = ans
                question.right_times += 1
                question.last_answer_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                update_right_question(
                    self.conn,
                    question.recent_answer,
                    question.right_times,
                    question.last_answer_date,
                    question.id
                )
            else:
                print(f"回答错误，正确答案为{question.answer}\n")
                question.recent_answer = ans
                question.last_wrong_answer = ans
                question.last_answer_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                question.wrong_times += 1
                update_wrong_question(
                    self.conn,
                    question.recent_answer,
                    question.wrong_times,
                    question.last_answer_date,
                    question.last_wrong_answer,
                    question.id
                )
                wrong_question.append(question)
            if cnt % 3 == 0:
                if input('.....回车键继续.....') == '':
                    continue


parser = argparse.ArgumentParser(description='argparse testing')
parser.add_argument('--type','-t',type=str, default="单选题")
parser.add_argument('--source','-S',type=str, default="all")
parser.add_argument('--shuffle','-s',type=int, default=0)
args = parser.parse_args()

# 从txt文件读取题目
# file_names = ["./files/新员工上岗题库-操作类（138题）.txt", "./files/新员工上岗题库-理论类（666题+35题简答）.txt"]
# questions = read_question_from_txt(file_names)

# 从数据库读取题目
conn = sqlite3.connect("question.db")
questions = read_question_from_db(conn)

de = DoExercercise(questions,conn)
de.filter(source=args.source,type=args.type,shuffle=args.shuffle)
de.do_ex()
