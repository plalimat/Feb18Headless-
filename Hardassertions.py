import time
import pytest
import pytest_soft_asserts
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def test_tutorials_ninga():
    driver = webdriver.Chrome()

    driver.maximize_window();
    # Load first website
    print("Loading the website now")
    #driver.implicitly_wait(10)
    #driver.get("https://omayo.blogspot.com/")
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(5)
    expected_title = "Your Store12" #purposely given wrong title Your Store
    actual_title = driver.title
    assert actual_title.__eq__(expected_title), f"I Am in wrong URL -Your Store12 "

    driver.find_element(By.NAME,"search").send_keys("HP")
    time.sleep(5)
    print("HP is typed in the search box")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    print("Button was able to find")
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    print("HP is clicked")


