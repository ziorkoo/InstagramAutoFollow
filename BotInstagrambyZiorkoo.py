# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import random
from time import sleep
import getpass

name = """
  .--.   .-. .-.  _______  .---.   ,---.       _____   ,-.  .---.   ,---.    ,-. .-.  .---.    .---.   
 / /\ \  | | | | |__   __|/ .-. )  | .-.\     /___  /  |(| / .-. )  | .-.\   | |/ /  / .-. )  / .-. )  
/ /__\ \ | | | |   )| |   | | |(_) | `-'/        / /)  (_) | | |(_) | `-'/   | | /   | | |(_) | | |(_) 
|  __  | | | | |  (_) |   | | | |  |   (        / /(_) | | | | | |  |   (    | | \   | | | |  | | | |  
| |  |)| | `-')|    | |   \ `-' /  | |\ \      / /___  | | \ `-' /  | |\ \   | |) \  \ `-' /  \ `-' /  
|_|  (_) `---(_)    `-'    )---'   |_| \)\    (_____/  `-'  )---'   |_| \)\  |((_)-'  )---'    )---'   
                          (_)          (__)                (_)          (__) (_)     (_)      (_)      
"""
class InstaPy():
    def __init__(self):
        self.browser = webdriver.Firefox()  
        print(name)
        time.sleep(0.5)
        print('GitHub = https://github.com/ziorkoo')
        time.sleep(0.5)
        print('YouTube = https://www.youtube.com/channel/UCvdG_WahSIRa3m5CHREtLJg')
        time.sleep(0.5)
        print('NEW VERSION ---> BotInstagrambyZiorkoo.py ver. 1.0')
        time.sleep(0.5)
 

 
    ### ---> logowanie

    def login(self):
        logins = input("Login: ")
        password =  getpass.getpass('haslo dla "'+logins+'": ')
        follow = input("Wybierz co ma bot robić[follow/unfollow]: ")
        hasztag = input("Wybierz hasztag jaki ma obserwować: ")
        print("Niczego nie ruszaj, bot sie sam zaloguje a jeśli mu w czymś przerwiesz przestanie pracować!")
        self.logins = logins
        self.password = password
        self.browser.get('https://www.instagram.com/')
        rand = random.randint(2,5)
        sleep(rand)
        ##---> click to accept cookies.    
        self.acceptbutton = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        rand = random.randint(2,5)
        sleep(rand)
        self.acceptbutton.click()
        rand = random.randint(2,5)
        sleep(rand)
    ##---> end     
        self.emailForm = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.logins)
        rand = random.randint(2,5)
        sleep(rand)
        self.passwordForm = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        rand = random.randint(2,5)
        sleep(rand)
        self.loginButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        rand = random.randint(2,5)
        sleep(rand)
        self.loginButton.click()
        rand = random.randint(2,5)
        sleep(rand)
        if follow == "follow":
            self.browser.get('https://www.instagram.com/explore/tags/' + hasztag )
            rand = random.randint(2,5)
            self.left = random.randint(1,3)
            self.left = str(self.left)
            self.downIndex = random.randint(1,3)
            self.downIndex = str(self.downIndex)
            self.photo = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+ self.left + ']/div['+ self.downIndex +']/a/div')
            self.photo.click()
            time.sleep(2)
            self.click_follow()
            time.sleep(2)

        def n_photo(self):
            time.sleep(3)
            while(True):
                while(True):
                    if self.browser.find_element_by_xpath('//button[text()="Obserwowanie"]'):
                        self.next_photo_button = self.browser.find_element_by_link_text('Dalej')
                        self.next_photo_button()
                        rand = random.randint(15,20)
                        sleep(rand)

        def click_follow(self):
            time.sleep(3)
            while(True):
                while(True):
                    if self.browser.find_element_by_xpath('//button[text()="Obserwuj"]'):
                        button = self.browser.find_element_by_xpath('//button[text()="Obserwuj"]')
                        button.click()
                        self.n_photo()
                        rand = random.randint(15,20)
                        sleep(rand)
bot = InstaPy()
bot.login()     
