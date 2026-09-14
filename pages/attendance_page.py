import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AttendancePage:

    def __init__(self, driver):

        self.driver = driver

        # ==================================================
        # Attendance Page
        # ==================================================

        self.attendance_page = (
            By.XPATH,
            "//*[contains(text(),'Attendance')]"
        )

        # ==================================================
        # Status Dropdown
        # ==================================================

        self.status_dropdown = (
            By.XPATH,
            "//*[contains(text(),'All Status')]"
        )

        # ==================================================
        # Department Dropdown
        # ==================================================

        self.department_dropdown = (
            By.XPATH,
            "//*[contains(text(),'All Department')]"
        )

        # ==================================================
        # Employee Search
        # ==================================================

        self.employee_search = (
            By.XPATH,
            "//input[contains(@placeholder,'Search')]"
        )

        # ==================================================
        # Clear Filters
        # ==================================================

        self.clear_filters_button = (
            By.XPATH,
            "//button[contains(.,'Clear')]"
        )

        # ==================================================
        # Export Button
        # ==================================================

        self.export_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/section[2]/div[1]/div/div/button'
        )

        # ==================================================
        # PDF Export
        # ==================================================

        self.pdf_export = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/section[2]/div[1]/div/div/ul/li[1]'
        )

        # ==================================================
        # XLS Export
        # ==================================================

        self.xls_export = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/section[2]/div[1]/div/div/ul/li[2]'
        )

        # ==================================================
        # Attendance Details - Eye Icon
        # ==================================================

        self.attendance_eye_icon = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/section[3]/div[1]/table/tbody/tr[1]/td[7]/button'
        )

        # ==================================================
        # Attendance Details Popup - Close Button
        # ==================================================

        self.attendance_details_close = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div/div/div/button'
        )

    # ==================================================
    # Verify Attendance Page
    # ==================================================

    def is_attendance_page_displayed(self):

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("attendance")
        )

        return "attendance" in self.driver.current_url.lower()

    # ==================================================
    # Verify Status Dropdown
    # ==================================================

    def is_status_dropdown_displayed(self):

        status = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.status_dropdown
            )
        )

        return status.is_displayed()

    # ==================================================
    # Open Status Dropdown
    # ==================================================

    def open_status_dropdown(self):

        status = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.status_dropdown
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            status
        )

        time.sleep(1)

    # ==================================================
    # Select Status
    # ==================================================

    def select_status(self, status):

        option = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[normalize-space(text())='{status}']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            option
        )

        time.sleep(2)

    # ==================================================
    # Verify Department Dropdown
    # ==================================================

    def is_department_dropdown_displayed(self):

        department = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.department_dropdown
            )
        )

        return department.is_displayed()

    # ==================================================
    # Open Department Dropdown
    # ==================================================

    def open_department_dropdown(self):

        department = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.department_dropdown
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            department
        )

        time.sleep(1)

    # ==================================================
    # Select Department
    # ==================================================

    def select_department(self, department):

        option = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//*[normalize-space(text())='{department}']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            option
        )

        time.sleep(2)

    # ==================================================
    # Search Employee
    # ==================================================

    def search_employee(self, employee_name):

        search = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.employee_search
            )
        )

        search.clear()
        search.send_keys(employee_name)

        time.sleep(2)

    # ==================================================
    # Clear Filters
    # ==================================================

    def click_clear_filters(self):

        button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.clear_filters_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)

    # ==================================================
    # Open Export Dropdown
    # ==================================================

    def click_export(self):

        button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.export_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)

    # ==================================================
    # Click PDF Export
    # ==================================================

    def click_pdf_export(self):

        pdf = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.pdf_export
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            pdf
        )

        time.sleep(3)

    # ==================================================
    # Click XLS Export
    # ==================================================

    def click_xls_export(self):

        xls = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.xls_export
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            xls
        )

        time.sleep(3)

    # ==================================================
    # Verify Eye Icon is Displayed
    # ==================================================

    def is_eye_icon_displayed(self):
        eye_icon = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.attendance_eye_icon
            )
        )

        return eye_icon.is_displayed()

    # ==================================================
    # Open Attendance Details
    # ==================================================

    def open_attendance_details(self):
        eye_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.attendance_eye_icon
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            eye_icon
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            eye_icon
        )

        time.sleep(2)

    # ==================================================
    # Verify Attendance Details Popup
    # ==================================================

    def is_attendance_details_popup_displayed(self):
        close_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                self.attendance_details_close
            )
        )

        return close_button.is_displayed()

    # ==================================================
    # Close Attendance Details Popup
    # ==================================================

    def close_attendance_details(self):
        close_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                self.attendance_details_close
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            close_button
        )

        time.sleep(2)