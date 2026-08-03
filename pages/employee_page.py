from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class EmployeePage:

    def __init__(self, driver):

        self.driver = driver

        # Employees Menu
        self.employee_menu = (
            By.XPATH,
            "//span[contains(text(),'Employees')]"
        )

        # Search Box
        self.search_box = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[1]/div[2]/div[2]/input'
        )

        # Employee Table
        self.employee_table = (
            By.XPATH,
            "//table/tbody/tr"
        )

        # View Button
        self.view_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[7]/button[1]/img'
        )

        # Edit Button
        self.edit_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[7]/button[2]/img'
        )

        # Current Employee Tab
        self.current_employee_tab = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[1]/div/button[1]/span'
        )

        # Former Employee Tab
        self.former_employee_tab = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[2]/div[1]/div/button[2]/span'
        )

        # New Employee Button
        self.new_employee_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/section/div[1]/div/button/span'
        )

    # Smooth Scroll to Element
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

    # Open Employees Page
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

    # Search Employee
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

    # Click View Employee
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

    # Click Edit Employee
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

    # Open Current Employees
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

    # Open Former Employees
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

    # Click New Employee Button
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

    # Scroll Full Page Down Slowly
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

    # Scroll Full Page Up Slowly
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