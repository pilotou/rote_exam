import sys
from PySide6 import QtGui,QtCore
from PySide6.QtGui import QAction

# app = QtWidgets.QApplication(sys.argv)
#
# wid = QtWidgets.QWidget()
# wid.resize(250, 150)
# wid.setWindowTitle('Simple')
# wid.show()
#
# sys.exit(app.exec_())
from PySide6.QtWidgets import QLabel, QWidget, QComboBox, QPushButton, QGridLayout, QTextBrowser, QTextEdit, \
    QApplication, \
    QVBoxLayout, QSizePolicy,QFrame,QFormLayout,QMainWindow,QToolBar
from main_ui import Ui_Form
from database.Database import get_question_from_db


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nerding Exam App')
        self.resize(600, 450)
        self.question_area = QTextBrowser()
        self.question_area.setEnabled(False)
        self.question_area.setGeometry(5,5,300,200)

        self.answer_area = QTextEdit()
        self.answer_area.setGeometry(5,210,60,30)

        self.right_ans_area = QLabel()
        self.right_ans_area.setGeometry(70,210,60,30)

        self.submit_btn = QPushButton("提交")
        self.submit_btn.setGeometry(5,245,40,30)
        self.next_question_btn = QPushButton("下一题")
        self.next_question_btn.setGeometry(5,410,40,30)

        vlayout = QFormLayout()
        vlayout.addWidget(self.question_area)
        vlayout.addWidget(self.answer_area)
        vlayout.addWidget(self.right_ans_area)
        vlayout.addWidget(self.submit_btn)
        vlayout.addWidget(self.next_question_btn)
        #
        # # frame = QFrame()
        # # frame.setGeometry()
        #
        # grid = QGridLayout()
        # # grid.setSpacing(10)
        # grid.addWidget(answer_area, 1, 0)
        # grid.addWidget(right_ans_area, 1, 1)
        # grid.addWidget(submit_btn, 2, 0)
        # grid.addWidget(next_question_btn, 2, 1)
        #
        # sp = answer_area.sizePolicy()
        # sp.setVerticalPolicy(QSizePolicy.Minimum)
        # answer_area.setSizePolicy(sp)
        #
        # grid.setRowStretch(0, 1)
        # grid.setRowStretch(1, 1)
        #
        # vlayout.addLayout(grid)
        self.setLayout(vlayout)

class Window1(QMainWindow):
    def __init__(self):
        super(Window1,self).__init__()
        self.ui = Ui_Form()
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        self.addAction(button_action)
        self.ui.setupUi(self)
        # self.ui.showAnswerLabel.setSizePolicy(QSizePolicy.)
        self.ui.submitBtn.clicked.connect(self.submit)
        self.ui.nextBtn.clicked.connect(self.next_question)
        self.ui.answerInput.returnPressed.connect(self.submit)
        # self.ui.questionContent.setFont("15")
        self.questions = get_question_from_db()
        self.current_question_id = 0
        self.ui.questionContent.setText(self.questions[self.current_question_id].show())

    def onMyToolBarButtonClick(self, s):
        print("click", s)


    def submit(self):
        answer = self.ui.answerInput.text()
        question = self.questions[self.current_question_id]
        correct_answer = question.answer
        self.ui.showAnswerLabel.clear()
        if answer.upper() == correct_answer:
            self.ui.showAnswerLabel.setText("回答正确")
        else:
            self.ui.showAnswerLabel.setText("回答错误")

    def next_question(self):
        self.current_question_id += 1
        self.ui.questionContent.setText(self.questions[self.current_question_id].show())
        self.clear_input()

    def clear_input(self):
        self.ui.answerInput.clear()
        self.ui.showAnswerLabel.clear()



app = QApplication(sys.argv)
window = Window1()
window.show()
app.exec()

