import re



def parse_txt(contents):
    regex = r'"([^"]*)"'
    return re.findall(regex, contents)

def deal_singlechoice(question):
    """
    处理选择题字符串
    """
    return {
        "question_temp": re.search(r"\..*?[\s\S]+?A[\.、]",question).group()[1:-3].replace("\n",""),
        "choice": re.search("A[\.、].*[\s\S]+答案",question).group().split("\n答案")[0],
        "choice_num": 4,
        "answer": re.search("答案.*?\n",question).group().strip()[-1],
        "difficulty": 1 #re.search("难度[:：]\d",question).group().split("难度[:：]")[-1].strip()
    }

def deal_multichoice(question):
    """
    处理选择题字符串
    """
    return {
        "question_temp": re.search(r"\..*?[\s\S]+?A[\.、]", question).group()[1:-3].replace("\n", ""),
        "choice": re.search("A[\.、].*[\s\S]+答案", question).group().split("\n答案")[0],
        "choice_num": 4,
        "answer": re.search("答案.*?\n", question).group()[3:].strip(),
        "difficulty": 1#re.search("难度:\d", question).group().split("难度:")[-1].strip()
    }

def deal_truefalse(question):
    """
    处理判断题
    """
    return{
        "question_temp": re.search(r"\..*?[\s\S]+?答案",question).group()[1:].split("\n答案")[0],
        "choice": "",
        "choice_num": 0,
        "answer": re.search(r"答案[:：].*?\n",question).group()[3:].strip(),
        "difficulty": 1#re.search("难度[:：]\d",question).group().split("难度[:：]")[-1].strip()
    }

def deal_shortanswer(question):
    """
    处理简答题
    pass
    """
    return{
        "question_temp": "",
        "choice": "",
        "choice_num": 0,
        "answer": "",
        "difficulty": "0"
    }