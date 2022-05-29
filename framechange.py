from tkinter import *

#페이지 넘버
page_num=0

#이전 페이지로
def forward_image():
    global page_num
    page_num=page_num-1
    lab_d.configure(image=background[page_num])

#다음 페이지로
def next_image():
    global page_num
    page_num=page_num+1
    lab_d.configure(image=background[page_num])

win = Tk()
win.geometry("450x750+540+40")
win.title("대여 물품 현황 알리미 앱")
win.iconbitmap(default='learnus_logo.ico')
win.option_add("*Font", "맑은고딕 20")
lab_d = Label(win)
lab_d.pack()

background = [PhotoImage(file="background1.png"),
               PhotoImage(file="background2.png")]
taptostart = Button(win, image=background[0], command=next_image)
taptostart.pack()

win.mainloop()