# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.backup = QtWidgets.QPushButton(Mod_Choose)
        self.backup.setGeometry(QtCore.QRect(140, 320, 75, 23))
        self.backup.setObjectName("backup")
        self.listWidget = QtWidgets.QListWidget(Mod_Choose)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 451, 251))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
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
        self.backup.setText(_translate("Mod_Choose", "復原"))
        self.Previous.setText(_translate("Mod_Choose", "上一步"))
