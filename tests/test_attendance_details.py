import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.attendance_page import AttendancePage


# ==================================================
# TC_ATT_DET_001
# Verify Eye Icon is Displayed in Actions Column
# ==================================================

def test_tc_att_det_001_eye_icon_displayed(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    # Verify Dashboard
    assert dashboard_page.is_dashboard_displayed()

    # Open Attendance
    dashboard_page.open_attendance_page()

    time.sleep(3)

    # Verify Eye icon
    assert attendance_page.is_eye_icon_displayed()

    print(
        "TC_ATT_DET_001 - Eye icon displayed correctly"
    )


# ==================================================
# TC_ATT_DET_002
# Verify Attendance Details Popup Opens
# ==================================================

def test_tc_att_det_002_attendance_details_popup(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    # Verify Dashboard
    assert dashboard_page.is_dashboard_displayed()

    # Open Attendance
    dashboard_page.open_attendance_page()

    time.sleep(3)

    # Open Attendance Details
    attendance_page.open_attendance_details()

    # Verify popup
    assert attendance_page.is_attendance_details_popup_displayed()

    print(
        "TC_ATT_DET_002 - Attendance Details popup opened successfully"
    )


# ==================================================
# TC_ATT_DET_007
# Verify Close Button
# ==================================================

def test_tc_att_det_007_close_attendance_details(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    # Verify Dashboard
    assert dashboard_page.is_dashboard_displayed()

    # Open Attendance
    dashboard_page.open_attendance_page()

    time.sleep(3)

    # Open Attendance Details
    attendance_page.open_attendance_details()

    # Verify popup opened
    assert attendance_page.is_attendance_details_popup_displayed()

    # Close popup
    attendance_page.close_attendance_details()

    print(
        "TC_ATT_DET_007 - Attendance Details popup closed successfully"
    )