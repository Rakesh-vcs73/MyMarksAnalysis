#Just curious to see the statistical properties of my marks
#Having FUN with data analysis

import tkinter
from tkinter import *
import time
import random
import matplotlib.pyplot as plt;plt.rcdefaults()

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import math
from array import *

root=tkinter.Tk()
root.title('Marks Analysis: Rakesh V USN: 1VE16CS073')
root.geometry('1366x768')


#My marks in sem 3rd, 4th, 5th and 6th sem

result=[[86,72,80,73,74,57,99,99],[92,76,75,67,72,73,45,99],[65,80,61,65,80,89,97,97],[74,77,67,76,80,68,99,95]]
MeanArr=[]
MedianArr=[]
StdArr=[]
SkewArr=[]
Frame1=Frame(root,width=455,height=384,bg='white').place(x=0,y=0)
Frame2=Frame(root,width=455,height=384,bg='white').place(x=455,y=0)
Frame3=Frame(root,width=455,height=384,bg='white').place(x=910,y=0)
Frame4=Frame(root,width=455,height=384,bg='white').place(x=0,y=384)
Frame5=Frame(root,width=455,height=384,bg='white').place(x=455,y=384)
Frame6=Frame(root,width=455,height=384,bg='white').place(x=910,y=384)

def simulate():
    MeanArr.clear()
    MedianArr.clear()
    StdArr.clear()
    SkewArr.clear()
    Mean=0
    Median=0
    Std=0
    Variance=0
    Skewness=0
    delay=0

    for i in range(0,4):
        Mean=np.mean(result[i])
        Median=np.median(result[i])
        Variance=np.var(result[i])
        Std=np.std(result[i])
        MeanArr.append(Mean)
        MedianArr.append(Median)
        StdArr.append(Std)
        if(Std!=0):
            Skewness = (3*(Mean-Median)/Std)
        else:
            Skewness = 0
        SkewArr.append(Skewness)
        SkewAvg=np.mean(SkewArr)

        text=Label(Frame2, text="   Statistical Properties ",bg='white',font=("Helvetica", 18),fg='blue')
        text.place(x=500,y=30)

        text = Label(Frame2, text="Mean :",bg='white',font=("Helvetica", 16),fg='blue')
        text.place(x=450,y=96)
        text = Label(Frame2, text=Mean,font=("", 16),bg='white')
        text.place(x=630,y=96)

        text = Label(Frame2, text="Median :",bg='white',font=("Helvetica", 16),fg='blue')
        text.place(x=450, y=144)
        text = Label(Frame2, text=Median,font=("", 16),bg='white')
        text.place(x=630, y=144)

        text = Label(Frame2, text="Standard Deviation:",bg='white',font=("Helvetica", 16),fg='blue')
        text.place(x=450, y=192)
        text = Label(Frame2, text=Std,font=("", 16),bg='white')
        text.place(x=640, y=192)

        text = Label(Frame2, text="Variance :",bg='white',font=("Helvetica", 16),fg='blue')
        text.place(x=450, y=240)
        text = Label(Frame2, text=Variance,font=("", 16),bg='white')
        text.place(x=630, y=240)

        text = Label(Frame2, text="Skewness :",bg='white',font=("Helvetica", 16),fg='blue')
        text.place(x=450, y=288)
        text = Label(Frame2, text=Skewness,font=("", 16),bg='white')
        text.place(x=630, y=288)


        #text = Label(Frame1, text="Skewness Average :",bg='white',font=("Helvetica", 16),fg='blue')
        #text.place(x=10, y=150)
        #text = Label(Frame2, text=SkewAvg,font=("", 16),bg='white')
        #text.place(x=50, y=200)

        
        

        root.update()
        #to update the frame erasing previous data
        #for widget in Frame2.winfo_children():
        #    widget.destroy()
        fig = Figure()
        fig.add_subplot(111).plot(MeanArr)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=910,y=10,width=450,height=350)

        fig = Figure()
        fig.add_subplot(111).plot(MedianArr)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=370,width=450,height=350)

        fig = Figure()
        fig.add_subplot(111).plot(StdArr)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=455,y=370,width=450,height=350)

        fig = Figure()
        fig.add_subplot(111).plot(SkewArr)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=910,y=370,width=450,height=350)

        Label(Frame3,text="Graph for Mean",bg='white').place(x=910,y=0)
        Label(Frame4,text="Graph for Median",bg='white').place(x=0,y=360)
        Label(Frame5,text="Graph for Standard Deviation",bg='white').place(x=455,y=360)
        Label(Frame6,text="Graph for Skewness",bg='white').place(x=910,y=360)
        time.sleep(delay)


Label(Frame1, text = "Marks Analysis\nName: Rakesh V\nUSN: 1VE16CS073",bg='white',font=("Times", 24),fg='midnight blue').place(x=20,y=100)
simulate()

root.mainloop()
