import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class EmployeePage:

    def __init__(self, driver):

        self.driver = driver

        # =========================================================
        # Employees Menu
        # =========================================================

        self.employee_menu = (
            By.XPATH,
            "//span[contains(text(),'Employees')]"
        )

        # =========================================================
        # Search Box
        # =========================================================

        self.search_box = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[1]/div[2]/div[2]/input'
        )

        # =========================================================
        # Employee Table
        # =========================================================

        self.employee_table = (
            By.XPATH,
            "//table/tbody/tr"
        )

        # =========================================================
        # View Button
        # =========================================================

        self.view_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[7]/button[1]/img'
        )

        # =========================================================
        # Edit Button
        # =========================================================

        self.edit_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[7]/button[2]/img'
        )

        # =========================================================
        # Current Employee Tab
        # =========================================================

        self.current_employee_tab = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[1]/div/button[1]/span'
        )

        # =========================================================
        # Former Employee Tab
        # =========================================================

        self.former_employee_tab = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[1]/div/button[2]/span'
        )

        # =========================================================
        # New Employee Button
        # =========================================================

        self.new_employee_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[1]/div/button/span'
        )

        # =========================================================
        # Filter Button
        #
        # NOTE:
        # Replace this XPath with your exact Filter button XPath
        # if the current locator does not work.
        # =========================================================

        self.filter_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[1]/div[2]/div[1]/button'
        )

        # =========================================================
        # Filter Panel
        # =========================================================

        self.filter_panel = (
            By.XPATH,
            "//*[contains(@class,'filter')]"
        )

        # =========================================================
        # Clear All
        #
        # NOTE:
        # Replace with exact XPath if needed.
        # =========================================================

        self.clear_all_button = (
            By.XPATH,
            "//*[normalize-space()='Clear all' or normalize-space()='Clear All']"
        )

        # =========================================================
        # Table No Records Message
        # =========================================================

        self.no_records_message = (
            By.XPATH,
            "//*[contains(normalize-space(),'No employees found.')]"
        )

    # =============================================================
    # Smooth Scroll
    # =============================================================

    def scroll_to_element(self, element):

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
            """,
            element
        )

        time.sleep(2)

    # =============================================================
    # Open Employees Page
    # =============================================================

    def open_employee_page(self):

        employee = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.employee_menu
            )
        )

        self.scroll_to_element(employee)

        self.driver.execute_script(
            "arguments[0].click();",
            employee
        )

        time.sleep(3)

    # =============================================================
    # Verify Employees Page
    # =============================================================

    def is_employee_page_displayed(self):

        try:

            WebDriverWait(self.driver, 20).until(
                ec.presence_of_element_located(
                    self.employee_table
                )
            )

            return True

        except Exception:

            return False

    # =============================================================
    # Search Employee
    # =============================================================

    def search_employee(self, employee_name):

        search = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.search_box
            )
        )

        self.scroll_to_element(search)

        self.driver.execute_script(
            "arguments[0].click();",
            search
        )

        search.clear()

        search.send_keys(employee_name)

        time.sleep(3)

    # =============================================================
    # Clear Search Box
    # =============================================================

    def clear_search(self):

        search = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.search_box
            )
        )

        search.clear()

        time.sleep(3)

    # =============================================================
    # Get Employee Rows
    # =============================================================

    def get_employee_rows(self):

        return self.driver.find_elements(
            *self.employee_table
        )

    # =============================================================
    # Verify Employee Exists in Table
    # =============================================================

    def is_employee_displayed(self, employee_name):

        rows = self.get_employee_rows()

        employee_name = employee_name.lower()

        for row in rows:

            if employee_name in row.text.lower():
                return True

        return False

    # =============================================================
    # Verify No Employee Found
    # =============================================================

    def is_no_records_displayed(self):

        try:

            message = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.no_records_message
                )
            )

            print(
                f"No records message: {message.text}"
            )

            return (
                    message.is_displayed()
                    and "No employees found." in message.text
            )

        except Exception:

            return False

    # =============================================================
    # Click View Employee
    # =============================================================

    def click_view_employee(self):

        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.employee_table
            )
        )

        view = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.view_button
            )
        )

        self.scroll_to_element(view)

        self.driver.execute_script(
            "arguments[0].click();",
            view
        )

        time.sleep(3)

    # =============================================================
    # Click Edit Employee
    # =============================================================

    def click_edit_employee(self):

        WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.employee_table
            )
        )

        edit = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.edit_button
            )
        )

        self.scroll_to_element(edit)

        self.driver.execute_script(
            "arguments[0].click();",
            edit
        )

        time.sleep(3)

    # =============================================================
    # Open Current Employees
    # =============================================================

    def open_current_employees(self):

        current = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.current_employee_tab
            )
        )

        self.scroll_to_element(current)

        self.driver.execute_script(
            "arguments[0].click();",
            current
        )

        time.sleep(3)

    # =============================================================
    # Open Former Employees
    # =============================================================

    def open_former_employees(self):

        former = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.former_employee_tab
            )
        )

        self.scroll_to_element(former)

        self.driver.execute_script(
            "arguments[0].click();",
            former
        )

        time.sleep(3)

    # =============================================================
    # Switch Current -> Former -> Current
    # =============================================================

    def switch_employee_tabs(self):

        self.open_current_employees()

        time.sleep(2)

        self.open_former_employees()

        time.sleep(2)

        self.open_current_employees()

        time.sleep(2)

    # =============================================================
    # Click New Employee
    # =============================================================

    def click_new_employee(self):

        new_employee = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.new_employee_button
            )
        )

        self.scroll_to_element(new_employee)

        self.driver.execute_script(
            "arguments[0].click();",
            new_employee
        )

        time.sleep(3)

    # =============================================================
    # Filter Button
    # =============================================================

    def click_filter(self):

        filter_button = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.filter_button
            )
        )

        self.scroll_to_element(filter_button)

        self.driver.execute_script(
            "arguments[0].click();",
            filter_button
        )

        time.sleep(2)

        print("Employee filter opened successfully")

    # =============================================================
    # Verify Filter Panel
    # =============================================================

    def is_filter_panel_displayed(self):

        try:

            elements = self.driver.find_elements(
                *self.filter_panel
            )

            for element in elements:

                if element.is_displayed():
                    return True

            return False

        except Exception:

            return False

    # =============================================================
    # Clear All Filters
    # =============================================================

    def click_clear_all(self):

        clear_button = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.clear_all_button
            )
        )

        self.scroll_to_element(clear_button)

        self.driver.execute_script(
            "arguments[0].click();",
            clear_button
        )

        time.sleep(3)

        print("All employee filters cleared successfully")

    # =============================================================
    # Scroll Full Page Down
    # =============================================================

    def scroll_page_down(self):

        self.driver.execute_script(
            """
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
            """
        )

        time.sleep(2)

    # =============================================================
    # Scroll Full Page Up
    # =============================================================

    def scroll_page_up(self):

        self.driver.execute_script(
            """
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            """
        )

        time.sleep(2)