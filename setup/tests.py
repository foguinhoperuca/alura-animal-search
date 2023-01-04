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

        # Vini would like to find a new animal for him

        # He finds our website (Animal Search) go for it
        home_page = self.browser.get(self.live_server_url + '/')  # FIXME doesn't return anything

        # 'Cause he sees "Animal Search" wrote in menu
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Animal Search', brand_element.text)

        # Also he sees a field to search for animals by name
        search_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#search-animal')
        self.assertEqual(search_animal_input.get_attribute('placeholder'), 'Eg.: lion, bear, dog, cat, etc...')
        sleep(5)

        # So, he searches for Lion and click in button "search"
        search_animal_input.send_keys('Lion')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # # Then, the site show 4 features of animal
        feat = self.browser.find_element(By.CSS_SELECTOR, '.result-description')

        # And, of course, Vini gave up with Lion
