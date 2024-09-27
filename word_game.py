from tkinter import *
import random
import time

win = Tk()
win.geometry('300x300')
win.resizable(0,0)

words = ["washington", "oregon", "california", "ohio", "colorado", "michigan", "florida", "oklahoma"]
word = random.choice(words)

char_list = list(word)
random.shuffle(char_list)
shuffled_string = ''.join(char_list)

current_char_index = 0

def check_answer():
    answer = v2.get().lower()
    if answer == word:
        lb2.config(text="Correct!", fg="green")
    else:
        lb2.config(text="Incorrect!", fg="red")

def hint():
    global current_char_index
    if current_char_index < len(word):
        current_hint = lb3.cget("text") 
        lb3.config(text=current_hint + word[current_char_index])  
        current_char_index += 1

def ran():
    global word, char_list, shuffled_string, current_char_index

    word = random.choice(words)  
    char_list = list(word) 
    random.shuffle(char_list) 
    shuffled_string = ''.join(char_list) 
    current_char_index = 0 

    lb1.config(text=shuffled_string) 
    lb2.config(text="") 
    lb3.config(text="") 
    v2.set("")  



v2 = StringVar()


lb1 = Label(win, text= shuffled_string, font=('Arial', 18))
lb2 = Label(win, text="", font=('Arial', 18))
lb3 = Label(win, text="", font=('Arial', 18))

e1 = Entry(win,width=35 , textvariable=v2)

bt1 = Button(win, text='My Answer is', width=15, command=check_answer)
bt2 = Button(win, text='H i n t', width=15, command=hint)
bt3 = Button(win, text='Pick Another', width=15,command=ran)

lb1.place(x=20, y=20)
lb2.place(x=160, y=120)
lb3.place(x=160, y=150)


e1.place(x=20, y=60)

bt1.place(x=30, y=100)
bt2.place(x=30, y=140)
bt3.place(x=30, y=180)





win.mainloop()
