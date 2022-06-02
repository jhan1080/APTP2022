from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
from bs4 import BeautifulSoup
import requests
from tkinter import *
import threading
import time
import keyboard

#####################################################
# 기본설정 크롬드라이버 자동다운
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"ChromeDriver is installed: {driver_path}")
else:
    print(f"install the ChromeDriver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)


####################################################
# 런어스 로그인 함수
def learnus_login(event):
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

    # 사용자 정보 가져오기
    driver.get("https://www.learnus.org/?lang=")
    learnus_page_source = driver.page_source
    soup = BeautifulSoup(learnus_page_source, 'html.parser')

    studentid = ent1.get()
    print("\n사용자 학번:")
    print(studentid)

    while (True):
        if keyboard.is_pressed("esc"):
            break

    driver.close()
    print("드라이버 종료")


# 런어스 로그인 함수 쓰레드를 만들기
def login(event):
    threading.Thread(target=learnus_login).start()

#####################################################
win = Tk()
win.geometry("450x750+540+40")
win.title("대여 물품 현황 알리미 앱")
win.iconbitmap(default='learnus_logo.ico')
win.option_add("*Font", "맑은고딕 20")
background2 = PhotoImage(file="background2.png")
lab4=Label(win, image=background2)
lab4.pack()
# id 라벨과 입력창
lab1 = Label(win)
lab1.config(text="학번")
lab1.pack()
lab1.place(x=190, y=320)
ent1 = Entry(win)
ent1.pack()
ent1.place(x=60, y=360)

# pw 라벨과 입력창
lab2 = Label(win)
lab2.config(text="비밀번호")
lab2.pack()
lab2.place(x=165, y=400)
ent2 = Entry(win)
ent2.config(show="*")
ent2.pack()
ent2.place(x=60, y=440)

# 로그인 버튼 넣기
btn = Button(win)
btn.config(width=10, height=1)
btn.config(text="로그인")
btn.pack()
btn.place(x=140, y=480)

# Enter 누르면 로그인
ent2.bind("<Return>", learnus_login)
# 로그인 버튼 왼쪽 클릭하면 로그인
btn.bind("<Button-1>", learnus_login)

win.mainloop()
