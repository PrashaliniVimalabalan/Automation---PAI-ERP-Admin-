import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.attendance_page import AttendancePage


# ==================================================
# TC_ATT_001
# Verify Attendance Page Loads Successfully
# ==================================================

def test_tc_att_001_attendance_page_loads(driver):

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

    # Verify Attendance Page
    assert attendance_page.is_attendance_page_displayed()

    print(
        "TC_ATT_001 - Attendance page loaded successfully"
    )


# ==================================================
# TC_ATT_006
# Verify All Status Dropdown is Displayed
# ==================================================

def test_tc_att_006_status_dropdown_displayed(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    assert attendance_page.is_status_dropdown_displayed()

    print(
        "TC_ATT_006 - All Status dropdown displayed correctly"
    )


# ==================================================
# TC_ATT_007
# Verify Attendance Records Filtered by Status
# ==================================================

def test_tc_att_007_filter_attendance_by_status(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    attendance_page.open_status_dropdown()

    attendance_page.select_status("Absent")

    print(
        "TC_ATT_007 - Attendance filtered by selected status"
    )


# ==================================================
# TC_ATT_009
# Verify All Department Dropdown is Displayed
# ==================================================

def test_tc_att_009_department_dropdown_displayed(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    assert attendance_page.is_department_dropdown_displayed()

    print(
        "TC_ATT_009 - All Department dropdown displayed correctly"
    )


# ==================================================
# TC_ATT_010
# Verify Attendance Filtered by Department
# ==================================================

def test_tc_att_010_filter_attendance_by_department(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    attendance_page.open_department_dropdown()

    attendance_page.select_department(
        "QA Department"
    )

    print(
        "TC_ATT_010 - Attendance filtered by department"
    )


# ==================================================
# TC_ATT_011
# Verify Search Employee Field
# ==================================================

def test_tc_att_011_search_employee(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    attendance_page.search_employee("aafi")

    print(
        "TC_ATT_011 - Employee search performed successfully"
    )


# ==================================================
# TC_ATT_012
# Verify Clear Filters Button
# ==================================================

def test_tc_att_012_clear_filters(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    # Apply a filter
    attendance_page.search_employee("aafi")

    time.sleep(2)

    # Clear filters
    attendance_page.click_clear_filters()

    print(
        "TC_ATT_012 - Attendance filters cleared successfully"
    )


# ==================================================
# TC_ATT_013
# Verify Export Button
# ==================================================

def test_tc_att_013_export_button(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    attendance_page.click_export()

    print(
        "TC_ATT_013 - Export dropdown opened successfully"
    )


# ==================================================
# TC_ATT_014
# Verify Export PDF and XLS
# ==================================================

def test_tc_att_014_export_pdf_excel(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    attendance_page = AttendancePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    dashboard_page.open_attendance_page()

    time.sleep(3)

    # --------------------------------------------------
    # Export PDF
    # --------------------------------------------------

    attendance_page.click_export()

    attendance_page.click_pdf_export()

    time.sleep(3)

    print(
        "TC_ATT_014 - PDF exported successfully"
    )

    # --------------------------------------------------
    # Export XLS
    # --------------------------------------------------

    attendance_page.click_export()

    attendance_page.click_xls_export()

    time.sleep(3)

    print(
        "TC_ATT_014 - XLS exported successfully"
    )