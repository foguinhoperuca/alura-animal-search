from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AnimalsTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\chrome_webdriver\\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_search_animal(self):
        """Testing if a user can find an animal in search screen"""
        home_page = self.browser.get(self.live_server_url + '/') # FIXME doesn't return anything
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Animal Search', brand_element.text)
