import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class SearchResultsPage(Base):
    """ Класс содержащий локаторы и методы для страницы представления результатов поиска """
    from variables import years_old_min, years_old_max, price_min, price_max, transmission_type, ads_on_page

    # --------------------------------------------------
    """---- Locators and variables ----"""
    right_word_detail_search = 'Результаты поиска - Объявл. автомобилей - auto24.ee'
    ads_on_page_locator = '//div[contains(@class, "result-row")]/div[@class="description"]'
    years_old_locator = '/div[@class="extra"]/span[@class="year"]'
    price_locator = '/div[@class="finance"]/span[@class="pv"]/span[@class="price"]'
    transmission_locator = '/div[@class="extra"]/span[@class="transmission sm-none"]'
    all_ads_in_search = '(//span[@class="label"]/strong)[2]'
    button_next_locator = '//div[contains(@class, "btns-pages")]/button[contains(@class, "btn-right")]'
    button_next_locator2 = '//div[@class="paginator__next"]'  # //a[@rel="next"]'
    aa = '//div[@class="bs-modules list-top-panel"]'
    # --------------------------------------------------
    """---- Getters ----"""

    def get_data_on_selected_ads(self):
        # Находим общее количество объявлений и страниц.
        time.sleep(2)
        v = self.driver.find_element(By.XPATH, self.aa).text
        vv = v.splitlines()
        if len(vv) >= 4 and '/' in vv[3]:
            # Случай 1. строка содержит информацию о количестве объявлений и страницах
            vvv = vv[3].split()
            search_data = [int(vvv[1])]  # Количество объявлений
            pages_info = vvv[2][:-1].split('/')
            search_data.append(int(pages_info[1]))  # Число справа от "/"
            # print(f'Вариант 1 ______ {search_data}')
            return search_data
        else:
            # Случай 2. строка содержит только количество объявлений
            vvv = vv[3].split()
            # print(vvv)
            search_data = [int(vvv[1]), 1]  # Количество объявлений
            # print(f'Вариант 2 ______ {search_data}')
            return search_data

    def get_len_ads_on_page(self):
        # Возвращаем количество найденных объявлений на странице
        return len(self.driver.find_elements(By.XPATH, self.ads_on_page_locator))

    def get_car_years_old(self, i=1):
        # Возвращаем год выпуска
        locator = f"({self.ads_on_page_locator})[{str(i)}]{self.years_old_locator}"
        return self.driver.find_element(By.XPATH, locator).text

    def get_car_price(self, i):
        # Возвращаем цену авто
        locator = f"({self.ads_on_page_locator})[{str(i)}]{self.price_locator}"
        return self.driver.find_element(By.XPATH, locator).text.replace("€", "")

    def get_transmission(self, i):
        # Возвращаем тип коробки передач
        locator = f"({self.ads_on_page_locator})[{str(i)}]{self.transmission_locator}"
        return self.driver.find_element(By.XPATH, locator).text.lower()

    def get_quantity_ads_in_search(self):
        # Возвращаем общее число найденных объявлений
        locator = self.all_ads_in_search
        quantity = int(self.driver.find_element(By.XPATH, locator).text)
        # print(f"Общее количество найденных объявлений {quantity}")
        return quantity

    def get_button_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_next_locator)))

    # --------------------------------------------------
    """---- Actions ----"""

    def check_len_ads_on_page(self):
        # Проверяем количество объявлений на странице на соответствие выбранному параметру
        quantity = self.get_quantity_ads_in_search()
        assert quantity == self.ads_on_page, (
            f"Количество найденных объявлений на странице ({quantity}) не соответствует заданному диапазону,")
        print(f"Количество найденных объявлений на странице  <= {quantity} - ОК")

    def check_ads_on_page(self):
        # Проверяем количество объявлений на странице
        ads = self.get_len_ads_on_page()
        assert ads <= self.ads_on_page, (f"Количество объявлений на странице ({ads}), что не соответствует заданному "
                                         f"диапазону,")
        print(f"Количество объявлений на странице ({ads})- ОК")
        return ads

    def check_type_transmission(self, i):
        # Проверяем тип коробки передач
        transmission = self.get_transmission(i).lower()
        assert transmission == self.transmission_type.lower(), (
            f"Тип коробки передач ({transmission}) не соответствует заданному диапазону,")
        print(f"Тип коробки передач ({transmission})- ОК")

    def check_price(self, i):
        # Проверяем цену авто
        price = int(self.get_car_price(i))
        year_min = int(self.price_min)
        year_max = int(self.price_max)
        assert year_min <= price <= year_max, f"Цена авто ({price}) не соответствует заданному диапазону,"
        print(f"Цена авто ({price})- ОК")

    def check_years_old(self, i=1):
        # Проверяем год выпуска
        year = int(self.get_car_years_old(i))
        year_min = int(self.years_old_min)
        year_max = int(self.years_old_max)
        assert year_min <= year <= year_max, f"Год выпуска ({year}) не соответствует заданному диапазону,"
        print(f"Год выпуска ({year})- ОК")

    def click_next_page(self):
        # Нажимаем на кнопку ">>" вверху страницы
        self.get_button_next().click()

    # --------------------------------------------------
    """---- Methods ----"""

    def check_ads(self, k=0):  # k - поправочный коэффициент. Реальная нумерация
        # проверяем объявления на подгруженной странице.
        time.sleep(1)
        b = self.check_ads_on_page() + 1
        for i in range(1, b):  # ads_on_page - количество объявлений на странице
            print(f"_____Number__{i + k}_____")
            self.check_years_old(i)  # Проверяем год выпуска
            self.check_price(i)  # Проверяем цену авто
            self.check_type_transmission(i)  # Проверяем тип коробки передач
        time.sleep(1)

    def check_results_of_search(self):
        #   Проверяем все отсортированные объявления.
        self.assert_word(self.right_word_detail_search, self.get_current_title())
        a = self.get_data_on_selected_ads()
        print("+++++++++++++++++")
        print(f'Всего найдено {a[0]} объявлений на {a[1]} страницах')
        print()
        for page in range(a[1]):
            print(f"страница номер {page + 1}")
            time.sleep(2)
            k = page * self.ads_on_page
            self.check_ads(k)
            page < a[1] - 1 and self.click_next_page()
            print()
