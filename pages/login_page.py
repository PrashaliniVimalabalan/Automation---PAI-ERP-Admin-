from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

        # ==================================================
        # Login Page Locators
        # ==================================================

        # Employee ID field
        self.employee_id_input = (
            By.XPATH,
            "//input[@type='text']"
        )

        # Password field
        self.password_input = (
            By.XPATH,
            "//input[@type='password']"
        )

        # Login button
        self.login_button = (
            By.XPATH,
            "//button[contains(text(),'Login')]"
        )

        # Remember Me
        self.remember_me_checkbox = (
            By.XPATH,
            '//*[@id="root"]/div/div/div/div/div/div/div[2]/div/div[4]/label/span[1]'
        )

        # Company logo
        self.company_logo = (
            By.XPATH,
            "//img"
        )

        # Employee ID required message
        self.employee_id_error = (
            By.XPATH,
            "//*[contains(text(),'Employee ID is required')]"
        )

        # Password required message
        self.password_error = (
            By.XPATH,
            "//*[contains(text(),'Password is required')]"
        )

    # ==================================================
    # Open Login Page
    # ==================================================

    def open_url(self):

        self.driver.get(
            "https://pai-erp-qa.pineappleai.cloud/login"
        )

    # ==================================================
    # Enter Employee ID
    # ==================================================

    def enter_employee_id(self, employee_id):

        employee_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.employee_id_input
            )
        )

        employee_field.clear()
        employee_field.send_keys(employee_id)

    # ==================================================
    # Enter Password
    # ==================================================

    def enter_password(self, password):

        password_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.password_input
            )
        )

        password_field.clear()
        password_field.send_keys(password)

    # ==================================================
    # Click Login
    # ==================================================

    def click_login(self):

        login_btn = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.login_button
            )
        )

        # JavaScript click is used because the button
        # looks disabled but is manually clickable.
        self.driver.execute_script(
            "arguments[0].click();",
            login_btn
        )

    # ==================================================
    # Complete Login
    # ==================================================

    def login(self, employee_id, password):

        self.enter_employee_id(employee_id)
        self.enter_password(password)
        self.click_login()

    # ==================================================
    # Verify Login Page Displayed
    # ==================================================

    def is_login_page_displayed(self):

        WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.employee_id_input
            )
        )

        WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.password_input
            )
        )

        return "login" in self.driver.current_url.lower()

    # ==================================================
    # Verify Company Logo
    # ==================================================

    def is_company_logo_displayed(self):

        logo = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.company_logo
            )
        )

        return logo.is_displayed()

    # ==================================================
    # Verify Employee ID Field
    # ==================================================

    def is_employee_id_displayed(self):

        field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.employee_id_input
            )
        )

        return field.is_displayed()

    # ==================================================
    # Verify Password Field
    # ==================================================

    def is_password_displayed(self):

        field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.password_input
            )
        )

        return field.is_displayed()

    # ==================================================
    # Verify Password is Masked
    # ==================================================

    def is_password_masked(self):

        field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.password_input
            )
        )

        return field.get_attribute("type") == "password"

    # ==================================================
    # Verify Remember Me is Displayed
    # ==================================================

    def is_remember_me_displayed(self):

        checkbox = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.remember_me_checkbox
            )
        )

        return checkbox.is_displayed()

    # ==================================================
    # Click Remember Me
    # ==================================================

    def click_remember_me(self):

        checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.remember_me_checkbox
            )
        )

        checkbox.click()

    # ==================================================
    # Verify Login Button is Displayed
    # ==================================================

    def is_login_button_displayed(self):

        button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.login_button
            )
        )

        return button.is_displayed()

    # ==================================================
    # Verify Login Button is Enabled
    # ==================================================

    def is_login_button_enabled(self):

        button = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.login_button
            )
        )

        return button.is_enabled()

    # ==================================================
    # Verify Employee ID Required Message
    # ==================================================

    def is_employee_id_required_message_displayed(self):

        message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                self.employee_id_error
            )
        )

        return message.is_displayed()

    # ==================================================
    # Verify Password Required Message
    # ==================================================

    def is_password_required_message_displayed(self):

        message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                self.password_error
            )
        )

        return message.is_displayed()