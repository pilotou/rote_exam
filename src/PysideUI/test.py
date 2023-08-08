import sys
from PySide6 import QtGui,QtCore

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
    QVBoxLayout, QSizePolicy


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My PySide App')
        self.resize(600, 450)
        question_area = QTextBrowser()
        question_area.setEnabled(False)
        question_area.resize(380,200)
        answer_area = QTextEdit()
        answer_area.resize(10, 30)
        right_ans_area = QLabel()
        submit_btn = QPushButton("提交")
        next_question_btn = QPushButton("下一题")

        vlayout = QVBoxLayout()
        vlayout.addWidget(question_area)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(answer_area, 1, 0)
        grid.addWidget(right_ans_area, 1, 1)
        grid.addWidget(submit_btn, 2, 0)
        grid.addWidget(next_question_btn, 2, 1)
    
        sp = answer_area.sizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Minimum)
        answer_area.setSizePolicy(sp)

        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 1)

        vlayout.addLayout(grid)
        self.setLayout(vlayout)



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()