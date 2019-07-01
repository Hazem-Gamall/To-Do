import sys
import subprocess
import json
from os import path, stat,execl, system
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QCheckBox, QMessageBox, QInputDialog, QVBoxLayout
import string

class window(QWidget):
    s = int
    checklist = {}
    objsCount = -1
    ls = []
    bx = QCheckBox
    lista = []
    readd = True

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.s = int
        # self.checklist = {}
        self.objsCount = -1
        # self.ls = []
        self.bx = QCheckBox
        # self.lista = []

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('SD')

        btn = QPushButton('add', self)
        btn.move(160, 250)
        btn.clicked.connect(self.createobj)

        deletebtn = QPushButton('delete',self)
        deletebtn.move(280,250)
        deletebtn.clicked.connect(self.delete)

        self.read()

        self.show()


    def createobj(self):
        self.objsCount = self.objsCount + 1
        msg = QInputDialog()
        msg.exec_()

        # if path.isfile('data.json') is True:
        #     with open ('data.json','r') as f:
        #         data = json.load(f)
        #         self.checklist = data
        #         print(self.checklist)
        #         print(type(self.checklist))

        txt = msg.textValue()
        if txt != '' and not txt.isspace():
            self.ls.clear()
            for i in self.checklist:
                # self.ls.clear()
                self.ls.append(i)

            if not self.ls:
                self.ls.append(-1)
            print(self.ls,'ls')
            self.s = max(self.ls)
            self.s = int(self.s) + 1

            self.checklist.update({self.s:txt})
            # print(self.checklist,'check')
            # bxx = QCheckBox(txt,self)
            # bxx.show()
            # bxx.move(10, self.s*20)
            # self.lista.append(bxx)
            # print(self.s)
            self.updateS()
            self.initUI()


    def updateS(self):
        # print(json.dumps(self.checklist))

        # if path.isfile('data.json') is True:
        #     with open ('data.json','r') as f:
        #         data = json.load(f)
        #         self.checklist = data
        #         print(self.checklist)
        #         print(type(self.checklist))

        try:
            with open('data.json','w') as f:
                data = json.dump(self.checklist,f)
                # print(data)

                # for i in self.checklist:
                #     self.ls.append(str(i))
                print(max(self.ls))
        except Exception as e:
            print(e)

    def read(self):
        self.ls.clear()
        with open('data.json','r') as f:

            for i in self.lista:
                i.setParent(None)

            if path.getsize('data.json') is not 0:
                data = json.load(f)
                self.checklist = data
                self.sort()
                for i, t in self.checklist.items():
                    self.ls.append(i)
                    txt = t
                    bx = QCheckBox(txt, self)
                    bx.move(10, int(i) * 20)
                    bx.show()
                    print(i,'bx')
                    self.lista.append(bx)
                    print(self.lista)


                # self.s = max(self.ls)
                # self.s = int(self.s) + 1

    def delete(self):
        txt = ''
        isDel = False
        refk = str
        refv = str
        for i in self.lista:
            if i.isChecked():
                print('yaay')
                txt = i.text()
                # i.deleteLater()
                self.lista.remove(i)
                i.setParent(None)
        for key, value in self.checklist.items():
            #
            # if isDel is True:
            #
            #

            if value == txt:

                # self.checklist[str(int(key)+1)] = self.checklist[key]
                del self.checklist[key]
                print(self.checklist)
                isDel = True
                print(key)
                self.updateS()

                self.initUI()

                break

    def sort(self):
        dic = {}
        itr = 0
        for k,i in self.checklist.items():
            dic.update({str(itr):i})
            itr += 1
        self.checklist = dic
        print(self.checklist,'hobaaaa')



app = QApplication(sys.argv)

def main():

    gui = window()

    app.exec_()

try:
    if __name__ == '__main__':
        main()
except Exception as e:
    print(e)