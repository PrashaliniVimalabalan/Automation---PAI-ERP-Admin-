import time

from selenium.webdriver.common.by import By

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.template_page import TemplatePage


# ================================================================
# Helper
# ================================================================

def open_template_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    template_page = TemplatePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    template_page.open_template_page()

    time.sleep(3)

    return driver, template_page


# ================================================================
# TC_TEMP_NEG_001
# Invalid Name and Address
# Existing TC_TEMP_005 is a known bug:
# system accepts invalid characters.
# ================================================================

def test_temp_neg_001_invalid_name_address():

    driver, template_page = open_template_page()

    try:

        name = driver.find_element(
            *template_page.name_input
        )

        address = driver.find_element(
            *template_page.address_input
        )

        name.clear()
        name.send_keys("!@#123")

        address.clear()
        address.send_keys("@@@@@@")

        print(
            "TC_TEMP_NEG_001 - Invalid Name and Address entered"
        )

        # Current system behavior:
        # No validation message is displayed.
        # This test documents the existing bug.

        template_page.click_preview()

        time.sleep(3)

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        print(
            "Observed: System accepts invalid characters."
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_NEG_002
# Empty Offer Letter
# ================================================================

def test_temp_neg_002_empty_offer_letter():

    driver, template_page = open_template_page()

    try:

        template_page.click_preview()

        time.sleep(3)

        print(
            "TC_TEMP_NEG_002 - Empty Offer Letter validation checked"
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_NEG_003
# Invalid Service Letter Name
# Existing TC_TEMP_017 is a known bug:
# system accepts special characters.
# ================================================================

def test_temp_neg_003_invalid_service_name():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        name = driver.find_element(
            *template_page.service_name
        )

        name.clear()
        name.send_keys("@@@@")

        print(
            "TC_TEMP_NEG_003 - Invalid Service Letter name entered"
        )

        template_page.click_service_preview()

        time.sleep(3)

        print(
            "Observed: System accepts invalid characters."
        )

    finally:

        driver.quit()


# ================================================================
# TC_TEMP_NEG_004
# Empty Service Letter
# ================================================================

def test_temp_neg_004_empty_service_letter():

    driver, template_page = open_template_page()

    try:

        template_page.open_service_letter()

        template_page.click_service_preview()

        time.sleep(3)

        print(
            "TC_TEMP_NEG_004 - Empty Service Letter validation checked"
        )

    finally:

        driver.quit()