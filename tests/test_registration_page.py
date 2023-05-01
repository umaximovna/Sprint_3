from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestRegistrationPage:
    def test_successful_registration(self, data_for_registration):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTER_PAGE_NAME_FIELD).send_keys(data_for_registration.get("name"))
        driver.find_element(*TestLocators.REGISTER_PAGE_EMAIL_FIELD).send_keys(data_for_registration.get("email"))
        driver.find_element(*TestLocators.REGISTER_PAGE_PASSWORD_FIELD).send_keys(data_for_registration.get("password"))
        driver.find_element(*TestLocators.REGISTER_PAGE_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.LOGIN_CHECK_IN_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_incorrect_password_show_error(self, data_for_incorrect_registration):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.REGISTER_PAGE_NAME_FIELD).send_keys(data_for_incorrect_registration.get("name"))
        driver.find_element(*TestLocators.REGISTER_PAGE_EMAIL_FIELD).send_keys(data_for_incorrect_registration.get("email"))
        driver.find_element(*TestLocators.REGISTER_PAGE_PASSWORD_FIELD).send_keys(data_for_incorrect_registration.get("password"))
        driver.find_element(*TestLocators.REGISTER_PAGE_REGISTER_BUTTON).click()
        message = driver.find_elements(*TestLocators.REGISTER_PAGE_PASSWORD_ERROR_MESSAGE)
        assert len(message) > 0
        driver.quit()
