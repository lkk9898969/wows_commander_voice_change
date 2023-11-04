import Windows,winreg,icon
from base64 import b64decode
from PyQt5 import QtCore,QtGui,QtWidgets
from soundmodcode import mod
from os.path import exists
import xml.etree.ElementTree as et
xmlfile="\\user_preferences{}.xml"
paths="C:\\Games\\World_of_Warships"
error=False

class Position_Check_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Windows.Ui_Position_Check()
        self.ui.setupUi(self)
        # self.setup

class Mod_Choose_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Windows.Ui_Mod_Choose()
        self.ui.setupUi(self)

class Finish_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Windows.Ui_Finish()
        self.ui.setupUi(self)

class MainWindow_controller(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.Position_Check_controller = Position_Check_ui()
        self.addWidget(self.Position_Check_controller)
        self.Mod_Choose_controller = Mod_Choose_ui()
        self.addWidget(self.Mod_Choose_controller)
        self.Finish_controller = Finish_ui()
        self.addWidget(self.Finish_controller)
        self.setup_control()
    
    def setup_control(self):
        pm = QtGui.QPixmap()
        pm.loadFromData(b64decode(icon.img))
        self.i = QtGui.QIcon()
        self.i.addPixmap(pm)
        self.setWindowIcon(self.i)
        global paths,xmlfile
        self.Position_Check_controller.ui.Next.clicked.connect(self.page1done)
        self.Position_Check_controller.ui.Cancel.clicked.connect(self.close)
        self.Mod_Choose_controller.ui.Next.clicked.connect(self.page2done)
        self.Mod_Choose_controller.ui.Cancel.clicked.connect(self.close)
        self.Mod_Choose_controller.ui.Previous.clicked.connect(lambda: self.setCurrentIndex(0))
        self.Mod_Choose_controller.ui.recover.clicked.connect(self.recover)
        self.Position_Check_controller.ui.Change_Position.clicked.connect(self.change_postition)
        self.Finish_controller.ui.Next.clicked.connect(lambda: sys.exit())
        # self.Mod_Choose_controller.ui.recover.installEventFilter(self)
        self.Mod_Choose_controller.ui.recover.setToolTip('復原上一次設定')
        self.setFixedSize(500,360)
        self.setWindowTitle("戰艦世界 指揮官語音修改程式")
        self.init()
        if not exists(paths+xmlfile.format("_backup")):
            self.Mod_Choose_controller.ui.recover.deleteLater()

    def init(self):
        
        # self.Position_Check_controller.setWindowIcon(i)
        # self.Mod_Choose_controller.setWindowIcon(i)
        self.selected=False
        item=mod.items()
        item=list(item)
        item.sort(key=lambda items:items[0])
        for i in item:
            self.Mod_Choose_controller.ui.listWidget.addItem(i[0])
        # self.Mod_Choose_controller.ui.listWidget.setCurrentItem(self.Mod_Choose_controller.ui.listWidget.findItems("一般",QtCore.Qt.MatchFlag.MatchContains)[0])
        self.Mod_Choose_controller.ui.listWidget.currentItemChanged.connect(self.__selectchange)
        self.loadpath()

    def __selectchange(self):
        self.selected=True
    
    def closeEvent(self, a0: QtGui.QCloseEvent):
        if(self.cancelmsgbox("尚未修改完成，確定要取消修改?")):
            return super().closeEvent(a0)
        a0.ignore()
    # def eventFilter(self, a0: QtCore.QObject, a1):
    #     if a1.type()==QtCore.QEvent.HoverEnter:
    #         QtWidgets.QToolTip.showText(QtGui.QCursor.pos(),'Test',self.Mod_Choose_controller)
    #     if a1.type()==QtCore.QEvent.HoverLeave:
    #         QtWidgets.QToolTip.hideText()
    #     return super().eventFilter(a0, a1)

    def errormsgbox(self,Text):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        font = QtGui.QFont()
        font.setPointSize(10)
        msg.setWindowIcon(self.i)
        msg.setFont(font)
        msg.setText(Text)
        msg.setWindowTitle("錯誤")
        msg.addButton("確定",QtWidgets.QMessageBox.ButtonRole.RejectRole)
        msg.exec_()
    
    def infosound(self):
        sound=QtWidgets.QMessageBox()
        sound.setIcon(QtWidgets.QMessageBox.Warning)
        sound.setWindowFlag(QtCore.Qt.WindowStaysOnBottomHint)
        sound.show()
        sound.close()

    def cancelmsgbox(self,Text):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText(Text)
        msg.setWindowTitle("取消")
        msg.setWindowIcon(self.i)
        cancel=msg.addButton("確定",QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        msg.addButton("取消",QtWidgets.QMessageBox.ButtonRole.RejectRole)
        self.infosound()
        msg.exec_()
        if msg.clickedButton()==cancel:
            return True
        return False

    def infomsgbox(self,Title,Text):
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(Text)
        msg.setWindowIcon(self.i)
        msg.setWindowTitle(Title)
        msg.addButton("確定",QtWidgets.QMessageBox.ButtonRole.AcceptRole)
        msg.exec_()

    def loadpath(self):
        software=winreg.CreateKey(winreg.HKEY_CURRENT_USER,"SOFTWARE")
        wargaming=winreg.CreateKey(software,"Wargaming.net")
        software.Close()
        cheng=winreg.CreateKey(wargaming,"cheng")
        wargaming.Close()
        try:
            position=winreg.EnumValue(cheng,0)[1]
            global paths
            paths=position
        except:
            winreg.SetValueEx(cheng,"app_folder",0,winreg.REG_SZ,'C:\\Games\\World_of_Warships')
        cheng.Close()
    
    def savepath(self):
        global paths
        software=winreg.CreateKey(winreg.HKEY_CURRENT_USER,"SOFTWARE")
        wargaming=winreg.CreateKey(software,"Wargaming.net")
        software.Close()
        cheng=winreg.CreateKey(wargaming,"cheng")
        wargaming.Close()
        winreg.SetValueEx(cheng,"app_folder",0,winreg.REG_SZ,paths)
        cheng.Close()

    def backup(self):
        global paths,xmlfile
        with open(paths+xmlfile.format(""),'r',encoding='utf-8') as f:
            content=f.read()
        with open(paths+xmlfile.format("_backup"),'w',encoding='utf-8') as f:
            f.write(content)

    def change_postition(self):
        postition=QtWidgets.QFileDialog.getExistingDirectory(self,'選擇資料夾',paths,QtWidgets.QFileDialog.Option.ShowDirsOnly | QtWidgets.QFileDialog.Option.DontResolveSymlinks)
        if postition != "":
            postition=postition.replace("/","\\")
            self.Position_Check_controller.ui.Position.setText(postition)
    
    def recover(self):
        global paths,xmlfile
        with open(paths+xmlfile.format("_backup"),'r',encoding='utf-8') as f:
            content=f.read()
        with open(paths+xmlfile.format(""),'w',encoding='utf-8') as f:
            f.write(content)
        self.infomsgbox("復原","復原完成")

    def page1done(self):
        postition=self.Position_Check_controller.ui.Position.text()
        if exists(postition+xmlfile.format("")):
            global paths
            paths=postition
            self.savepath()
            self.setCurrentIndex(1)
        else:
            self.errormsgbox("未能在該資料夾找到{}".format(xmlfile[1:].format("")))

    def page2done(self):
        if(self.selected):
            choice=self.Mod_Choose_controller.ui.listWidget.currentItem().text()
            self.mod=mod[choice]
            error=self.mod_change()
            if(error):
                sys.exit()
            else:
                self.infomsgbox("完成","修改成功")
                self.setCurrentIndex(2)
        else:
            self.errormsgbox("請選擇語音")

    def mod_change(self):
        voice_mod=True
        global paths
        with open(paths+xmlfile.format(""),'r',encoding='utf-8') as f:
            global error
            text = f.read()
            pos=text.find("voice_mod>")
            if pos == -1:
                pos=text.find("sound>")
                if pos == -1:
                    error=True
                    self.errormsgbox("尋找<sound>標籤失敗")
                else:
                    voice_mod=False
                # text=text.replace("sound>","sound>\n\t\t\t<voice_mod> </voice_mod>",1)
            else:
                frontpos=pos+10
                backpos=text.find("voice_mod",frontpos)
                backpos=backpos-2
            # text.replace(text[frontpos:backpos],"",1)
        if(error):
            return error
        else:
            if(voice_mod):
                text=text.replace(text[frontpos:backpos],"\t{}\t".format(self.mod),1)
            else:
                text=text.replace("sound>","sound>\n\t\t\t<voice_mod>\t{}\t</voice_mod>".format(self.mod),1)
            self.backup()
            with open(paths+xmlfile.format(""),'w',encoding='utf-8') as f:
                f.write(text)
            return error
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.resize(500,360)
    window.show()

    sys.exit(app.exec_())