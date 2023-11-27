# Create your tests here.
# Link to locating elements: https://selenium-python.readthedocs.io/locating-elements.html

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class Hosttest(LiveServerTestCase):
    def testhomePage(self):

        driver = webdriver.Chrome()
        driver.get('http://localhost:8000/')

        time.sleep(3)

        assert 'Geology Outcrop Finder' in driver.title

class CreateAccountTest(LiveServerTestCase):
    def testCreateForm(self):
        driver = webdriver.Chrome()
        driver.get('http://localhost:8000/create_Account/')
        time.sleep(3)

    
        user_name = driver.find_element(By.NAME,'username')
        user_password = driver.find_element(By.NAME,'password1')
        user_email = driver.find_element(By.NAME,'email')
        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
        user_password_confirmation = driver.find_element(By.NAME,'password2')

        user_name.send_keys('Sarah_Connor')
        user_email.send_keys('SarahConnor@gmail.com')
        user_password.send_keys('SarahTime1')
        user_password_confirmation.send_keys('SarahTime1')

        submit.send_keys(Keys.RETURN)

        assert 'Geological Formations around Colorado!!' in driver.page_source

class LoginFormTest(LiveServerTestCase):
    def testform(self):

        driver = webdriver.Chrome()
        driver.get('http://localhost:8000/login/')
        time.sleep(3)

        user_name = driver.find_element(By.NAME,'username')
        user_password = driver.find_element(By.NAME,'password')
        submit = driver.find_element(By.XPATH, '//button[@type="submit"]')

        user_name.send_keys('Sarah_Connor')
        user_password.send_keys('SarahTime1')

        submit.send_keys(Keys.RETURN)

        assert 'Geological Formations around Colorado!!' in driver.page_source


class OpenFormationTest(LiveServerTestCase):
    def testOpenForm(self):

        driver = webdriver.Chrome()
        driver.get('http://localhost:8000/portfolio/1')
        time.sleep(3)

        assert 'Geology Outcrop Finder' in driver.title