from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestLoginPage:

    def test_redirect_to_login_page_by_sign_in_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SING_IN_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_login_by_sign_in_button(self, data_of_existing_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SING_IN_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_redirect_to_login_page_by_personal_cabinet_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_login_by_by_personal_cabinet_button(self, data_of_existing_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.COMMON_PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        WebDriverWait(driver, 10).until(
              expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_redirect_to_login_page_by_recently_registered_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTER_PAGE_RECENTLY_REGISTERED_LOGIN_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_login_by_recently_registered_button(self, data_of_existing_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTER_PAGE_RECENTLY_REGISTERED_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_redirect_to_login_page_by_remember_password_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 15)
        driver.find_element(*TestLocators.REMEMBER_PASSWORD_LOGIN_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_login_by_remember_password_button(self, data_of_existing_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 15)
        driver.find_element(*TestLocators.REMEMBER_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_EMAIL_FIELD).send_keys(data_of_existing_user.get("email"))
        driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data_of_existing_user.get("password"))
        driver.find_element(By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.DESIGN_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
