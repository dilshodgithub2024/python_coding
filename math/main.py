from tkinter import *

wnd = Tk()
wnd.geometry("370x640")
wnd.title("kankulator")

first = Entry( bg = "white")
first.place(x = 60, y = 100, width=250, height=50)

first_txt = Label(text="MATH", font="Arial 14")
first_txt.place(x = 120, y = 20, width=100, height=50)

second = Entry(bg="white")
second.place(x = 60, y = 180, width=250, height=50)




hisobla1 = StringVar()
hisobla2 = StringVar()
hisobla3 = StringVar()
hisobla4 = StringVar()

answer = Label(text=0, bg="orange", fg = "white", font= "Arial 14", textvariable=hisobla1)
answer.place(x = 60, y = 340, width=250, height=50)

answer = Label(text=0, bg="orange", fg = "white", font= "Arial 14", textvariable=hisobla2)
answer.place(x = 60, y = 420, width=250, height=50)

answer = Label(text=0, bg="orange", fg = "white", font= "Arial 14", textvariable=hisobla3)
answer.place(x = 60, y = 500, width=250, height=50)

answer = Label(text=0, bg="orange", fg = "white", font= "Arial 14", textvariable=hisobla4)
answer.place(x = 60, y = 580, width=250, height=50)



def plus():
    hisobla1.set(int(first.get()) + int(second.get()))

def minus():
    hisobla2.set(int(first.get()) - int(second.get()))

def kopaytirish():
    hisobla3.set(int(first.get()) / int(second.get()))

def bolish():
    hisobla4.set(int(first.get()) * int(second.get()))

btnp = Button(text="+", bg="blue", fg = "white", font="Arial 14", command=plus)
btnp.place(x = 60, y = 260, width=50, height=50)

btnm =  Button(text="-", bg="blue", fg="white", font="Arial 14", command=minus)
btnm.place(x = 120, y = 260, width=50, height=50)

btnb = Button(text=":", bg = "blue", fg = "white", font="Arial 14", command=kopaytirish)
btnb.place(x = 180, y = 260, width=50, height=50)


btnk = Button(text="x", bg = "blue", fg = "white", font="Arial 14", command=bolish)
btnk.place(x = 240, y = 260, width=50, height=50)



wnd.mainloop()