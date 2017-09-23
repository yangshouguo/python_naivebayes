# -*- coding: utf-8 -*-
###################
#画布，使用Canvas小构件
###################
from Tkinter import *
import tkMessageBox as tm
from A_Star_Search import AStar

import time

PASS = 'green'
NOPASS = 'red'
TRACE = 'black'
START = 'white'
TARGET = 'black'

class CanvasDemo():
    def __init__(self,size, function):
        self._size = size
        self._Astarfun = function
        self._trace = []
        self._Buttons = []
        self._Buttons_status = []
        self._startp = ()
        self._target = ()
        window = Tk() #创建窗口
        window.title("A star") #给窗口命名

        # #在窗口画布
        # self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
        # self.canvas.pack()

        #创建frame的框架，窗口window为这个框架的父容器
        self._frame = Frame(window, width = size, height = size, bg='white')
        self._frame.pack()
        self._init_Buttons(self._frame)

        self._frame_hint = Frame(window, width = size, height = size, bg = 'gray')
        self._var = IntVar()
        self._var.set(1)
        Radiobutton(window, text = 'set wall', variable=self._var, value=1, command = self._changeaction).pack(anchor = W)
        Radiobutton(window, text='set start', variable=self._var, value=2, command=self._changeaction).pack(anchor = W)
        Radiobutton(window, text='set target', variable=self._var, value=3, command=self._changeaction).pack(anchor = W)

        Button(window, text='run', command=self.run).pack(anchor=N)

        Label(self._frame_hint,text = 'red represents no pass').pack(anchor = N)
        Label(self._frame_hint,text = 'green reprensents pass').pack(anchor = N)
        self._frame_hint.pack()



        #创建事件循环直到关闭主窗口
        window.mainloop()


    def run(self):
        G = [ [1 if x == PASS else 0 for x in self._Buttons_status[i]] for i in range(self._size) ]
        self._trace = self._Astarfun(G,self._startp,self._target)
        # print self._trace
        if (len(self._trace) > 0 ):
            self._drawTrace()
        else:
            tm.askokcancel('no way!','...')
        pass

    def _drawTrace(self):

        for item in self._trace:
            self._Buttons[item[0]][item[1]].config(bg = TRACE)
            # time.sleep(1)


    def _changeaction(self):
        # print self._var.get()
        pass


    def _init_Buttons(self,frame):
        for i in range(self._size):
            self._Buttons.append([])
            self._Buttons_status.append([])
            for j in range(self._size):
                # print i,j
                name = str(i*self._size+j)
                self._Buttons[i].append(Button(frame,name=name,height=1, width=1))
                self._Buttons_status[i].append(PASS)
                # Button在画布上布局
                # print i,j
                self._Buttons[i][j].grid(row=i+1,column=j+1)
                self._Buttons[i][j].bind('<Button-1>', self._changeColor)
        self._init_Button_Color()


    def _changeColor(self,event):
        # print type(event.widget)
        # for item in event.widget:
        #     print str(item)
        id = event.widget._name
        id = int(id)
        i = id / self._size
        j = id % self._size
        if self._var.get() == 1: #set wall
            if (self._Buttons_status[i][j] == PASS):
                self._Buttons[i][j].config(bg=NOPASS)
                self._Buttons_status[i][j] = NOPASS
            else:
                self._Buttons[i][j].config(bg=PASS)
                self._Buttons_status[i][j] = PASS
        elif self._var.get() == 2:#set start
            self._Buttons[i][j].config(bg=START)
            self._Buttons_status[i][j] = PASS
            self._startp = (i,j)
        else: #set target
            self._Buttons[i][j].config(bg=TARGET)
            self._Buttons_status[i][j] = PASS
            self._target = (i,j)

    def _init_Button_Color(self):

        for i in range(self._size):
            for j in range(self._size):
                self._Buttons[i][j].config(bg=PASS)
                self._Buttons_status[i][j] = PASS
        pass

    def get_status(self):
        return self._Buttons_status,self._startp,self._target



def compute(G,start,target):
    # print G,start,target
    x = AStar(G,len(G),start,target)
    return x.Search()


def main():
    pass
    view = CanvasDemo(20,compute)

if __name__ == '__main__':
    main()