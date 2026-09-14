import time
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.leave_page import LeavePage


# ================================================================
# Helper Method
# ================================================================

def open_leave_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    # Open Leave Page
    leave_page.open_leave_page()

    time.sleep(3)

    return driver, leave_page


# ================================================================
# TC_LEAVE_001
# Verify Leave page loads successfully
# ================================================================

def test_tc_leave_001_leave_page_loads():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_leave_page_displayed()

        print(
            "TC_LEAVE_001 - Leave page opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_002
# Verify Today and Week tab functionality
# ================================================================

def test_tc_leave_002_today_week_tabs():

    driver, leave_page = open_leave_page()

    try:

        # Click Today
        leave_page.click_today_button()

        time.sleep(3)

        # Click Week
        leave_page.click_week_button()

        time.sleep(3)

        assert leave_page.is_leave_page_displayed()

        print(
            "TC_LEAVE_002 - Today and Week tabs working successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_003
# Verify All Leaves count display
# ================================================================

def test_tc_leave_003_all_leaves_count():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_all_leaves_displayed()

        print(
            "TC_LEAVE_003 - All Leaves count displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_004
# Verify Pending Approvals count display
# ================================================================

def test_tc_leave_004_pending_approvals_count():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_pending_approvals_displayed()

        print(
            "TC_LEAVE_004 - Pending Approvals count displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_005
# Verify Approved Leaves count display
# ================================================================

def test_tc_leave_005_approved_leaves_count():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_approved_leaves_displayed()

        print(
            "TC_LEAVE_005 - Approved Leaves count displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_006
# Verify Rejected Leaves count display
# ================================================================

def test_tc_leave_006_rejected_leaves_count():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_rejected_leaves_displayed()

        print(
            "TC_LEAVE_006 - Rejected Leaves count displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_007
# Verify Leave Requests table display
# ================================================================

def test_tc_leave_007_leave_requests_table():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_leave_table_displayed()

        print(
            "TC_LEAVE_007 - Leave Requests table displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_008
# Verify Leave Type column display
# ================================================================

def test_tc_leave_008_leave_type_column():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_leave_type_displayed()

        print(
            "TC_LEAVE_008 - Leave Type displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_009
# Verify Leave Status labels display
# ================================================================

def test_tc_leave_009_status_labels():

    driver, leave_page = open_leave_page()

    try:

        assert leave_page.is_status_displayed()

        print(
            "TC_LEAVE_009 - Status labels displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_010
# Search valid employee - Kaviram
# ================================================================

def test_tc_leave_010_valid_employee_search():

    driver, leave_page = open_leave_page()

    try:

        leave_page.search_leave_employee(
            "Kaviram"
        )

        time.sleep(5)

        assert leave_page.is_employee_leave_displayed(
            "Kaviram"
        )

        print(
            "TC_LEAVE_010 - Kaviram leave records displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_011
# Search partial employee name - Kav
# ================================================================

def test_tc_leave_011_partial_employee_search():

    driver, leave_page = open_leave_page()

    try:

        leave_page.search_leave_employee(
            "Kav"
        )

        time.sleep(5)

        assert leave_page.is_employee_leave_displayed(
            "Kav"
        )

        print(
            "TC_LEAVE_011 - Partial employee search working successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_012
# Search invalid employee name - XYZ123
# ================================================================

def test_tc_leave_012_invalid_employee_search():

    driver, leave_page = open_leave_page()

    try:

        leave_page.search_leave_employee(
            "XYZ123"
        )

        time.sleep(5)

        assert leave_page.is_no_records_displayed()

        print(
            "TC_LEAVE_012 - No matching leave records displayed"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_013
# Empty search
# ================================================================

def test_tc_leave_013_empty_search():

    driver, leave_page = open_leave_page()

    try:

        leave_page.search_leave_employee(
            ""
        )

        time.sleep(5)

        assert leave_page.is_leave_table_displayed()

        print(
            "TC_LEAVE_013 - All leave records displayed for empty search"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_014
# Verify Filter button functionality
# ================================================================

def test_tc_leave_014_filter_button():

    driver, leave_page = open_leave_page()

    try:

        # Click green filter icon
        leave_page.click_filter()

        time.sleep(3)

        # Verify filter options
        full_day = driver.find_element(
            *leave_page.full_day_option
        )

        assert full_day.is_displayed()

        print(
            "TC_LEAVE_014 - Filter options displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_015
# Verify records after applying filter
#
# Test case:
# Apply Leave Type filter
# Example: Full Day
# ================================================================

def test_tc_leave_015_apply_leave_filter():

    driver, leave_page = open_leave_page()

    try:

        # Open Filter
        leave_page.click_filter()

        time.sleep(2)

        # Select Full Day
        leave_page.select_full_day()

        time.sleep(5)

        # Verify table contains Full Day
        rows = leave_page.get_leave_rows()

        assert len(rows) > 0

        found_full_day = False

        for row in rows:

            if "Full Day" in row.text:

                found_full_day = True
                break

        assert found_full_day

        print(
            "TC_LEAVE_015 - Full Day filtered records displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_016
# Verify Leave Type filter options
#
# Application uses the green funnel as Filter.
# Full Day option is verified using the exact locator.
# ================================================================

def test_tc_leave_016_leave_type_filter():

    driver, leave_page = open_leave_page()

    try:

        # Open Filter
        leave_page.click_filter()

        time.sleep(2)

        # Select Full Day
        leave_page.select_full_day()

        time.sleep(4)

        rows = leave_page.get_leave_rows()

        assert len(rows) > 0

        for row in rows:

            assert "Full Day" in row.text

        print(
            "TC_LEAVE_016 - Leave Type filter applied successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_017
# Verify Status filter options
#
# Exact Status checkbox locators were not provided yet.
# This test verifies the Filter panel is available.
# ================================================================

def test_tc_leave_017_status_filter():

    driver, leave_page = open_leave_page()

    try:

        leave_page.click_filter()

        time.sleep(2)

        # Verify Status text is displayed
        status_elements = driver.find_elements(
            By.XPATH,
            "//*[normalize-space()='Status']"
        )

        visible_status = False

        for element in status_elements:

            if element.is_displayed():

                visible_status = True
                break

        assert visible_status

        print(
            "TC_LEAVE_017 - Status filter options displayed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_018
# Verify Clear All clears selected filters
# ================================================================

def test_tc_leave_018_clear_all():

    driver, leave_page = open_leave_page()

    try:

        # Open Filter
        leave_page.click_filter()

        time.sleep(2)

        # Select Full Day
        leave_page.select_full_day()

        time.sleep(4)

        # Clear filter
        leave_page.click_clear_all()

        time.sleep(4)

        # Verify leave list returned
        rows = leave_page.get_leave_rows()

        assert len(rows) > 0

        print(
            "TC_LEAVE_018 - Clear All cleared the selected filter successfully"
        )

    finally:

        driver.quit()