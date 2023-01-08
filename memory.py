import numpy as np
import random
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import font as tkFont
import time
from threading import Thread    
import threading
from tkinter import *

global btn_counter
global button_dict
global table
global done
global message ,text_box, timer_txt
global timeVal
global reset


btn_counter = []
button_dict = {}
done = 0
message = 0
timeVal = 0
reset = 0


top = tk.Tk()
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
helv26 = tkFont.Font(family='Helvetica', size=26, weight=tkFont.BOLD)



def Table_gen(x,y):
    arr_first = np.arange(1,int((x*y)/2)+1)
    arr_sec = np.arange(1,int((x*y)/2)+1)
    arr_puzzle = np.concatenate((arr_first, arr_sec))
    random.shuffle(arr_puzzle)
    arr_puzzle = arr_puzzle.reshape(x,y)
        
    return arr_puzzle

def changeColor(btn):
    global button_dict
    global btn_counter
    global table
    global done
    global message
    global timeVal
    global reset
    global timer_txt

    message += 1
    text_box.delete(1.0, tk.END)
    text_box.insert('end', message)

    value_indx1 = list(button_dict.values()).index(btn)
    value_btn1 = table[int(value_indx1/4),int(value_indx1%4)]

    if (len(btn_counter) == 2):
        btn_counter[0].config(text="?")
        btn_counter[1].config(text="?")
        btn_counter[0].config(bg='#00f', fg='#fff')
        btn_counter[1].config(bg='#00f', fg='#fff')
        
        btn_counter = []
    
    if (len(btn_counter) == 0):
        btn.config(bg='#f00')
        btn.config(text=value_btn1)
        btn_counter.append(btn)
    else:
        value_indx2 = list(button_dict.values()).index(btn_counter[len(btn_counter)-1])
        value_btn2 = table[int(value_indx2/4),int(value_indx2%4)]

        if(btn_counter[0] == btn):
            btn.configure(bg='#00f', fg='#fff')
            btn.config(text="?")
            btn_counter = []

        else:
            if(value_btn1 == value_btn2):
                btn.config(text=value_btn1)
                btn_counter[len(btn_counter)-1].config(text=value_btn1)

                btn.config(state = tk.DISABLED)
                btn_counter[len(btn_counter)-1].config(state = tk.DISABLED)

                btn.config(bg='#ff0')
                btn_counter[len(btn_counter)-1].config(bg='#ff0')
                btn_counter = []
                done +=1
                if done == 8: ##reset part
                    done = 0
                    message = 0
                    timeVal = 0
                    timer_txt.configure(fg='#000')
                    tkMessageBox.showinfo(title="Gratuliere!", message="Du hesch gwunne!")
                    table = Table_gen(4,4)
                    declare()

            else:
                btn.config(text=value_btn1)
                btn.config(bg='#f00')

                btn_counter.append(btn)

def declare():
    global button_dict
    button_dict[0]=tk.Button(top, command=lambda: changeColor(button_dict[0]),text="?", font=helv36)
    button_dict[0].configure(bg='#00f', fg='#fff')
    button_dict[0].grid(row=0,column=0)

    button_dict[1]=tk.Button(top, command=lambda: changeColor(button_dict[1]),text="?", font=helv36)
    button_dict[1].configure(bg='#00f', fg='#fff')
    button_dict[1].grid(row=0,column=1)

    button_dict[2]=tk.Button(top, command=lambda: changeColor(button_dict[2]),text="?", font=helv36)
    button_dict[2].configure(bg='#00f', fg='#fff')
    button_dict[2].grid(row=0,column=2)

    button_dict[3]=tk.Button(top, command=lambda: changeColor(button_dict[3]),text="?", font=helv36)
    button_dict[3].configure(bg='#00f', fg='#fff')
    button_dict[3].grid(row=0,column=3)

    button_dict[4]=tk.Button(top, command=lambda: changeColor(button_dict[4]),text="?", font=helv36)
    button_dict[4].configure(bg='#00f', fg='#fff')
    button_dict[4].grid(row=1,column=0)

    button_dict[5]=tk.Button(top, command=lambda: changeColor(button_dict[5]),text="?", font=helv36)
    button_dict[5].configure(bg='#00f', fg='#fff')
    button_dict[5].grid(row=1,column=1)

    button_dict[6]=tk.Button(top, command=lambda: changeColor(button_dict[6]),text="?", font=helv36)
    button_dict[6].configure(bg='#00f', fg='#fff')
    button_dict[6].grid(row=1,column=2)

    button_dict[7]=tk.Button(top, command=lambda: changeColor(button_dict[7]),text="?", font=helv36)
    button_dict[7].configure(bg='#00f', fg='#fff')
    button_dict[7].grid(row=1,column=3)

    button_dict[8]=tk.Button(top, command=lambda: changeColor(button_dict[8]),text="?", font=helv36)
    button_dict[8].configure(bg='#00f', fg='#fff')
    button_dict[8].grid(row=2,column=0)

    button_dict[9]=tk.Button(top, command=lambda: changeColor(button_dict[9]),text="?", font=helv36)
    button_dict[9].configure(bg='#00f', fg='#fff')
    button_dict[9].grid(row=2,column=1)

    button_dict[10]=tk.Button(top, command=lambda: changeColor(button_dict[10]),text="?", font=helv36)
    button_dict[10].configure(bg='#00f', fg='#fff')
    button_dict[10].grid(row=2,column=2)

    button_dict[11]=tk.Button(top, command=lambda: changeColor(button_dict[11]),text="?", font=helv36)
    button_dict[11].configure(bg='#00f', fg='#fff')
    button_dict[11].grid(row=2,column=3)

    button_dict[12]=tk.Button(top, command=lambda: changeColor(button_dict[12]),text="?", font=helv36)
    button_dict[12].configure(bg='#00f', fg='#fff')
    button_dict[12].grid(row=3,column=0)

    button_dict[13]=tk.Button(top, command=lambda: changeColor(button_dict[13]),text="?", font=helv36)
    button_dict[13].configure(bg='#00f', fg='#fff')
    button_dict[13].grid(row=3,column=1)

    button_dict[14]=tk.Button(top, command=lambda: changeColor(button_dict[14]),text="?", font=helv36)
    button_dict[14].configure(bg='#00f', fg='#fff')
    button_dict[14].grid(row=3,column=2)

    button_dict[15]=tk.Button(top, command=lambda: changeColor(button_dict[15]),text="?", font=helv36)
    button_dict[15].configure(bg='#00f', fg='#fff')
    button_dict[15].grid(row=3,column=3)


def timer():
    global timeVal, timer_txt
    global reset
    while(True):
        time.sleep(1)
        timeVal += 1
        timer_txt.delete(1.0, tk.END)
        timer_txt.insert('end', timeVal)
        if timeVal >=30 :
            timer_txt.configure(fg='#f00')


text_box = Text(top,height=1,width=3,font=helv26,)
text_box.insert('end', message)
text_box.grid(row=1,column=4)


text1 = Text(top,height=1,width=6,font=helv26)
text1.insert('end', "Clicks:")
text1.grid(row=0,column=4)


timer_txt = Text(top,height=1,width=3,font=helv26)
timer_txt.insert('end', timeVal)
timer_txt.grid(row=3,column=4)


text2 = Text(top,height=1,width=6,font=helv26)
text2.insert('end', "Timer:")
text2.grid(row=2,column=4)



table = Table_gen(4,4)
declare()


thread = threading.Thread(target=timer)
thread.start()
top.mainloop()