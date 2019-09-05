#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tkhodr
"""


from selenium import webdriver # WebDriver through Selenium
import time # To sleep in orer to be able to authentiate
from utility_methods.utility_methods import * # Imports all from Utility
import urllib.request # Opens URL's using pip interface
import os # Easy file movement


class InstaBot:

    def __init__(self, username=None, password=None):

        self.username = config['IG_AUTH']['USERNAME'] # User name from config
        self.password = config['IG_AUTH']['PASSWORD'] # Pass from config

        self.login_url = config['IG_URLS']['LOGIN']
        self.nav_user_url = config['IG_URLS']['NAV_USER']
        self.get_tag_url = config['IG_URLS']['SEARCH_TAGS']

        self.driver = webdriver.Chrome('/Users/tkhodr/Desktop/Instabot/chromedriver')

        self.logged_in = False # If user is logged in or not

    def login(self):
        """
        Logs into insta via Web Driver
        """

        self.driver.get(self.login_url)

        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]') # login button xpath changes after text is entered, find first

        username_input = self.driver.find_element_by_name('username')
        password_input = self.driver.find_element_by_name('password')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_btn.click()


    def nav_user(self, user):

        self.driver.get(self.nav_user_url.format(user))


    def follow_user(self, user): # To follow a user
        self.nav_user(user)

        follow_buttons = self.find_buttons('Follow')

        for btn in follow_buttons:
            btn.click()



    def like_latest_posts(self, user, n_posts, like=True):# WIP to like posts

        action = 'Like' if like else 'Unlike'

        self.nav_user(user)

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))

        for img in imgs[:n_posts]:
            img.click() 
            time.sleep(1) 
            try:
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click() 
            except Exception as e:
                print(e)
            self.driver.find_elements_by_class_name('ckWGn')[0].click()


    def find_buttons(self, button_text): # Should find buttons


        buttons = self.driver.find_elements_by_xpath("//*[text()='{}']".format(button_text))

        return buttons


if __name__ == '__main__':

    config_file_path = './config.ini' 
    logger_file_path = './bot.log'
    config = init_config(config_file_path)

    bot = InstaBot()
    bot.login()
#   bot.follow_user('instagram')
    bot.like_latest_posts('postmalone', 2, like=True)
  