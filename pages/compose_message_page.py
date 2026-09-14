import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComposeMessagePage:

    def __init__(self, driver):
        self.driver = driver

        # =========================================================
        # Compose Message Popup
        # =========================================================

        self.compose_popup = (
            By.CSS_SELECTOR,
            "div.cm-modal"
        )

        # =========================================================
        # Recipient Type
        # =========================================================

        self.departments_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/button[1]/span[1]'
        )

        self.individuals_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/button[2]/span[1]'
        )

        # =========================================================
        # Department Dropdown
        # =========================================================

        self.department_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span'
        )

        # =========================================================
        # Individual / Employee Dropdown
        # =========================================================

        self.individual_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/span'
        )

        # =========================================================
        # Department Option
        # =========================================================

        self.department_option = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/label[1]'
        )

        # =========================================================
        # Subject
        # =========================================================

        self.subject_field = (
            By.ID,
            "cm-subject"
        )

        # =========================================================
        # Message
        # =========================================================

        self.message_field = (
            By.ID,
            "cm-message"
        )

        # =========================================================
        # Attach File
        # =========================================================

        self.attach_file = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[4]/span'
        )

        # =========================================================
        # Send Message Button
        # =========================================================

        self.send_message_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/button[2]'
        )

        # =========================================================
        # Cancel Button
        # =========================================================

        self.cancel_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/button[1]'
        )

        # =========================================================
        # Required Validation Message
        # Actual application message:
        # "Subject and message are required."
        # =========================================================

        self.required_message = (
            By.CSS_SELECTOR,
            "p.cm-error"
        )

    # =============================================================
    # Compose Message Popup
    # =============================================================

    def is_compose_popup_displayed(self):

        elements = self.driver.find_elements(
            *self.compose_popup
        )

        for element in elements:
            if element.is_displayed():
                return True

        return False

    # =============================================================
    # Departments
    # =============================================================

    def select_departments(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.departments_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(1)

        print("Departments selected")

    # =============================================================
    # Individuals
    # =============================================================

    def select_individuals(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.individuals_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(1)

        print("Individuals selected")

    # =============================================================
    # Verify Departments Selected
    # =============================================================

    def is_departments_selected(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.departments_button
            )
        )

        return button.is_displayed()

    # =============================================================
    # Department Dropdown
    # =============================================================

    def is_department_dropdown_displayed(self):

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.department_dropdown
            )
        )

        return dropdown.is_displayed()

    # =============================================================
    # Open Department Dropdown
    # =============================================================

    def open_department_dropdown(self):

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.department_dropdown
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            dropdown
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            dropdown
        )

        time.sleep(1)

        print("Department dropdown opened successfully")

    # =============================================================
    # Select Department
    # =============================================================

    def select_department(self):

        option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.department_option
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            option
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            option
        )

        time.sleep(2)

        print("Department selected successfully")

    # =============================================================
    # Individual Dropdown
    # =============================================================

    def is_individual_dropdown_displayed(self):

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.individual_dropdown
            )
        )

        return dropdown.is_displayed()

    # =============================================================
    # Open Individual Dropdown
    # =============================================================

    def open_individual_dropdown(self):

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.individual_dropdown
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            dropdown
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            dropdown
        )

        time.sleep(1)

        print("Employee dropdown opened successfully")

    # =============================================================
    # Subject
    # =============================================================

    def enter_subject(self, subject):

        field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.subject_field
            )
        )

        field.clear()
        field.send_keys(subject)

        time.sleep(1)

    # =============================================================
    # Message
    # =============================================================

    def enter_message(self, message):

        field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.message_field
            )
        )

        field.clear()
        field.send_keys(message)

        time.sleep(1)

    # =============================================================
    # Send Message - Check Enabled
    # =============================================================

    def is_send_message_enabled(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.send_message_button
            )
        )

        return button.is_enabled()

    # =============================================================
    # Send Message
    # =============================================================

    def click_send_message(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.send_message_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)

        print("Send Message button clicked")

    # =============================================================
    # Attach File
    # =============================================================

    def is_attach_file_displayed(self):

        attach = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.attach_file
            )
        )

        return attach.is_displayed()

    # =============================================================
    # Click Attach File
    # =============================================================

    def click_attach_file(self):

        attach = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.attach_file
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            attach
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            attach
        )

        time.sleep(1)

        print("Attach File clicked")

    # =============================================================
    # Cancel
    # =============================================================

    def click_cancel(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                self.cancel_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        time.sleep(2)

        print("Compose Message popup closed successfully")

    # =============================================================
    # Required Validation Message
    # =============================================================

    def is_required_message_displayed(self):

        try:

            message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    self.required_message
                )
            )

            actual_text = message.text.strip()

            print(
                f"Validation message displayed: {actual_text}"
            )

            return (
                message.is_displayed()
                and actual_text == "Subject and message are required."
            )

        except Exception:

            return False