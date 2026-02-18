import time
import pytest
#import pytest_soft_asserts
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
    #invalid_xpath = "//button[@class='btn btn-default btn-lg']"
    invalid_xpath = "//button[@class='btn btn-default btn-lgx']" #look at the xpath differences
    expected_title = "Your Store1" #purposely given wrong title Your Store
    actual_title = driver.title
    soft_assertions = []
    try:
        #WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located(By.XPATH,invalid_xpath))
        assert actual_title.__eq__(expected_title)
    except NoSuchElementException:
        soft_assertions.append(f"Element with XPATH '{invalid_xpath}' not found (No Such Element)")
    except TimeoutException:
        soft_assertions.append(f"Element with XPATH '{invalid_xpath}' not found (Timeout)")
    except AssertionError as e:
        soft_assertions.append(str(e))

    if soft_assertions: #list has some elements, len of list > 0
        print("soft assertions failed:")
        for failure in soft_assertions:
            print("USER DEFINED FAILURE: " ,failure)


    print("The program is ended**")

    # driver.find_element(By.NAME,"search").send_keys("HP")
    # print("HP is typed in the search box")
    # driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    # print("Button was able to find")
    # assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    # print("HP is clicked")


