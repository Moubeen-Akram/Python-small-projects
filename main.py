import tkinter as tk
window=tk.Tk()
window.title("Calculator")

#to not maximize or minimize the screen window
window.resizable(False,False)

#for screen showing calculation
entry=tk.Entry(width=48,justify='right')
entry.grid(row=0, column=0, columnspan=4)

#to press buttons and it appears on the screen
def press_button(command):
    if command=='1':
        entry.insert(tk.END,"1") #END to show it at end of display screen
    elif command=='2':
        entry.insert(tk.END,"2")
    elif command=='3':
        entry.insert(tk.END,"3")
    elif command=='4':
        entry.insert(tk.END,"4")
    elif command=='5':
        entry.insert(tk.END,"5")
    elif command=='6':
        entry.insert(tk.END,"6")
    elif command=='7':
        entry.insert(tk.END,"7")
    elif command=='8':
        entry.insert(tk.END,"8")
    elif command=='9':
        entry.insert(tk.END,"9")
    elif command=='0':
        entry.insert(tk.END,"0")
    elif(command=='+'):
        entry.insert(tk.END,"+")
    elif(command=="/"):
        entry.insert(tk.END,"/")
    elif(command=='-'):
        entry.insert(tk.END,"-")
    elif(command=='*'):
        entry.insert(tk.END,"*")

#equal command to perform operation of equal
def equal(command):
    command=entry.get()
    try:
        result=eval(command)
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error!")

#clear command to clear the history
def clear(command):
    entry.delete(0,tk.END)



#for buttons of the calculator
#Lambda creates an anonymous function that delays execution until the button is clicked

button1=tk.Button(width=2,text="1",command=lambda: press_button("1"))
button2=tk.Button(width=2,text="2",command=lambda: press_button("2"))
button3=tk.Button(width=2,text="3",command=lambda: press_button("3"))
button4=tk.Button(width=2,text="4",command=lambda: press_button("4"))
button5=tk.Button(width=2,text="5",command=lambda: press_button("5"))
button6=tk.Button(width=2,text="6",command=lambda: press_button("6"))
button7=tk.Button(width=2,text="7",command=lambda: press_button("7"))
button8=tk.Button(width=2,text="8",command=lambda: press_button("8"))
button9=tk.Button(width=2,text="9",command=lambda: press_button("9"))
button10=tk.Button(width=2,text="0",command=lambda: press_button("0"))
button11=tk.Button(width=2,text="/",command=lambda: press_button("/"))
button12=tk.Button(width=2,text="x",command=lambda:press_button("x"))
button13=tk.Button(width=2,text="-",command=lambda:press_button('-'))
button_plus=tk.Button(width=1,text="+",command=lambda:press_button('+'))
button_dot=tk.Button(width=1,text='C',command=lambda:clear('C'))
button_eq=tk.Button(width=1,text='=',command=lambda: equal("="))
button7.grid(row=1,column=0,sticky="nsew") #sticky is used for north,south,east west
button8.grid(row=1,column=1,sticky="nsew")
button9.grid(row=1,column=2,sticky="nsew")
button11.grid(row=1,column=3,sticky="nsew")
button4.grid(row=2,column=0,sticky="nsew")
button5.grid(row=2,column=1,sticky="nsew")
button6.grid(row=2,column=2,sticky="nsew")
button12.grid(row=2,column=3,sticky="nsew")
button1.grid(row=3,column=0,sticky="nsew")
button2.grid(row=3,column=1,sticky="nsew")
button3.grid(row=3,column=2,sticky="nsew")
button13.grid(row=3,column=3,sticky="nsew")
button10.grid(row=4,column=0,sticky="nsew")
button_dot.grid(row=4,column=1,sticky="nsew")
button_eq.grid(row=4,column=2,sticky="nsew")
button_plus.grid(row=4,column=3,sticky="nsew")


#to show the screen
window.geometry("300x200")
#To show it on loop
window.mainloop()
