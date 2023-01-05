from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class AnimalsTestCase(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\chrome_webdriver\\chromedriver.exe',
                                        options=chrome_options)

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
        search_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#search')
        self.assertEqual(search_animal_input.get_attribute('placeholder'), 'Eg.: lion, bear, dog, cat, etc...')

        # So, he searches for Lion and click in button "search"
        search_animal_input.send_keys('Lion')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        sleep(200)

        # Then, the site show 4 features of animal
        feat = self.browser.find_element(By.CSS_SELECTOR, '.result-description')
        sleep(10)
        self.assertGreater((len(feat), 3))

        # And, of course, Vini gave up with Lion
