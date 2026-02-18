import pytest_check as check

def test_soft_assertion(driver):
    driver.get("https://example.com")

    check.equal(driver.title, "Wrong Title")  # Will fail but continue
    check.is_true(driver.find_element("id", "login").is_displayed())

    print("This line WILL run even if above checks fail.")
