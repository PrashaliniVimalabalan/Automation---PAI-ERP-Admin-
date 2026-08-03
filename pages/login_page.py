from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        # Locators
        self.employee_id_input = (
            By.XPATH,
            "//input[@type='text']"
        )

        self.password_input = (
            By.XPATH,
            "//input[@type='password']"
        )

        self.login_button = (
            By.XPATH,
            "//button[contains(text(),'Login')]"
        )

    def open_url(self):

        self.driver.get(
            "https://pai-erp-qa.pineappleai.cloud/login"
        )

    def enter_employee_id(self, employee_id):

        employee_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.employee_id_input
            )
        )

        employee_field.clear()
        employee_field.send_keys(employee_id)

    def enter_password(self, password):

        password_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.password_input
            )
        )

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):

        login_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.login_button
            )
        )

        login_btn.click()

    def login(self, employee_id, password):

        self.enter_employee_id(employee_id)
        self.enter_password(password)
        self.click_login()