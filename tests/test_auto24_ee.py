import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.MainPage_PreWork import MainPagePreWork
from pages.detail_search_page import DetailSearchPage
from pages.search_results_page import SearchResultsPage
from variables import way_from_webdriver


def test_select_product():
    driver = webdriver.Chrome(service=Service(way_from_webdriver))
    print('Начало теста')

    main_page_pre_work = MainPagePreWork(driver)
    main_page_pre_work.localisation()

    detail_search_page = DetailSearchPage(driver)
    detail_search_page.setting_detailed_search_parameters()

    search_results_page = SearchResultsPage(driver)
    search_results_page.check_results_of_search()
    time.sleep(1)
    driver.quit()
