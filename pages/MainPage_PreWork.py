from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPagePreWork(Base):
    """ Класс содержащий локаторы и методы для настройки локализации главной страницы """

    url = "https://www.auto24.ee"  # url тестируемого сайта

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators and another
    right_word = 'Главная - auto24.ee'
    cookies_bar = '//button[@id="onetrust-reject-all-handler"]'
    language_ddm = "lang_bar"
    select_language = '//a[@href="/session.php?l=rus"]'

    # Getters
    def get_cookies_bar(self):
        # return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookies_bar)))
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookies_bar)))

    def get_language_ddm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.language_ddm)))

    def get_select_language(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_language)))

    # Actions
    def click_cookies_bar(self):
        self.get_cookies_bar().click()

    def click_language_ddm(self):
        self.get_language_ddm().click()

    def click_select_language(self):
        self.get_select_language().click()

    # Methods
    def localisation(self):
        self.driver.get(self.url)  # открытие url
        self.driver.maximize_window()
        self.click_cookies_bar()
        self.click_language_ddm()
        self.click_select_language()
        self.assert_word(self.right_word, self.get_current_title())
        # self.screenshot()
