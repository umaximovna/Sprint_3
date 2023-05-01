from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestPersonalCabinet:

    def test_click_to_personal_cabinet_button_before_login_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 15)
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_click_to_personal_cabinet_button_before_login_from_login_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_click_to_personal_cabinet_button_after_login(self, data_of_existing_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.MESSAGE_IN_PROFILE_PAGE)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    def test_to_constructor_page_from_personal_cabinet_by_button(self, data_of_existing_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestLocators.COMMON_CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_to_constructor_page_from_personal_cabinet_by_logo(self, data_of_existing_user): #доделать
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestLocators.COMMON_LOGO).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

