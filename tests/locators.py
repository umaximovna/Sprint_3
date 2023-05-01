from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLocators:
    # локаторы на странице конструктора /
    SING_IN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    DESIGN_ORDER_BUTTON = "//button[text()='Оформить заказ']"
    LOAFS_SECTION = By.XPATH, ".//span[text()='Булки']"
    SOUSES_SECTION = By.XPATH, ".//span[text()='Соусы']"
    FILLINGS_SECTION = By.XPATH, ".//span[text()='Начинки']"
    LOAFS_SECTION_IS_CURRENT = By.XPATH, ".//div[contains( @class , 'tab_tab_type_current__2BEPc') " \
                                         "and contains(.//span,'Булки')]"
    SOUSES_SECTION_IS_CURRENT = By.XPATH, ".//div[contains( @class , 'tab_tab_type_current__2BEPc') " \
                                          "and contains(.//span,'Соусы')]"
    FILLINGS_SECTION_IS_CURRENT = By.XPATH, ".//div[contains( @class , 'tab_tab_type_current__2BEPc') " \
                                            "and contains(.//span,'Начинки')]"

    # локаторы на странице регистрации /register
    REGISTER_PAGE_NAME_FIELD = By.XPATH,  ".//label[text()='Имя']/following-sibling::input"
    REGISTER_PAGE_EMAIL_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input"
    REGISTER_PAGE_PASSWORD_FIELD = By.XPATH,  ".//label[text()='Пароль']/following-sibling::input"
    REGISTER_PAGE_REGISTER_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"
    REGISTER_PAGE_PASSWORD_ERROR_MESSAGE = By.CLASS_NAME, "input__error"
    REGISTER_PAGE_RECENTLY_REGISTERED_LOGIN_BUTTON = By.XPATH, ".//a[text()='Войти']"

    # локаторы на странице входа /login
    LOGIN_CHECK_IN_BUTTON = "//button[text()='Войти']"
    LOGIN_EMAIL_FIELD = By.XPATH, ".//label[text()='Email']/following-sibling::input"
    LOGIN_PASSWORD_FIELD = By.XPATH, ".//label[text()='Пароль']/following-sibling::input"
    LOGIN_PAGE_FORGOT_YOUR_PASSWORD_QUESTION = ".//p[text()='Забыли пароль?']"
    ATTRIBUTE_IN_LOGIN_PAGE = By.CLASS_NAME, "input__icon"

    # локаторы на странице восстановления пароля /forgot-password
    REMEMBER_PASSWORD_LOGIN_BUTTON = By.XPATH, ".//a[text()='Войти']"

    # локаторы в шапке страницы
    COMMON_PERSONAL_CABINET_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    COMMON_CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"
    COMMON_LOGO = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"

    # локаторы в личном кабинете /account/profile
    MESSAGE_IN_PROFILE_PAGE = ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"
    EXIT_FROM_PERSONAL_CABINET_BUTTON = By.XPATH, "//button[text()='Выход']"








