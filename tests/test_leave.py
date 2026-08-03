from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
import time


# Open Leave Page Test
def test_open_leave_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Leave Page
    leave_page.open_leave_page()

    time.sleep(5)

    print("Leave Page Opened Successfully")

    driver.quit()


# Today Button Test
def test_today_button():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Leave Page
    leave_page.open_leave_page()

    # Click Today Button
    leave_page.click_today_button()

    time.sleep(5)

    print("Today Button Working Successfully")

    driver.quit()


# Week Button Test
def test_week_button():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Leave Page
    leave_page.open_leave_page()

    # Click Week Button
    leave_page.click_week_button()

    time.sleep(5)

    print("Week Button Working Successfully")

    driver.quit()


# Search Leave Employee Test
def test_search_leave_employee():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Leave Page
    leave_page.open_leave_page()

    # Search Employee
    leave_page.search_leave_employee("Affath")

    time.sleep(5)

    print("Leave Search Working Successfully")

    driver.quit()