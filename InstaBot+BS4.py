from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.common.exceptions import NoSuchElementException
from random import randint
from pynput.keyboard import Key, Controller as KeyboardController #this is only going to work if you are using one single screen (this is a bad idea), but
#instagram blocks some of the operations like ex. trying to send keys using webdriver. 

keyboard = KeyboardController()

comments = [u'Looks nice mate :)',
            u'Keep posting pics like this! <3 :)',
            u'Good. I like this <3',
            u'Nice pic mate :)',
            u'I like your profile. Always something interesting <3 :)',
            u'Hmm, interesting stuff :)',
            u'Nice profile! Always good posts :)',
            u'Nice stuff mate :)',
            u'Good job! :)',
            u'Like your posts. Can find many interesting things here :)',
            u'Learning from you :)',
            u'Good. I like this pic :)',
            u'Keep posting stuff like this!'
            ]


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Piotrek\Desktop\geckodriver\geckodriver') #full path to your geckodriver

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        user_name_elem = driver.find_element_by_name("username")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        time.sleep(4)
        password_elem = driver.find_element_by_name("password")
        password_elem.clear()
        password_elem.send_keys(self.password)
        time.sleep(1)
        password_elem.send_keys(Keys.ENTER)
        time.sleep(5)

    def user_to_follow(self, x, number_to_follow):
        follow_counter = 0
        self.driver.get('https://www.instagram.com/' + x)
        # I am at a profile page
        self.driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(randint(4, 7))
        num = 1
        while follow_counter <= number_to_follow:
            temp = '/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(num)
            temp_alternative = '/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(num)
            # Instagram changes the structure of their website. One of these temps will work.
            try:
                temp_elem = self.driver.find_element_by_xpath(temp)
            except NoSuchElementException:
                temp_elem = self.driver.find_element_by_xpath(temp_alternative)

            time.sleep(random.randint(1, 2))
            temp_text = temp_elem.text
            try:
                if temp_text == 'Obserwuj':
                    temp_elem.click()
                    time.sleep(randint(1, 3))
                    follow_counter += 1
                    num += 1
                else:
                    time.sleep(randint(1, 3))
                    num += 1
                    continue
            except NoSuchElementException:
                if temp_text == 'Obserwuj':
                    temp_elem.click()
                    time.sleep(randint(1, 3))
                    follow_counter += 1
                    num += 1
                else:
                    time.sleep(randint(1, 3))
                    num += 1
                    continue


        print('Users followed: ' + str(follow_counter))

    def like_and_comment_hashtags(self, hashtag, number):
        def chill(): #chill has been created to show instagram, that we operate not like a bot
            time.sleep(randint(2, 4))
        i = 0
        number_of_likes_and_comments = number
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag)
        time.sleep(randint(20, 60))
        chill()
        comments = [u'Looks nice mate :)',
                    u'Keep posting pics like this! <3 :)',
                    u'Good. I like this <3',
                    u'Nice pic mate :)',
                    u'I like your profile. Always something interesting <3 :)',
                    u'Hmm, interesting stuff :)',
                    u'Nice profile! Always good posts :)',
                    u'Nice stuff mate :)',
                    u'Good job! :)',
                    u'Like your posts. Can find many interesting things here :)',
                    u'Learning from you :)',
                    u'Good. I like this pic :)',
                    u'Keep posting stuff like this!'
                    ]

        cols_counter = 1
        rows_counter = 1
        hashtags_commented_and_liked = 0
        for nums in range(0, number_of_likes_and_comments):
            driver.find_element_by_xpath(
                '/html/body/span/section/main/article/div[2]/div/div[{}]/div[{}]/a/div'.format(rows_counter,
                                                                                               cols_counter)).click()
            chill()
            # Clicking like button
            driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span").click()
            chill()
            # heading to comment section
            try:
                comment_section_area = driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                chill()
                comment_section_area.click()
                chill()
                keyboard.type(comments[randint(0, 12)])
                chill()
                chill()
                chill()
                publish_button = driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/button')
                publish_button.click()
                chill()
                chill()
                quit_photo = driver.find_element_by_xpath('/html/body/div[3]/button[1]')
                quit_photo.click()
                chill()
                chill()
                time.sleep(randint(60, 120))
                hashtags_commented_and_liked += 1

            except NoSuchElementException:
                quit_photo = driver.find_element_by_xpath('/html/body/div[3]/button[1]')
                quit_photo.click()

            if cols_counter == 3:
                rows_counter += 1
                cols_counter = 1
                print(cols_counter)
            else:
                cols_counter += 1
                print(cols_counter)
        print('Number of hashtags liked and commented: ' + str(hashtags_commented_and_liked))

    def like_your_feed(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(randint(4, 7))
        for nums in range(1, 5):
            driver.find_element_by_xpath(
                '/html/body/span/section/main/section/div[1]/div[1]/div/article[{}]/div[2]/section[1]/span[1]/button/span'.format(
                    nums)).click()
            time.sleep(randint(5, 8))




bot = InstagramBot('', '')
bot.login()
time.sleep(5)
bot.user_to_follow('', 18)


