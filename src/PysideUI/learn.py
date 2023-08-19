import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class UI_MainWindow(object):
    def setup_ui(self,parent):
        '''parent: 一般由 main.py文件中MainWindow类的实例self变量作为父类，目的是UI_MainWindow实例做mai文件中的UI界面。
                    通常，在main.py，这样调用setup_ui方法
                            # SETUP MAIN WINDOW
                            self.ui = UI_MainWindow()
                            self.ui.setup_ui(self)
        '''
        if not parent.objectName():  # 此判断，经测试，一定会进入
            parent.setObjectName("MainWindow")  # TODO(wangjh-xm): 暂时不清楚setObjectName的作用效果。
            # print('test')

        # SET INITIAL PARAMETERS
        # ///////////////////////////////////////////////////////////////
        parent.resize(1200, 720)  # 重新设启动时的界面大小
        parent.setMinimumSize(960, 540)# 设置手动调整的最小尺寸

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MANU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        # self.left_menu.setMaximumHeight(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)


        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # content layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # Add to content layout
        self.content_layout.addWidget(self.top_bar)




        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL
        parent.setCentralWidget(self.central_frame)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("learning")
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.show()



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())

