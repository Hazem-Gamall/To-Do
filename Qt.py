import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QCheckBox, QMessageBox, QInputDialog
import string

class Window(QWidget):
    content = ''
    count = int()
    l =[]
    z = []
    ln = []
    a = -30
    num = 0
    countt = len(open('data.txt').readlines())
    xn = []
    # count = len(open('data.txt').readlines())
    # print(count)

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('SD')

        if self.num == 0:


            cnt = len(open('data.txt').readlines())
            with open('data.txt','r')as fl:
                self.z.clear()
                for line in fl:
                    self.xn.append(line)
            for x in range(cnt):
                if self.xn == ' ':
                    continue
                self.a += 30
                self.z.append(QCheckBox(self.xn[x], self))
                self.z[x].show()
                self.z[x].move(0, self.a)

            cnt = 0
            self.xn.clear()
            self.a = -30
            #self.z.clear()

        btn = QPushButton('Add', self)
        btn.move(210,250)
        btn.clicked.connect(self.createobj)

        btn1 = QPushButton('Delete', self)
        btn1.move(210, 280)
        btn1.clicked.connect(self.deleteobj)

        self.show()

    def createobj(self):
        self.num += 1
        if self.num > 1:
            self.ln.clear()
        dlg = QInputDialog()
        dlg.show()
        dlg.exec_()
        if dlg.textValue() != '':
            self.content = dlg.textValue()
            with open('data.txt','a')as file:
                file.write(self.content + '\r')

        self.count = len(open('data.txt').readlines())
        print(self.count)

            # chk = QCheckBox(self.content,self)
            # chk


        with open('data.txt','r') as f:
            for line in f:
                # if len(self.ln) == (self.count-1):
                #     # break
                self.ln.append(line)

        for x in range(self.count):
            if self.num == 1:
                if self.l == ' ':
                    continue
                self.a += 30
                self.l.append(QCheckBox(self.ln[x],self))
                self.l[x].show()
                self.l[x].move(0,self.a)
            if self.num > 1 and x == (self.count-1) and dlg.textValue() != '' :
                self.a += 30
                self.l.append(QCheckBox(self.ln[x], self))
                self.l[x].show()
                self.l[x].move(0, self.a)

    def deleteobj(self):
        n = 0
        sp = 0
        t = ''
        ls = []
        c = ''
        y = ''
        v = ''
        cn = int()
        for x in range(self.countt):
            if self.z[x].isChecked():
                t = str((self.z[x].text()))
                t = t.strip('\n')
                # v = str(t)
                print(t)
                # v = "'" + t + "'"
                file = open('data.txt', 'r')
                c = str(file.readlines())
                # c = c.replace(t,'')
                print(c)
                # print([pos for pos, char in enumerate(c)])
                start = c.find(t)
                print(start)
                index = c.find(t) + len(t) + 6
                print(index)
                sl = slice(start,index,1)
                nw = c.replace(c[sl],'')
                print(nw)

                with open('data.txt', 'w') as f:
                    for char in nw:
                        if char.isalpha() or char == ' ' or char == '\\':
                            if char == '\\':
                                n += 1
                                continue
                            if char == 'n' and n == 1:
                                f.write('\n')
                                n = 0
                                sp += 1
                                continue
                            if char == ' ' and sp == 1:
                                sp = 0
                                continue

                            f.write(char)
                            print(char)
                            if cn == (len(nw)-1):
                                f.write('\n')

                # with open('data.txt', 'r')as fl:
                #     for line in fl:
                #         ls.append(line)
                for x in range(len(self.z)):
                    self.z[x].hide()

        self.initUI()







app = QApplication(sys.argv)

gui = Window()

app.exec_()
