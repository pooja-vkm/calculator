from tkinter import *
window=Tk()
window.title("CALCULATOR")
expression = ""
result=False
def press(num):
    global expression
    global result
    if result=True & str(num).isdigit:
        expression=" "
        result=False
    expression=expression+str(num)
    equation.set(expression)

def backspace():
    global expression
    expression=expression[:-1]
    equation.set(expression)


def clear():
    equation.set("")

def equal():
    global expression
    try:
        value=str(eval(expression))
        equation.set(value)
        expression=value
        result=True

    except:
        equation.set("error")
        expression=" "


equation= StringVar()
entry_line=Entry(window, textvariable=equation)
entry_line.grid(columnspan=8,ipadx=100)


button1=Button(text="1",width=5,height=3,command=lambda :press(1))
button2=Button(text="2",width=5,height=3,command=lambda :press(2))
button3=Button(text="3",width=5,height=3,command=lambda: press(3))
button4=Button(text="4",width=5,height=3,command=lambda:press(4))
button5=Button(text="5",width=5,height=3,command=lambda :press(5))
button6=Button(text="6",width=5,height=3,command=lambda :press(6))
button7=Button(text="7",width=5,height=3,command=lambda :press(7))
button8=Button(text="8",width=5,height=3,command=lambda :press(8))
button9=Button(text="9",width=5,height=3,command=lambda :press(9))
button0=Button(text="0",width=5,height=3,command=lambda :press(0))
button_dec=Button(text=".",width=5,height=3,command=lambda :press('.'))
button_add=Button(text="+",width=5,height=3,command=lambda :press('+'))
button_sub=Button(text="-",width=5,height=3,command=lambda :press('-'))
button_mul=Button(text="*",width=5,height=3,command=lambda :press('*'))
button_div=Button(text="/",width=5,height=3,command=lambda :press('/'))
button_ent=Button(text="Enter",width=8,height=3,command=lambda :equal())
button_bck=Button(text="<",width=5,height=3,command=lambda :backspace())
button_clr=Button(text="C",width=5,height=3,command=lambda :clear())


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)
button5.grid(row=1,column=4)
button6.grid(row=2,column=0)
button7.grid(row=2,column=1)
button8.grid(row=2,column=2)
button9.grid(row=2,column=3)
button0.grid(row=2,column=4)
button_add.grid(row=1,column=6)
button_sub.grid(row=1,column=7)
button_mul.grid(row=2,column=6)
button_div.grid(row=2,column=7)
button_clr.grid(row=3,column=0)
button_bck.grid(row=3,column=1)
button_dec.grid(row=3,column=2)
button_ent.grid(row=3,column=3)


window.mainloop()
