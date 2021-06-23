from tkinter import *
from math import *
import parser

root = Tk()
root.iconbitmap("./icono.ico")
root.title("CALCULADORA") #nombre
root.geometry("350x660") #witdh,height
root.resizable(False,False)
root.config(background="purple3")
color=("maroon1")
color2=("dodger blue")
ancho=8
alto=3

#mostrar numeros
display=Entry(root,background="SkyBlue1",bd=15,width=22,font=('arial',18,'bold'),justify="right")
#display.insert(0,'Escribe...')
display.place(x=10,y=10)

i=0

def get_number(n):
    global i
    display.insert(i,n)
    i+=1
def get_operation(operator):
    global i
    operator_len=len(operator)
    display.insert(i,operator)
    i+=operator_len

def clear():
    display.delete(0,END)

def clear_uno():
    display_state=display.get()
    if len(display_state):
        display_new=display_state[:-1]
        clear()
        display.insert(0,display_new)
    else:
        clear()

def igual():
    display_state = display.get()
    try:
        math_expression= parser.expr(display_state).compile()
        resultado=eval(math_expression)
        clear()
        display.insert(0,resultado)
    except:
        clear()
        display.insert(0,'error')




#crear botones
Button (root,text="%",command=lambda:get_operation("%"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=80)
Button (root,text="AC",command=lambda:clear(),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=80)
Button (root,text="C",command=lambda:clear(),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=80)
Button (root,text="⌫",command=lambda:clear_uno(),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=80)

Button (root,text="sin",command=lambda:get_operation("sin("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=152)
Button (root,text="cos",command=lambda:get_operation("cos("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=152)
Button (root,text="tan",command=lambda:get_operation("tan("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=152)
Button (root,text="log",command=lambda:get_operation("log10("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=152)


Button (root,text="π",command=lambda:get_operation("pi"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=224)
Button (root,text="x²",command=lambda:get_operation("**2"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=224)
Button (root,text="ln",command=lambda:get_operation("log("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=224)
Button(root,text="√",command=lambda:get_operation("sqrt("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=224)


Button (root,text="6",command=lambda:get_number(6),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=296)
Button (root,text="7",command=lambda:get_number(7),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=296)
Button (root,text="8",command=lambda:get_number(8),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=296)
Button (root,text="9",command=lambda:get_number(9),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=296)

Button (root,text="5",command=lambda:get_number(5),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=368)
Button (root,text="4",command=lambda:get_number(4),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=368)
Button (root,text="3",command=lambda:get_number(3),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=368)
Button (root,text="2",command=lambda:get_number(2),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=368)


Button (root,text="1",command=lambda:get_number(1),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=440)
Button (root,text="0",command=lambda:get_number(0),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=440)
Button (root,text="1/x",command=lambda:get_operation("1/"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=440)
Button(root,text="EXP",command=lambda:get_operation("**"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=440)

Button (root,text="+",command=lambda:get_operation("+"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=512)
Button (root,text="-",command=lambda:get_operation("-"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=512)
Button (root,text="×",command=lambda:get_operation("*"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=512)
Button (root,text="÷",command=lambda:get_operation("/"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=512)

Button (root,text=",",command=lambda:get_operation("."),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=10,y=584)
Button (root,text="(",command=lambda:get_operation("("),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=90,y=584)
Button(root,text=")",command=lambda:get_operation(")"),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=170,y=584)
Button (root,text="=",command=lambda:igual(),background=color,width=ancho,height=alto,font=('arial',12,'bold'),activebackground=color2).place(x=250,y=584)


root.mainloop()