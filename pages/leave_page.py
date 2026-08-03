from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LeavePage:

    def __init__(self, driver):

        self.driver = driver

        # Leave Menu
        self.leave_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[3]'
        )

        # Today Button
        self.today_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/button[1]'
        )

        # Week Button
        self.week_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/button[2]'
        )

        # Search Box
        self.search_box = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[1]/div/div[2]/input'
        )

    # Open Leave Page
    def open_leave_page(self):

        leave = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.leave_menu
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            leave
        )

    # Click Today Button
    def click_today_button(self):

        today = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.today_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            today
        )

    # Click Week Button
    def click_week_button(self):

        week = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.week_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            week
        )

    # Search Leave Employee
    def search_leave_employee(self, employee_name):
        search = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.search_box
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            search
        )

        self.driver.execute_script(
            "arguments[0].click();",
            search
        )

        search.clear()
        search.send_keys(employee_name)