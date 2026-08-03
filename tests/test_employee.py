from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
import time


# Search Employee Test
def test_search_employee():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employees Page
    employee_page.open_employee_page()

    # Search Employee
    employee_page.search_employee("Afri")

    time.sleep(5)

    print("Employee Search Successful")

    driver.quit()


# View Employee Test
def test_view_employee():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employees Page
    employee_page.open_employee_page()

    # Click View Employee
    employee_page.click_view_employee()

    time.sleep(5)

    print("Employee View Opened Successfully")

    driver.quit()


# Edit Employee Test
def test_edit_employee():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employees Page
    employee_page.open_employee_page()

    # Click Edit Employee
    employee_page.click_edit_employee()

    time.sleep(5)

    print("Employee Edit Page Opened Successfully")

    driver.quit()


# Former Employee Tab Test
def test_former_employee_tab():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employees Page
    employee_page.open_employee_page()

    # Open Former Employees
    employee_page.open_former_employees()

    time.sleep(5)

    print("Former Employee Tab Opened Successfully")

    driver.quit()


# Current Employee Tab Test
def test_current_employee_tab():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employees Page
    employee_page.open_employee_page()

    # Open Current Employees
    employee_page.open_current_employees()

    time.sleep(5)

    print("Current Employee Tab Opened Successfully")

    driver.quit()


# New Employee Button Test
def test_new_employee_button():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login("ADMIN001", "Admin@123")

    # Open Employees Page
    employee_page.open_employee_page()

    # Click New Employee Button
    employee_page.click_new_employee()

    time.sleep(5)

    print("New Employee Page Opened Successfully")

    driver.quit()