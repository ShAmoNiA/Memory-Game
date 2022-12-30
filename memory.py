import numpy as np
import random
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter import font as tkFont
import time

global btn_counter
global button_dict
global table
global done

btn_counter = []
button_dict = {}
done = 0


top = tk.Tk()
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)



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

    value_indx1 = list(button_dict.keys())[list(button_dict.values()).index(btn)]
    value_btn1 = table[int(value_indx1/4),int(value_indx1%4)]

    if (len(btn_counter) == 2):
        btn_counter[len(btn_counter)-2].config(text="?")
        btn_counter[len(btn_counter)-1].config(text="?")
        btn_counter[len(btn_counter)-2].config(bg='#f0f', fg='#fff')
        btn_counter[len(btn_counter)-1].config(bg='#f0f', fg='#fff')
        
        btn_counter = []
    
    if (len(btn_counter) == 0):
        btn.config(bg='#f00')
        btn.config(text=value_btn1)
        btn_counter.append(btn)
    else:
        value_indx2 = list(button_dict.keys())[list(button_dict.values()).index(btn_counter[len(btn_counter)-1])]
        value_btn2 = table[int(value_indx2/4),int(value_indx2%4)]

        if(btn_counter[0] == btn):
            btn.configure(bg='#f0f', fg='#fff')
            btn_counter[len(btn_counter)-1].configure(bg='#f0f', fg='#fff')
            btn.config(text="?")
            btn_counter[0].config(text="?")
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
                if done == 6: ##reset part
                    done = 0
                    tkMessageBox.showinfo(title="Gratuliere!", message="Du hesch gwunne!")
                    table = Table_gen(3,4)
                    declare()

            else:
                btn.config(text=value_btn1)
                btn_counter[len(btn_counter)-1].config(text=value_btn2)
                btn.config(bg='#f00')
                btn_counter[len(btn_counter)-1].config(bg='#f00')

                btn_counter.append(btn)

def declare():
    global button_dict
    button_dict[0]=tk.Button(top, command=lambda: changeColor(button_dict[0]),text="?", font=helv36)
    button_dict[0].configure(bg='#f0f', fg='#fff')
    button_dict[0].grid(row=0,column=0)

    button_dict[1]=tk.Button(top, command=lambda: changeColor(button_dict[1]),text="?", font=helv36)
    button_dict[1].configure(bg='#f0f', fg='#fff')
    button_dict[1].grid(row=0,column=1)

    button_dict[2]=tk.Button(top, command=lambda: changeColor(button_dict[2]),text="?", font=helv36)
    button_dict[2].configure(bg='#f0f', fg='#fff')
    button_dict[2].grid(row=0,column=2)

    button_dict[3]=tk.Button(top, command=lambda: changeColor(button_dict[3]),text="?", font=helv36)
    button_dict[3].configure(bg='#f0f', fg='#fff')
    button_dict[3].grid(row=0,column=3)

    button_dict[4]=tk.Button(top, command=lambda: changeColor(button_dict[4]),text="?", font=helv36)
    button_dict[4].configure(bg='#f0f', fg='#fff')
    button_dict[4].grid(row=1,column=0)

    button_dict[5]=tk.Button(top, command=lambda: changeColor(button_dict[5]),text="?", font=helv36)
    button_dict[5].configure(bg='#f0f', fg='#fff')
    button_dict[5].grid(row=1,column=1)

    button_dict[6]=tk.Button(top, command=lambda: changeColor(button_dict[6]),text="?", font=helv36)
    button_dict[6].configure(bg='#f0f', fg='#fff')
    button_dict[6].grid(row=1,column=2)

    button_dict[7]=tk.Button(top, command=lambda: changeColor(button_dict[7]),text="?", font=helv36)
    button_dict[7].configure(bg='#f0f', fg='#fff')
    button_dict[7].grid(row=1,column=3)

    button_dict[8]=tk.Button(top, command=lambda: changeColor(button_dict[8]),text="?", font=helv36)
    button_dict[8].configure(bg='#f0f', fg='#fff')
    button_dict[8].grid(row=2,column=0)

    button_dict[9]=tk.Button(top, command=lambda: changeColor(button_dict[9]),text="?", font=helv36)
    button_dict[9].configure(bg='#f0f', fg='#fff')
    button_dict[9].grid(row=2,column=1)

    button_dict[10]=tk.Button(top, command=lambda: changeColor(button_dict[10]),text="?", font=helv36)
    button_dict[10].configure(bg='#f0f', fg='#fff')
    button_dict[10].grid(row=2,column=2)

    button_dict[11]=tk.Button(top, command=lambda: changeColor(button_dict[11]),text="?", font=helv36)
    button_dict[11].configure(bg='#f0f', fg='#fff')
    button_dict[11].grid(row=2,column=3)


table = Table_gen(3,4)
declare()

top.mainloop()