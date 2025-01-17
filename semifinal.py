from tkinter import *
import tkinter.messagebox
import tkinter.font as font
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
from bs4 import BeautifulSoup
import requests
import threading
import time
import keyboard
#페이지 넘버
page_num=0

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

#####################################################
# 기본설정 크롬드라이버 자동다운
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"ChromeDriver is installed: {driver_path}")
else:
    print(f"install the ChromeDriver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)



#로그인이 완료될시 1을 리턴
#이 함수 하나만 만들어주시면 됩니다!
def loggedIn():
    # 런어스 홈페이지 접속
    driver = webdriver.Chrome(driver_path)
    url = "https://www.learnus.org/"
    driver.implicitly_wait(15)
    driver.get(url)
    time.sleep(1)

    # 로그인창 들어가기
    driver.find_element(By.CSS_SELECTOR,
                        "#page-header > div.main-header.page-util > div > div.usermenu > ul > li > a.btn.btn-sm.btn-loginout").click()
    time.sleep(1)

    # 아이디 입력창
    id = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(3)")
    id.click()
    id.send_keys(ent1.get())
    time.sleep(1)

    # 비밀번호 입력창
    pw = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(4)")
    pw.click()
    pw.send_keys(ent2.get())
    time.sleep(1)

    # 로그인 버튼
    login_btn = driver.find_element(By.CSS_SELECTOR, '#ssoLoginForm > div > div.form-group.form-group-submit > input')
    login_btn.click()

    # 수강 과목들 가져오기
    driver.get("https://www.learnus.org/?lang=")
    learnus_page_source = driver.page_source
    soup = BeautifulSoup(learnus_page_source, 'html.parser')

    course_title_list = soup.select(
        'div.front-box-body.course_lists > ul > li > div > a > div > div.course-title > h3 ')
    print("\n수강 과목:")
    for title in course_title_list:
        print(title.text)

    # 전체 알림 먼저 들어가기
    time.sleep(1)
    notification_btn1 = driver.find_element(By.CSS_SELECTOR,
                                            '#page-header > div.page-util > div.usermenu > ul > li.nav-item.nav-item-userinfo > button')
    notification_btn1.click()
    time.sleep(1)

    notification_btn2 = driver.find_element(By.CSS_SELECTOR,
                                            '#page-userinfo > div > div.col-3.col-tab > div > a.nav-link.nav-link-noti')
    notification_btn2.click()
    time.sleep(1)

    notification_btn3 = driver.find_element(By.CSS_SELECTOR,
                                            '#mCSB_3_container > div > div.userinfo-title > div > div:nth-child(2) > a')
    notification_btn3.click()

    # 알림 내용들 가져오기

    driver.get("https://www.learnus.org/local/ubnotification/")
    notification_page_source = driver.page_source
    soup = BeautifulSoup(notification_page_source, 'html.parser')

    notification_list = soup.select('#page-content > div > div > div.well.wellnopadding > a > div > div')
    print("\n공지사항 업데이트:")
    for list in notification_list:
        print(list.text)

    while (True):
        if keyboard.is_pressed("esc"):
            break

    driver.close()
    print("드라이버 종료")



def login(event):
    threading.Thread(target=loggedIn()).start()


#다음 페이지로
def next_image():
    global page_num
    page_num=page_num+1
    lab_d.configure(image=background[page_num])

#두번째 페이지 버튼 생성
def show_page2():
    login = Button(win, text="Login", bg="#264bb4", fg="#ffffff", state=DISABLED, font=startfont,
                   command=lambda: [next_image(), login.destroy(), show_page3()])
    login.place(x=185, y=660)

    # id 라벨과 입력창
    lab1 = Label(win)
    lab1.config(text="학번")
    lab1.place(x=300, y=350)
    lab1.pack()

    ent1 = Entry(win)
    ent1.pack()
    ent1.place(x=63, y=330)

    # pw 라벨과 입력창
    lab2 = Label(win)
    lab2.config(text="비밀번호")
    lab2.pack()
    ent2 = Entry(win)
    ent2.config(show="*")
    ent2.pack()
    ent2.place(x=63, y=390)

    # 로그인 버튼 넣기
    btn = Button(win)
    btn.config(width=10, height=1)
    btn.config(text="로그인")
    btn.pack()

    # Enter 누르면 로그인
    ent2.bind("<Return>", loggedIn())
    # 로그인 버튼 왼쪽 클릭하면 로그인
    login.bind("<Button-1>", loggedIn())

    if loggedIn() == 1:
        login.configure(state=ACTIVE)

#세번째 페이지 버튼 생성
def show_page3():
    usingFont = font.Font(family='Helvetica', size="20")

    # 물품 버튼
    button1 = Button(win, text="    첫번째 물품    ", font=usingFont)
    button2 = Button(win, text="    두번째 물품    ", font=usingFont)
    button3 = Button(win, text="    세번째 물품    ", font=usingFont)
    button4 = Button(win, text="    네번째 물품    ", font=usingFont)
    button1.place(x=30, y=200)
    button2.place(x=30, y=280)
    button3.place(x=30, y=360)
    button4.place(x=30, y=440)

    # 대여/반납 버튼
    button5 = Button(win, text="대여", font=usingFont, command=lambda: rentalAndReturn(button5, 1))
    button6 = Button(win, text="대여", font=usingFont, command=lambda: rentalAndReturn(button6, 2))
    button7 = Button(win, text="대여", font=usingFont, command=lambda: rentalAndReturn(button7, 3))
    button8 = Button(win, text="대여", font=usingFont, state=DISABLED, command=lambda: rentalAndReturn(button8, 4))
    button5.place(x=350, y=200)
    button6.place(x=350, y=280)
    button7.place(x=350, y=360)
    button8.place(x=350, y=440)

    # 수량 버튼
    button9 = Button(win, text=str(num1) + "/5", font=usingFont)
    button10 = Button(win, text=str(num2) + "/5", font=usingFont)
    button11 = Button(win, text=str(num3) + "/5", font=usingFont)
    button12 = Button(win, text=str(num4) + "/5", font=usingFont)
    button9.place(x=270, y=200)
    button10.place(x=270, y=280)
    button11.place(x=270, y=360)
    button12.place(x=270, y=440)

    # 종료 버튼
    button13 = Button(win, text="종료", font=usingFont, command=lambda: exitApp())
    button13.place(x=185, y=560)


win = Tk()
win.geometry("450x750+540+40")
win.title("대여 물품 현황 알리미 앱")
win.iconbitmap(default='learnus_logo.ico')
win.option_add("*Font", "맑은고딕 20")
background = [PhotoImage(file="background1.png"),
              PhotoImage(file="background2.png"),
              PhotoImage(file="background3.png")]
lab_d = Label(win, image=background[0])
lab_d.pack()


startfont = font.Font(size="20")

taptostart = Button(win, text="Tap to Start", bg="#264bb4", fg="#ffffff",
                    font=startfont, command=lambda: [next_image(), taptostart.destroy(), show_page2()])
taptostart.place(x=142, y=660)



win.mainloop()