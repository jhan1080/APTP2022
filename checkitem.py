from tkinter import *
import tkinter.messagebox
import tkinter.font as font

#물품 수량
num1=5
num2=4
num3=4
num4=0



#대여/반납 알고리즘
def rentalAndReturn(button, n):
    global num1
    global num2
    global num3
    global num4

    if button['text'] == "대여":
        #버튼 업데이트
        tkinter.messagebox.showinfo("대여", "해당 물품이 대여되었습니다.")
        button.configure(text="반납", bg="#264bb4", fg="#ffffff")

        #수량 업데이트
        if n == 1:
            num1 = num1 - 1
        elif n == 2:
            num2 = num2 - 1
        elif n == 3:
            num3 = num3 - 1
        elif n == 4:
            num4 = num4 - 1

        button9.configure(text=str(num1)+"/5")
        button10.configure(text=str(num2) + "/5")
        button11.configure(text=str(num3) + "/5")
        button12.configure(text=str(num4) + "/5")

    else:
        tkinter.messagebox.showinfo("반납", "해당 물품이 반납되었습니다.")
        button.configure(text="대여", bg="#f0f0f0", fg="#000000")

        if n == 1:
            num1 = num1 + 1
        elif n == 2:
            num2 = num2 + 1
        elif n == 3:
            num3 = num3 + 1
        elif n == 4:
            num4 = num4 + 1

        button9.configure(text=str(num1) + "/5")
        button10.configure(text=str(num2) + "/5")
        button11.configure(text=str(num3) + "/5")
        button12.configure(text=str(num4) + "/5")


#이용종료
def exitApp():
    msgBox = tkinter.messagebox.askquestion("종료", "이용을 종료하시겠습니까?")
    if msgBox == 'yes':
        win.destroy()
    else:
        pass


win = Tk()
win.geometry("450x750+540+40")
win.title("대여 물품 현황 알리미 앱")
win.iconbitmap(default='learnus_logo.ico')
win.option_add("*Font", "맑은고딕 20")

background = [PhotoImage(file="background1.png"),
              PhotoImage(file="background2.png"),
              PhotoImage(file="background3.png")]

#본 코드에서는 초기화면이 background3으로 되어 있어서 최종본에서는 화면 전환하는 기능으로 연결해야 할 것 같습니다!
lab_d = Label(win, image=background[2])
lab_d.pack()

usingFont=font.Font(family='Helvetica', size="20")

#물품 버튼
button1 = Button(win, text="    첫번째 물품    ", font=usingFont)
button2 = Button(win, text="    두번째 물품    ", font=usingFont)
button3 = Button(win, text="    세번째 물품    ", font=usingFont)
button4 = Button(win, text="    네번째 물품    ", font=usingFont)
button1.place(x=30, y=200)
button2.place(x=30, y=280)
button3.place(x=30, y=360)
button4.place(x=30, y=440)

#대여/반납 버튼
button5 = Button(win, text="대여", font=usingFont, command=lambda: rentalAndReturn(button5, 1))
button6 = Button(win, text="대여", font=usingFont, command=lambda: rentalAndReturn(button6, 2))
button7 = Button(win, text="대여", font=usingFont, command=lambda: rentalAndReturn(button7, 3))
button8 = Button(win, text="대여", font=usingFont, state=DISABLED, command=lambda: rentalAndReturn(button8, 4))
button5.place(x=350, y=200)
button6.place(x=350, y=280)
button7.place(x=350, y=360)
button8.place(x=350, y=440)

#수량 버튼
button9 = Button(win, text=str(num1)+"/5", font=usingFont)
button10 = Button(win, text=str(num2)+"/5", font=usingFont)
button11 = Button(win, text=str(num3)+"/5", font=usingFont)
button12 = Button(win, text=str(num4)+"/5", font=usingFont)
button9.place(x=270, y=200)
button10.place(x=270, y=280)
button11.place(x=270, y=360)
button12.place(x=270, y=440)

#종료 버튼
button13 = Button(win, text="종료", font=usingFont, command=lambda: exitApp())
button13.place(x=185, y=560)


win.mainloop()