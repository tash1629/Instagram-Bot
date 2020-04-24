from selenium import webdriver
import os
import time
import configparser

class InstagramBot:
    def __init__(self, username, password):
        """
        Initializes an instancce of the InstagramBot class.
        Args:
            username: str: The Instagram username for a user
            password: str: The Instagram password for a user

        Attributes:
            druver: Selenium.webdriver.Chrome: The Chrome driver that is used to automate the bot

        """

        # pass and username are required
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com/"

        # fires up chrome and goes to login page
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.login()
        

    def login(self):
        self.driver.get(self.base_url)

        time.sleep(1) # giving time for website to load
        
        #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        
        # getting the first elem of the list returned--> returns the first text that says Log In from all texts inside div
        # To check how many texts contain 'Log In', inspect the page and ctrl-F 'Log In'or the class name of Log In
        # You might see there is more than one text that says 'Log In', and hence we only return the first one: [0]
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        time.sleep(2) # time to let login authentication

    def nav_user(self, user):
        """
        Args:
            user:str: The username of the instagram user
        Navigate to the users page
        """

        self.driver.get('{}{}'.format(self.base_url, user))

    def follow_user(self, user):
        """
        Args:
            user:str: The username of the Instagram user
        Follow a user    

        """
        self.nav_user(user)
        time.sleep(1)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        follow_button.click()

    def unfollow_user(self, user):
        """
        Args:
            user:str: The username of the Instagram user
        Follow a user    

        """

        self.nav_user(user)
        time.sleep(1)
        unfollow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]")
        unfollow_button.click()


if __name__ == '__main__':
    
    #ig_bot.nav_user('liampayne')       
    config_path = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config_path)
    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']

    ig_bot = InstagramBot(username, password) 
    ig_bot.follow_user('liampayne')