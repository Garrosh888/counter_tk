from tkinter import*
def pluss():
    global a
    a = a + 1
    lbl1["text"] = a
def minus():
    global a
    a = a - 1
    lbl1["text"] = a
window = Tk()
window.resizable(0,0)
window.iconbitmap("j.ico")
a = 0
btn1 = Button(window,text="-",font= (None,24),command=minus)
btn1.grid(row = 3,column=0)
btn2 = Button(window,text="+",font= (None,24),command=pluss)
btn2.grid(row = 3,column=3)
lbl1 = Label(window,text= a,font= (None,24))
lbl1.grid(row = 3,column=2)
lbl2 = Label(window,text= "example_tk",font= (None,24),fg= "red")
lbl2.grid(row = 1 ,column=0, columnspan= 4)


window.mainloop()