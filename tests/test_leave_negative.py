from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.leave_page import LeavePage


def test_search_empty_leave():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    leave_page.open_leave_page()

    leave_page.search_leave_employee(
        ""
    )

    print("Empty Search Tested")

    driver.quit()

def test_invalid_employee_search():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    leave_page.open_leave_page()

    leave_page.search_leave_employee(
        "XYZ123INVALID"
    )

    print("Invalid Employee Search Tested")

    driver.quit()

def test_special_character_search():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    leave_page.open_leave_page()

    leave_page.search_leave_employee(
        "@@@###$$$"
    )

    print("Special Character Search Tested")

    driver.quit()

