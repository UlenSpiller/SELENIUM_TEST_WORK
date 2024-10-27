import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def get_current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def get_current_title(self):
        return self.driver.find_element(By.TAG_NAME, 'title').get_attribute('innerText')

    def get_scroll(self, x=400):
        return self.driver.execute_script(f"window.scrollTo(0, {x});")

    @staticmethod
    def assert_word(right_title, check_title):
        assert right_title == check_title, (f'С совпадением заголовка проблемы: right_title ({right_title}) <> '
                                            f'check_title ({check_title})')
        print(f'Проверяемый заголовок верен.     right_title ({right_title}) == check_title ({check_title})')

    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\SELENIUM_TEST_WORK\\screens\\' + name_screenshot)
