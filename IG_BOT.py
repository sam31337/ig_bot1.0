from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
import time

class IGbot:
    username = 'username' #put real IG acc username
    password = 'password' #put real IG acc password

    hashtags = [
        'hashtag1', 'hashtag2', 'hashtag3',     #put (niche)targeting hashtags
    ]

    comments = [
        'comment1', 'comment2', 'comment3',      #add more or edit available comments
    ]

    links = []

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.login()
        self.process()

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(4)

        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(2)

        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(2)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(5)

    def process(self):
        self.top_posts()
        self.execute()
        self.finalize()

    def top_posts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
            time.sleep(3)

            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range(10, 15):                                                          
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(2)

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            
            self.comment()
            time.sleep(3)

            self.follow()
            time.sleep(3)
            
            self.like()
            sleeptime = random.randint(20, 35)                                                 
            time.sleep(sleeptime)

    def comment(self):
        comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
        comment_input().click()
        comment_input().clear()
            
        comment = random.choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = random.randint(1, 7) / 30
            time.sleep(delay)
        
        comment_input().send_keys(Keys.RETURN)
    
    def follow(self):
            follow_button = lambda: self.browser.find_element_by_xpath('//button[@class="oW_lN _0mzm- sqdOP yWX7d        "]')
            follow_button().click()
            time.sleep(5)

    def like(self):
        like_button = lambda: self.browser.find_element_by_xpath('//span[@class="glyphsSpriteHeart__outline__24__grey_9 u-__7"]')
        like_button().click()

    def finalize(self):
        self.browser.close()
        sys.exit()

igbot = IGbot()