# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import random
from time import sleep
class InstaPy():
    def __init__(self):
        self.browser = webdriver.Firefox()  
        print('Author = [Ziorkoo]')
        time.sleep(0.5)
        print('GitHub = brak')
        time.sleep(0.5)
        print('YouTube = brak')
        time.sleep(0.5)
        print('NEW VERSION ---> BotInstagrambyZiorkoo.py ver. 1.0')
        time.sleep(0.5)
 
 
 
    ### ---> logowanie

    def login(self):
        self.login = "login" ##<--- tu wpisz login
        self.password = "haslo" ##<--- tu wpisz hasoo
        self.browser.get('https://www.instagram.com/')
        rand = random.randint(10,15)
        sleep(rand)
        ##---> click to accept cookies.    
        self.acceptbutton = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        rand = random.randint(10,15)
        sleep(rand)
        self.acceptbutton.click()
        rand = random.randint(10,15)
        sleep(rand)
    ##---> end     
        self.emailForm = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)
        rand = random.randint(10,15)
        sleep(rand)
        self.passwordForm = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        rand = random.randint(10,15)
        sleep(rand)
        self.loginButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        rand = random.randint(10,15)
        sleep(rand)
        self.loginButton.click()
        rand = random.randint(10,15)
        sleep(rand)
        self.browser.get('https://www.instagram.com/explore/people/suggested/' )
        rand = random.randint(10,15)
        sleep(rand)
        while(True):
            while(True):
                button = self.browser.find_element_by_xpath('//button[text()="Obserwuj"]')
                if(button == None):
                    print("nie zmaleziono przycisku")
                    self.refresh()
                    break
                
                button.click()
                rand = random.randint(10,15)
                sleep(rand)
bot = InstaPy()
bot.login()     
