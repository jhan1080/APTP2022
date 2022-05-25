from tkinter import *

win = Tk()
win.geometry("550x200")
win.title('Tricks_Office')

frame1 = Frame(win)
frame1.pack()
lbName = Label(frame1, text="Name",width = 10).grid(row=0, column=0, sticky=W)
lbPath = Label(frame1, text="Path",width = 50).grid(row=0, column=1, sticky=W)
btnPath =Button(frame1,text="Change Path",width = 10).grid(row=0, column=2, sticky=W)

frame2 = Frame(win)       # Row of buttons
frame2.pack()
btnAction = Button(frame2,text="Button Name",width = 20).grid(row=0, column=0, sticky=W)
lbAction = Label(frame2, text="Button에 대한 설명입니다.",width = 50).grid(row=0, column=1, sticky=W)

frame3 = Frame(win)       # select of names
frame3.pack()
scroll = Scrollbar(frame3, orient=VERTICAL)
select = Listbox(frame3, yscrollcommand=scroll.set, height=6,width = 60)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

win.mainloop()

