from tkinter import *
import parser
import numpy as np

# Functions for calculator.

# get user input and place it in display area.
i = 0
def get_input(num):
    global i
    len_inc = len(str(num))
    display.insert(i,num)
    i += len_inc

# function for AC.
def clear_all():
    display.delete(0,END)

#function for C
def clear():
    entire_string = display.get()
    size = len(entire_string)
    display.delete(size-1,size)

root = Tk()
root.title('Calculator')
root.config(background='white')
# adding the input field.
display = Entry(root,bg='black',fg='yellow')
#display.place(height=100,width=100)
display.grid(row=1,columnspan=10,sticky=W + E,ipadx=10,ipady=10)
#display.pack(fill=BOTH)
display.grid_rowconfigure(0,weight= 1)

# functionality for equal
def compute():

    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a) 
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,'Error')   

def fact():
    entire_string = display.get()
    fac = 1
    for i in range(1,int(entire_string)+1):
        fac *= i
    
    clear_all()
    display.insert(0,fac)

def compute_log():

    res = np.log(int(display.get()))

    clear_all()
    display.insert(0,res)
    

#adding buttons.
#Button(root,text='0').grid(row=2,column=1)
Button(root,text='1',command=lambda : get_input(1)).grid(row=2,column=1,ipadx=5,ipady=5,padx=5,pady=10)
Button(root,text='2',command=lambda : get_input(2)).grid(row=2,column=2,ipadx=5,ipady=5,padx=5,pady=10)
Button(root,text='3',command=lambda : get_input(3)).grid(row=2,column=3,ipadx=5,ipady=5,padx=5,pady=10)

Button(root,text='4',command=lambda : get_input(4)).grid(row=3,column=1,ipadx=5,ipady=5,padx=5,pady=10)
Button(root,text='5',command=lambda : get_input(5)).grid(row=3,column=2,ipadx=5,ipady=5,padx=5,pady=10)
Button(root,text='6',command=lambda : get_input(6)).grid(row=3,column=3,ipadx=5,ipady=5,padx=5,pady=10)

Button(root,text='7',command=lambda : get_input(7)).grid(row=4,column=1,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='8',command=lambda : get_input(8)).grid(row=4,column=2,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='9',command=lambda : get_input(9)).grid(row=4,column=3,ipadx=5,ipady=5,padx=10,pady=10)

Button(root,text='AC',command=clear_all,bg='red').grid(row=5,column=1,ipadx=5,ipady=5,padx=10,pady=10)

# Operator Buttons.

Button(root,text='+',command=lambda: get_input('+')).grid(row=2,column=4,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='-',command=lambda : get_input('-')).grid(row=3,column=4,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='*',command=lambda : get_input('*')).grid(row=4,column=4,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='/',command=lambda : get_input('/')).grid(row=5,column=4,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='0',command=lambda : get_input(0)).grid(row=5,column=2,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='=',command=lambda: compute()).grid(row=2,column=6,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='C',command=lambda: clear(),bg='green',fg='white').grid(row=5,column=3,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='log',command=lambda: compute_log()).grid(row=2,column=5,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='exp',command=lambda: get_input('**')).grid(row=3,column=5,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='x!',command = lambda:fact()).grid(row=4,column=5,ipadx=5,ipady=5,padx=10,pady=10)
Button(root,text='pi',command=lambda: get_input('3.14')).grid(row=5,column=5,ipadx=5,ipady=5,padx=10,pady=10)


root.mainloop()