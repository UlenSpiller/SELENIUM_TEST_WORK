import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.keys import Keys


class DetailSearchPage(Base):
    from variables import years_old_min, years_old_max, price_min, price_max, transmission_type, crashed_type, \
        location_for_check, ads_on_page, edge_notification
    """ Класс содержащий локаторы и методы для страницы детального поиска """

    # --------------------------------------------------
    """---- Locators and variables ----"""
    right_word_detail_search = 'Объявл. автомобилей - auto24.ee'
    transmission_type_locator = '(//div[@class="a24-custom-select"])[11]'
    crashed_type_locator = '(//div[@class="a24-custom-select"])[13]'
    detail_search = '//a[@id="detailSearchLink"]'
    location_locator = '(//div[@class="a24-custom-select"])[15]'
    location_selection_input_field_locator = '//div[@id="item-searchParam-location"]/div/div/div[1]/span[2]'
    edge_notification_ddm_locator = '(//div[@class="a24-custom-select"])[20]'
    button_search_name = "otsi"

    # --------------------------------------------------
    """---- Getters ----"""
    def get_detail_search(self):
        # Возвращаем элемент "детал. поиск"
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.detail_search)))

    def get_years_old_min(self):
        #   Возвращаем поле ввода нижней границы года выпуска
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "f1")))

    def get_years_old_max(self):
        #   Возвращаем поле ввода верхней границы года выпуска
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "f2")))

    def get_price_min(self):
        #   Возвращаем поле ввода нижней границы цены
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "g1")))

    def get_price_max(self):
        #   Возвращаем поле ввода верхней границы цены
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "g2")))

    def get_transmission_type(self):
        #   Возвращаем дроп даун меню с типом коробки передач
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.transmission_type_locator)))

    def get_crashed_type(self):
        #   Возвращаем дроп даун меню аварийная / не аварийная
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.crashed_type_locator)))

    def get_location(self):
        #   Возвращаем дроп даун меню выбора места локации
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.location_locator)))

    def get_on_page_ddm(self):
        #   Возвращаем дроп даун меню выбора количества объявлений на странице
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "item-searchParam-showing")))

    def get_edge_notification_ddm(self):
        # Возвращаем дроп даун меню выбора возраста объявлений
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                   self.edge_notification_ddm_locator)))

    def get_button_search(self):
        # Возвращаем элемент кнопки "поиск"
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.NAME,
                                                                                    self.button_search_name)))

    # --------------------------------------------------
    """---- Actions ----"""
    def click_detail_search(self):
        # Нажимаем на надпись "[детал. поиск]."
        self.get_detail_search().click()

    def input_years_old_min(self):
        #   Вводим нижнюю границу поиска по году выпуска
        self.get_years_old_min().send_keys(self.years_old_min)

    def input_years_old_max(self):
        #   Вводим верхнюю границу поиска по году выпуска
        self.get_years_old_max().send_keys(self.years_old_max)

    def input_price_min(self):
        #   Вводим нижний предел цены
        self.get_price_min().send_keys(self.price_min)

    def input_price_max(self):
        #   Вводим верхний предел цены
        self.get_price_max().send_keys(self.price_max)

    def input_transmission_type(self):
        # Вводим в поле ввода тип коробки передач.
        self.actions.send_keys_to_element(self.get_transmission_type(), self.transmission_type).perform()
        self.actions.move_by_offset(0, 0).click().perform()

    def input_crashed_type(self):
        # Вводим в поле ввода тип коробки передач.
        self.actions.send_keys_to_element(self.get_crashed_type(), self.crashed_type).perform()
        self.actions.move_by_offset(0, 0).click().perform()

    def choosing_location(self):
        # Выбираем регион для поиска.
        select_ddm_location = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.location_locator)))
        select_ddm_location.click()
        time.sleep(2)

        location_selection_input_field_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.location_selection_input_field_locator)))
        location_selection_input_field_element.send_keys(self.location_for_check)
        time.sleep(1)
        location_selection_input_field_element.send_keys(Keys.ENTER)

    def number_of_notifications_per_page(self):
        # Выбираем количество объявлений на странице.
        self.actions.send_keys_to_element(self.get_on_page_ddm(), self.ads_on_page).perform()
        self.actions.move_by_offset(0, 0).click().perform()

    def choosing_edge_notification_ddm(self):
        # Выбираем возраст объявлений.
        self.actions.send_keys_to_element(self.get_edge_notification_ddm(), self.edge_notification).perform()
        self.actions.move_by_offset(0, 0).click().perform()

    def click_button_search(self):
        # Нажимаем кнопку "поиск".
        self.get_button_search().click()

    # --------------------------------------------------
    """---- Methods ----"""
    def setting_detailed_search_parameters(self):
        # Задаем параметры детального поиска
        self.get_scroll()
        time.sleep(1)
        self.click_detail_search()
        time.sleep(2)
        self.assert_word(self.right_word_detail_search, self.get_current_title())
        time.sleep(2)
        self.get_scroll()
        self.input_years_old_min()
        self.input_years_old_max()
        self.input_price_min()
        self.input_price_max()
        self.input_transmission_type()
        self.input_crashed_type()
        self.choosing_location()
        self.number_of_notifications_per_page()
        self.choosing_edge_notification_ddm()
        # self.screenshot()
        # self.get_scroll(600)
        time.sleep(5)
        self.click_button_search()
        time.sleep(3)
