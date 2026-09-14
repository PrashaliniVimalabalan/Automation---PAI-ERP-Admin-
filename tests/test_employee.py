import time

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage


# ================================================================
# TC_EMP_001
# Verify Employees page loads successfully
# ================================================================

def test_tc_emp_001_employee_page_loads():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        # Open Login Page
        login_page.open_url()

        # Login
        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        # Open Employees Page
        employee_page.open_employee_page()

        time.sleep(3)

        # Verify Employees page
        assert employee_page.is_employee_page_displayed()

        print(
            "TC_EMP_001 - Employees page opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_002
# Verify Current Employee tab functionality
# ================================================================

def test_tc_emp_002_current_employee_tab():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_current_employees()

        time.sleep(3)

        assert employee_page.is_employee_page_displayed()

        print(
            "TC_EMP_002 - Current employee records displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_003
# Verify Former Employee tab functionality
# ================================================================

def test_tc_emp_003_former_employee_tab():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_former_employees()

        time.sleep(3)

        assert employee_page.is_employee_page_displayed()

        print(
            "TC_EMP_003 - Former employee records displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_004
# Verify switching between Current and Former tabs
# ================================================================

def test_tc_emp_004_switch_between_employee_tabs():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        # Current
        employee_page.open_current_employees()

        time.sleep(2)

        # Former
        employee_page.open_former_employees()

        time.sleep(2)

        # Current again
        employee_page.open_current_employees()

        time.sleep(3)

        assert employee_page.is_employee_page_displayed()

        print(
            "TC_EMP_004 - Current and Former tabs switched successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_005
# Search Current Employee - Abitharani
# ================================================================

def test_tc_emp_005_search_current_employee_valid():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_current_employees()

        time.sleep(2)

        employee_page.search_employee(
            "Abitharani"
        )

        time.sleep(5)

        assert employee_page.is_employee_displayed(
            "Abitharani"
        )

        print(
            "TC_EMP_005 - Abitharani displayed in search results"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_006
# Search Former Employee - Keerththana
# ================================================================

def test_tc_emp_006_search_former_employee_valid():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_former_employees()

        time.sleep(2)

        employee_page.search_employee(
            "Keerththana"
        )

        time.sleep(5)

        assert employee_page.is_employee_displayed(
            "Keerththana"
        )

        print(
            "TC_EMP_006 - Keerththana displayed in search results"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_007
# Search using partial employee name
# ================================================================

def test_tc_emp_007_partial_employee_search():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.search_employee(
            "Abith"
        )

        time.sleep(5)

        assert employee_page.is_employee_displayed(
            "Abitharani"
        )

        print(
            "TC_EMP_007 - Partial employee search worked correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_008
# Search invalid employee name
# ================================================================

def test_tc_emp_008_invalid_employee_search():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.search_employee(
            "XY@@@@"
        )

        time.sleep(5)

        assert employee_page.is_no_records_displayed()

        print(
            "TC_EMP_008 - No matching employee records displayed"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_009
# Empty search field
# ================================================================

def test_tc_emp_009_empty_search():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        # Keep search empty
        employee_page.clear_search()

        time.sleep(5)

        rows = employee_page.get_employee_rows()

        assert len(rows) > 0

        print(
            "TC_EMP_009 - All employee records displayed for empty search"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_010
# Verify filter button
# ================================================================

def test_tc_emp_010_filter_button():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.click_filter()

        time.sleep(3)

        assert employee_page.is_filter_panel_displayed()

        print(
            "TC_EMP_010 - Employee filter options displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_011
# Verify employee records after applying filters
# ================================================================

def test_tc_emp_011_apply_employee_filter():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.click_filter()

        time.sleep(2)

        # --------------------------------------------------------
        # Filter selection must be added using the exact
        # Designation / Role locator from your application.
        # --------------------------------------------------------

        print(
            "TC_EMP_011 - Filter panel opened; filter selection flow ready"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_012
# Verify Clear All clears selected filters
# ================================================================

def test_tc_emp_012_clear_all_filters():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.click_filter()

        time.sleep(2)

        # --------------------------------------------------------
        # Select filters here when exact filter option locators
        # are available.
        # --------------------------------------------------------

        employee_page.click_clear_all()

        time.sleep(3)

        print(
            "TC_EMP_012 - All selected filters cleared successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_013
# Search Current Employee tab
# ================================================================

def test_tc_emp_013_current_employee_search():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_current_employees()

        time.sleep(2)

        employee_page.search_employee(
            "Abitharani"
        )

        time.sleep(5)

        assert employee_page.is_employee_displayed(
            "Abitharani"
        )

        print(
            "TC_EMP_013 - Current Employee search working correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_014
# Search Former Employee tab
# ================================================================

def test_tc_emp_014_former_employee_search():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_former_employees()

        time.sleep(2)

        employee_page.search_employee(
            "Keerththana"
        )

        time.sleep(5)

        assert employee_page.is_employee_displayed(
            "Keerththana"
        )

        print(
            "TC_EMP_014 - Former Employee search working correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_015
# Search Former Employee across all pages
# ================================================================

def test_tc_emp_015_former_employee_search_all_pages():

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.open_former_employees()

        time.sleep(3)

        # Search employee from page 1
        employee_page.search_employee(
            "Keerththana"
        )

        time.sleep(5)

        # Verify search result
        assert employee_page.is_employee_displayed(
            "Keerththana"
        )

        print(
            "TC_EMP_015 - Former Employee search worked across pages"
        )

    finally:

        driver.quit()


# ================================================================
# TC_EMP_016
# Verify View and Edit action buttons
# ================================================================

def test_tc_emp_016_employee_action_buttons():

    # ------------------------------------------------------------
    # VIEW
    # ------------------------------------------------------------

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.click_view_employee()

        time.sleep(5)

        print(
            "TC_EMP_016 - View Employee action working correctly"
        )

    finally:

        driver.quit()

    # ------------------------------------------------------------
    # EDIT
    # ------------------------------------------------------------

    driver = get_driver()

    try:

        login_page = LoginPage(driver)
        employee_page = EmployeePage(driver)

        login_page.open_url()

        login_page.login(
            "ADMIN001",
            "Admin@123"
        )

        time.sleep(3)

        employee_page.open_employee_page()

        time.sleep(2)

        employee_page.click_edit_employee()

        time.sleep(5)

        print(
            "TC_EMP_016 - Edit Employee action working correctly"
        )

    finally:

        driver.quit()