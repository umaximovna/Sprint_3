from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


class TestLogoutPage:
    def test_logout_from_personal_cabinet(self, data_of_existing_user):
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
        driver.find_element(*TestLocators.EXIT_FROM_PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, TestLocators.LOGIN_PAGE_FORGOT_YOUR_PASSWORD_QUESTION)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()