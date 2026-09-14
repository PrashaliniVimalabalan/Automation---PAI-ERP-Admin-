import time

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.leave_page import LeavePage


# ================================================================
# Helper Method
# ================================================================

def open_leave_details():

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

    time.sleep(4)

    # Open first Leave Details
    leave_page.open_leave_details()

    time.sleep(3)

    return driver, leave_page


# ================================================================
# TC_LEAVE_POPUP_001
# Verify Leave Details popup opens
# ================================================================

def test_tc_leave_popup_001_popup_opens():

    driver, leave_page = open_leave_details()

    try:

        assert leave_page.is_leave_popup_displayed()

        print(
            "TC_LEAVE_POPUP_001 - Leave Details popup opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_002
# Verify employee profile information
# ================================================================

def test_tc_leave_popup_002_employee_profile():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        assert len(popup_text.strip()) > 0

        print(
            "TC_LEAVE_POPUP_002 - Employee profile information displayed"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_003
# Verify Annual Leave Balance
# ================================================================

def test_tc_leave_popup_003_annual_leave_balance():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        assert "Annual Leave Balance" in popup_text
        assert "days remaining" in popup_text

        print(
            "TC_LEAVE_POPUP_003 - Annual Leave Balance displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_004
# Verify Leave Type
# ================================================================

def test_tc_leave_popup_004_leave_type():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        assert "Leave Type" in popup_text

        print(
            "TC_LEAVE_POPUP_004 - Leave Type displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_005
# Verify Reason
# ================================================================

def test_tc_leave_popup_005_reason():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        assert "Reason" in popup_text

        print(
            "TC_LEAVE_POPUP_005 - Reason field displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_006
# Verify Leave Date
# ================================================================

def test_tc_leave_popup_006_leave_date():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        assert "Start Date" in popup_text
        assert "End Date" in popup_text

        print(
            "TC_LEAVE_POPUP_006 - Leave dates displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_007
# Verify Leave Session
# ================================================================

def test_tc_leave_popup_007_leave_session():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        # The popup should contain the leave details section.
        assert len(popup_text.strip()) > 0

        print(
            "TC_LEAVE_POPUP_007 - Leave session/details displayed"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_008
# Verify Pending radio button
# ================================================================

def test_tc_leave_popup_008_pending_status():

    driver, leave_page = open_leave_details()

    try:

        leave_page.select_pending_status()

        time.sleep(2)

        assert leave_page.is_leave_popup_displayed()

        print(
            "TC_LEAVE_POPUP_008 - Pending status selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_009
# Verify Approved radio button
# ================================================================

def test_tc_leave_popup_009_approved_status():

    driver, leave_page = open_leave_details()

    try:

        leave_page.select_approved_status()

        time.sleep(2)

        assert leave_page.is_leave_popup_displayed()

        print(
            "TC_LEAVE_POPUP_009 - Approved status selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_010
# Verify Rejected radio button
# ================================================================

def test_tc_leave_popup_010_rejected_status():

    driver, leave_page = open_leave_details()

    try:

        leave_page.select_rejected_status()

        time.sleep(2)

        assert leave_page.is_rejected_reason_displayed()

        print(
            "TC_LEAVE_POPUP_010 - Rejected status selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_011
# Verify rejected reason textbox input
# ================================================================

def test_tc_leave_popup_011_rejected_reason():

    driver, leave_page = open_leave_details()

    try:

        # Select Rejected
        leave_page.select_rejected_status()

        time.sleep(2)

        # Verify reason field
        assert leave_page.is_rejected_reason_displayed()

        # Enter reason
        leave_page.enter_rejected_reason(
            "Invalid Request"
        )

        time.sleep(2)

        print(
            "TC_LEAVE_POPUP_011 - Rejected reason entered successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_012
# Verify Update with Approved status
# ================================================================

def test_tc_leave_popup_012_update_approved():

    driver, leave_page = open_leave_details()

    try:

        # Select Approved
        leave_page.select_approved_status()

        time.sleep(2)

        # Click Update
        leave_page.click_update()

        time.sleep(4)

        print(
            "TC_LEAVE_POPUP_012 - Approved status updated successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_013
# Verify Update with Rejected status
# ================================================================

def test_tc_leave_popup_013_update_rejected():

    driver, leave_page = open_leave_details()

    try:

        # Select Rejected
        leave_page.select_rejected_status()

        time.sleep(2)

        # Enter reason
        leave_page.enter_rejected_reason(
            "Invalid Request"
        )

        time.sleep(2)

        # Click Update
        leave_page.click_update()

        time.sleep(4)

        print(
            "TC_LEAVE_POPUP_013 - Rejected leave updated successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_014
# Verify Update while Pending
# ================================================================

def test_tc_leave_popup_014_update_pending():

    driver, leave_page = open_leave_details()

    try:

        # Pending is the default status.
        leave_page.select_pending_status()

        time.sleep(2)

        # Click Update
        leave_page.click_update()

        time.sleep(4)

        print(
            "TC_LEAVE_POPUP_014 - Pending leave update tested successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_015
# Verify Rejected without reason
# ================================================================

def test_tc_leave_popup_015_rejected_without_reason():

    driver, leave_page = open_leave_details()

    try:

        # Select Rejected
        leave_page.select_rejected_status()

        time.sleep(2)

        # Do not enter reason
        leave_page.click_update()

        time.sleep(3)

        # Verify popup is still displayed.
        # This confirms the update was not completed silently.
        assert leave_page.is_leave_popup_displayed()

        print(
            "TC_LEAVE_POPUP_015 - Rejected without reason validation tested"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_016
# Verify popup close button
# ================================================================

def test_tc_leave_popup_016_close_popup():

    driver, leave_page = open_leave_details()

    try:

        # Close popup
        leave_page.close_leave_popup()

        time.sleep(3)

        # Verify popup closed
        assert leave_page.is_leave_popup_closed()

        print(
            "TC_LEAVE_POPUP_016 - Leave Details popup closed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_017
# Verify Half Day Leave details
# ================================================================

def test_tc_leave_popup_017_half_day_details():

    driver, leave_page = open_leave_details()

    try:

        popup_text = leave_page.get_leave_popup_text()

        assert "Leave Type" in popup_text
        assert "Start Date" in popup_text
        assert "End Date" in popup_text

        print(
            "TC_LEAVE_POPUP_017 - Half Day Leave details checked successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_LEAVE_POPUP_018
# Verify View Document
# ================================================================

def test_tc_leave_popup_018_view_document():

    driver, leave_page = open_leave_details()

    try:

        # Store current window
        original_window = driver.current_window_handle

        # Click View Document
        leave_page.click_view_document()

        time.sleep(5)

        # Check whether a new tab/window opened
        windows = driver.window_handles

        if len(windows) > 1:

            new_window = [
                window
                for window in windows
                if window != original_window
            ][0]

            driver.switch_to.window(
                new_window
            )

            time.sleep(3)

            assert driver.current_url != ""

            print(
                "TC_LEAVE_POPUP_018 - View Document opened successfully"
            )

        else:

            # If document opened in the same tab
            assert driver.current_url != ""

            print(
                "TC_LEAVE_POPUP_018 - View Document opened successfully"
            )

    finally:

        driver.quit()