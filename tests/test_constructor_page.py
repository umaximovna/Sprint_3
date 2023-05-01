from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestConstructorPage:
    def test_turn_over_to_loafs(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10)
        driver.find_element(*TestLocators.SOUSES_SECTION).click()  # сначала выбор секции != Булки
        driver.find_element(*TestLocators.LOAFS_SECTION).click()
        assert len(driver.find_elements(*TestLocators.LOAFS_SECTION_IS_CURRENT)) > 0
        driver.quit()

    def test_turn_over_to_souses(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10)
        driver.find_element(*TestLocators.SOUSES_SECTION).click()
        assert len(driver.find_elements(*TestLocators.SOUSES_SECTION_IS_CURRENT)) > 0
        driver.quit()

    def test_turn_over_to_fillings(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10)
        driver.find_element(*TestLocators.FILLINGS_SECTION).click()
        assert len(driver.find_elements(*TestLocators.FILLINGS_SECTION_IS_CURRENT)) > 0
        driver.quit()
