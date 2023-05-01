import pytest
import random as r
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators


@pytest.fixture
def data_for_registration():
    n = r.randint(1, 100)
    m = r.randint(1, 1000)
    return {"name": 'Аделина', "email": f"anyemail{n}{m}@mail.ru", "password": f"anypassword{n}{m}"}


@pytest.fixture
def data_for_incorrect_registration():
    n = r.randint(1, 9)
    m = r.randint(1, 1000)
    return {"name": 'Аделина', "email": f"anyemail{n}{m}@mail.ru", "password": f"ab{n}"}

@pytest.fixture
def data_of_existing_user():
    return {"name": 'Иветта', "email": 'nononon@mail.ru', "password": 'lowcode1234'}


