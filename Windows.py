from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Position_Check(object):
    def setupUi(self, Position_Check):
        Position_Check.setObjectName("Position_Check")
        Position_Check.resize(500, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Position_Check.sizePolicy().hasHeightForWidth())
        Position_Check.setSizePolicy(sizePolicy)
        Position_Check.setMaximumSize(QtCore.QSize(500, 360))
        self.Next = QtWidgets.QPushButton(Position_Check)
        self.Next.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.Next.setObjectName("Next")
        self.Cancel = QtWidgets.QPushButton(Position_Check)
        self.Cancel.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.Cancel.setObjectName("Cancel")
        self.Position = QtWidgets.QLineEdit(Position_Check)
        self.Position.setGeometry(QtCore.QRect(40, 230, 401, 20))
        self.Position.setObjectName("Position")
        self.Text = QtWidgets.QLabel(Position_Check)
        self.Text.setGeometry(QtCore.QRect(40, 30, 381, 180))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.Text.setFont(font)
        self.Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Text.setObjectName("Text")
        self.Change_Position = QtWidgets.QPushButton(Position_Check)
        self.Change_Position.setGeometry(QtCore.QRect(450, 230, 20, 20))
        self.Change_Position.setObjectName("Change_Position")

        self.retranslateUi(Position_Check)
        QtCore.QMetaObject.connectSlotsByName(Position_Check)

    def retranslateUi(self, Position_Check):
        _translate = QtCore.QCoreApplication.translate
        self.Change_Position.setText(_translate("Position_Check", "..."))
        Position_Check.setWindowTitle(_translate("Position_Check", "戰艦世界 指揮官語音修改程式"))
        self.Next.setText(_translate("Position_Check", "下一步"))
        self.Cancel.setText(_translate("Position_Check", "取消"))
        self.Position.setText(_translate("Position_Check", "C:\\Games\\World_of_Warships"))
        self.Text.setText(_translate("Position_Check", "此為修改指揮官語音程式，\n"
        "詳情請閱讀巴哈文章。\n"
        "再次提醒修改前請關閉遊戲。\n"
        "\n"
        "在此請確認資料夾位置是否戰艦世界資料夾，\n"
        "請注意資料夾名稱應為\"World_of_Warships\"\n"
        "預設是\"C:\\Games\\World_of_Warships\"\n"
        ""))
        
class Ui_Mod_Choose(object):
    def setupUi(self, Mod_Choose):
        Mod_Choose.setObjectName("Mod_Choose")
        Mod_Choose.resize(500, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Mod_Choose.sizePolicy().hasHeightForWidth())
        Mod_Choose.setSizePolicy(sizePolicy)
        Mod_Choose.setMaximumSize(QtCore.QSize(500, 360))
        self.Next = QtWidgets.QPushButton(Mod_Choose)
        self.Next.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.Next.setObjectName("Next")
        self.Cancel = QtWidgets.QPushButton(Mod_Choose)
        self.Cancel.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.Cancel.setObjectName("Cancel")
        self.Text = QtWidgets.QLabel(Mod_Choose)
        self.Text.setGeometry(QtCore.QRect(30, 20, 381, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.Text.setFont(font)
        self.Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Text.setObjectName("Text")
        self.recover = QtWidgets.QPushButton(Mod_Choose)
        self.recover.setGeometry(QtCore.QRect(140, 320, 75, 23))
        self.recover.setObjectName("recover")
        font.setPointSize(10)
        font.setFamily("Consolas")
        self.listWidget = QtWidgets.QListWidget(Mod_Choose)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 451, 251))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setFont(font)
        self.Previous = QtWidgets.QPushButton(Mod_Choose)
        self.Previous.setGeometry(QtCore.QRect(230, 320, 75, 23))
        self.Previous.setObjectName("Previous")

        self.retranslateUi(Mod_Choose)
        QtCore.QMetaObject.connectSlotsByName(Mod_Choose)

    def retranslateUi(self, Mod_Choose):
        _translate = QtCore.QCoreApplication.translate
        Mod_Choose.setWindowTitle(_translate("Mod_Choose", "戰艦世界 指揮官語音修改程式"))
        self.Next.setText(_translate("Mod_Choose", "下一步"))
        self.Cancel.setText(_translate("Mod_Choose", "取消"))
        self.Text.setText(_translate("Mod_Choose", "請選擇語音"))
        self.recover.setText(_translate("Mod_Choose", "復原"))
        self.Previous.setText(_translate("Mod_Choose", "上一步"))


class Ui_Finish(object):
    def setupUi(self, Finish:QtWidgets.QWidget):
        Finish.setObjectName("Finish")
        Finish.resize(500, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Finish.sizePolicy().hasHeightForWidth())
        Finish.setSizePolicy(sizePolicy)
        Finish.setMaximumSize(QtCore.QSize(500, 360))
        self.Next = QtWidgets.QPushButton(Finish)
        self.Next.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.Next.setObjectName("Next")
        self.label = QtWidgets.QLabel(Finish)
        self.label.setGeometry(QtCore.QRect(30, 30, 451, 200))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.retranslateUi(Finish)
        QtCore.QMetaObject.connectSlotsByName(Finish)

    def retranslateUi(self, Finish:QtWidgets.QWidget):
        _translate = QtCore.QCoreApplication.translate
        Finish.setWindowTitle(_translate("Finish", "戰艦世界 指揮官語音修改程式"))
        self.Next.setText(_translate("Finish", "完成"))
        self.label.setText(_translate("Finish", "修改完成，\n"
            "請注意不要在遊戲中開啟設定畫面，\n"
            "否則需要再次重新修改，\n"
            "有任何問題請在巴哈回報。"))

# class Ui_ErrorBox(object):
#     def setupui(self,Errorbox:QtWidgets.QMessageBox):
#         Errorbox.setObjectName("Errorbox")
#         Errorbox.resize(500, 100)
#         Errorbox.setFixedSize(500,100)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(Errorbox.sizePolicy().hasHeightForWidth())
#         Errorbox.setSizePolicy(sizePolicy)
#         Errorbox.setMaximumSize(QtCore.QSize(500, 100))
#         self.done = QtWidgets.QPushButton(Errorbox)
#         self.done.setGeometry(QtCore.QRect(50, 50, 75, 23))
#         self.done.setObjectName("done")

#         self.retranslateUi(Errorbox)
#         QtCore.QMetaObject.connectSlotsByName(Errorbox)

#     def retranslateUi(self, Errorbox:QtWidgets.QWidget):
#         _translate = QtCore.QCoreApplication.translate
#         Errorbox.setWindowTitle(_translate("Errorbox", "戰艦世界 指揮官語音修改程式"))
#         self.Next.setText(_translate("Errorbox", "完成"))
        