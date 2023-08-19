# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextBrowser, QTextEdit, QWidget,QLineEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(650, 550)
        self.questionContent = QTextBrowser(Form)
        self.questionContent.setObjectName(u"questionContent")
        self.questionContent.setGeometry(QRect(40, 40, 570, 300))
        self.answerInput = QLineEdit(Form)
        self.answerInput.setObjectName(u"answerInput")
        self.answerInput.setGeometry(QRect(40, 350, 120, 30))
        self.showAnswerLabel = QLabel(Form)
        self.showAnswerLabel.setObjectName(u"showAnswerLabel")
        self.showAnswerLabel.setGeometry(QRect(510, 350, 100, 30))
        self.submitBtn = QPushButton(Form)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(40, 390, 120, 30))
        self.nextBtn = QPushButton(Form)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setGeometry(QRect(490, 390, 120, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.showAnswerLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.submitBtn.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.nextBtn.setText(QCoreApplication.translate("Form", u"Next", None))
    # retranslateUi














