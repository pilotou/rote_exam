import re
from Question import Question
from Dealer import deal_singlechoice,deal_multichoice,deal_truefalse,deal_shortanswer,parse_txt


file_names = ["./新员工上岗题库-操作类（138题）.txt", "./新员工上岗题库-理论类（666题+35题简答）.txt"]
def read_question_from_txt(file_names):
    question_list = {}
    for file_name in file_names:
        with open(file_name, 'r', encoding='UTF-8') as f:
            q_list_temp = parse_txt(f.read())
            if "操作类" in file_name:
                question_list["操作类"] = q_list_temp
            elif "理论类" in file_name:
                question_list["理论类"] = q_list_temp
    questions = []
    for source, all_q in question_list.items():
        for question in all_q:
            # 匹配题号
            q_id_re = re.search(r"\d+\.", question)
            if q_id_re:
                q_id = q_id_re.group()[:-1]
            else:
                print(f"题号解析出错，题目为：\n{question}")
                continue

            # 题型处理
            q_type_re = re.search(r"题型.*?\n", question)
            if q_type_re:
                q_type = q_type_re.group()[3:].strip()
            else:
                print(f"题型解析出错，题目为：\n{question}")
                continue

            cd = {}
            try:
                # 选择题
                if q_type == "单选题":
                    cd = deal_singlechoice(question)
                # 判断题
                elif q_type == "判断题":
                    cd = deal_truefalse(question)
                # 多选题
                elif q_type == "多选题":
                    cd = deal_multichoice(question)
                # 简答题
                elif q_type == "问答题":
                    cd = deal_shortanswer(question)
                else:
                    print(f"{q_id}.题未归类")
                    continue

            except Exception:
                print(f"{source} {q_type}第{q_id}题txt解析出现错误,题型:{q_type},题目为:\n{question}\n cd为：{cd}")

            questions.append(Question(
                id=None,
                q_id=q_id,
                question=cd['question_temp'],
                answer=cd['answer'],
                choice=cd['choice'],
                choice_num=cd['choice_num'],
                q_type=q_type,
                difficulty=cd['difficulty'],
                source=source
            ))
    return questions

# TODO: read question from db
def read_question_from_db():
    pass