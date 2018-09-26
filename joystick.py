from tkinter import *
 
root = Tk()
root.title("joystick")
# So that it becomes of fixed size
root.resizable(0, 0)
# So that it remains on top of the screen
root.wm_attributes("-topmost", 1)
 
# Label
Label1 = Label(root, text = "joystick app")
Label1.grid(row=0, columnspan=8)
 
# Variables
equa = ""
equation = StringVar()
calculation = Label(root, textvariable = equation)
 
equation.set("Enter your expression : ")
 
calculation.grid(row=2, columnspan=8)
 


#calculation.grid(row=2, columnspan=8)
 
def btnPress(num):
    global equa
    equa = equa + str(num)
    #equation.set(equa)
    print(equa)
    if(equa=='0'):
        print("moving forward")
    elif(equa=='1'):
        print("turned right")
    elif(equa=='2'):
        print("stoped")
    elif(equa=='3'):
        print("turned left")
    elif(equa=='4'):
        print("moving backward")
    elif(equa=='5'):
        print("moving fast")
    else:
        print("break applied")
    equation.set(equa)
    equa = ""
    equation.set("")
        
 
def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""
 
def ClearPress():
    global equa
    equa = ""
    equation.set("")
#def btnPress(backward):
    #print("moving backward")

#def btnPress(right):
    #print("turned right")
    
#def btnPress(left):
    #print("tun left")
    






#Button0 = Button(root, text="0", command = lambda:btnPress(0), borderwidth=1, relief=SOLID)
#Button0.grid(row = 6, column = 2, padx=10, pady=10)
#Button1 = Button(root, text="1", command = lambda:btnPress(1), borderwidth=1, relief=SOLID)
#Button1.grid(row = 3, column = 1, padx=10, pady=10)
Button2 = Button(root, text="forward", command = lambda:btnPress(0), borderwidth=1, relief=SOLID)
Button2.grid(row = 3, column = 2, padx=10, pady=10)
#Button3 = Button(root, text="3", command = lambda:btnPress(3), borderwidth=1, relief=SOLID)
#Button3.grid(row = 3, column = 3, padx=10, pady=10)
Button4 = Button(root, text="right", command = lambda:btnPress(1), borderwidth=1, relief=SOLID)
Button4.grid(row = 4, column = 1, padx=10, pady=10)
Button5 = Button(root, text="stop", command = lambda:btnPress(2), borderwidth=1, relief=SOLID)
Button5.grid(row = 4, column = 2, padx=10, pady=10)
Button6 = Button(root, text="left", command = lambda:btnPress(3), borderwidth=1, relief=SOLID)
Button6.grid(row = 4, column = 3, padx=10, pady=10)
#Button7 = Button(root, text="7", command = lambda:btnPress(7), borderwidth=1, relief=SOLID)
#Button7.grid(row = 5, column = 1, padx=10, pady=10)
Button8 = Button(root, text="backward", command = lambda:btnPress(4), borderwidth=1, relief=SOLID)
Button8.grid(row = 5, column = 2, padx=10, pady=10)
#Button9 = Button(root, text="9", command = lambda:btnPress(9), borderwidth=1, relief=SOLID)
#Button9.grid(row = 5, column = 3, padx=10, pady=10)
button10 = Button(root, text="Accelarator", command = lambda:btnPress(5), borderwidth=1, relief=SOLID)
button10.grid(row = 3, column = 4, padx=10, pady=10)
#Minus = Button(root, text="Subtract", command = lambda:btnPress("-"), borderwidth=1, relief=SOLID)
#Minus.grid(row = 4, column = 4, padx=10, pady=10)
#Multiply = Button(root, text="Multiply", command = lambda:btnPress("*"), borderwidth=1, relief=SOLID)
#Multiply.grid(row = 5, column = 4, padx=10, pady=10)
button11 = Button(root, text="brake", command = lambda:btnPress(6), borderwidth=1, relief=SOLID)
button11.grid(row = 6, column = 4, padx=10, pady=10)
#Equal = Button(root, text="Equals", command = EqualPress, borderwidth=1, relief=SOLID)
#Equal.grid(row=6, column=3, padx=10, pady=10)
#Clear = Button(root, text="Clear", command = ClearPress, borderwidth=1, relief=SOLID)
#Clear.grid(row = 6, column = 1, padx=10, pady=10)
 
root.mainloop()
