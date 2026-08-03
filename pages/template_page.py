from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time


class TemplatePage:

    def __init__(self, driver):

        self.driver = driver

        # ==========================
        # TEMPLATE MENU
        # ==========================

        self.template_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[5]/span'
        )

        # ==========================
        # OFFER LETTER
        # ==========================

        self.name_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[1]/input'
        )

        self.employee_email_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[2]/input'
        )

        self.address_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[3]/input'
        )

        self.date_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[4]/div/input'
        )

        self.role_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[5]/div/select'
        )

        self.joining_date_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[6]/div/input'
        )

        self.ending_date_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[7]/div/input'
        )

        self.department_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[8]/input'
        )

        self.reporting_manager_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[9]/input'
        )

        self.reporting_manager_email_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[10]/input'
        )

        self.preview_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[2]/button[2]'
        )

        # ==========================
        # SERVICE LETTER
        # ==========================

        self.service_letter_tab = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/button[2]'
        )

        self.service_name = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[1]/input'
        )

        self.service_designation = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[2]/div/select'
        )

        self.service_role = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[3]/div/select'
        )

        self.service_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[4]/div/input'
        )

        self.service_end_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[5]/div/input'
        )

        self.service_join_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[6]/div/input'
        )

        self.add_achievement = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/button/span[2]'
        )

        self.achievement_textbox = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[2]/div[4]/input'
        )

        self.service_preview = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[3]/button[1]'
        )

    def open_template_page(self):
        template = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(self.template_menu)
        )

        template.click()

        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,0)")

    def fill_template_details(
            self,
            name,
            email,
            address,
            role,
            joining_date,
            ending_date,
            department,
            manager,
            manager_email
    ):
        today = datetime.now().strftime("%d/%m/%Y")

        # Name
        name_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(self.name_input)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            name_field
        )

        name_field.clear()
        name_field.send_keys(name)

        # Email
        email_field = self.driver.find_element(*self.employee_email_input)
        email_field.clear()
        email_field.send_keys(email)

        # Address
        address_field = self.driver.find_element(*self.address_input)
        address_field.clear()
        address_field.send_keys(address)

        # Date
        date_field = self.driver.find_element(*self.date_input)
        date_field.clear()
        date_field.send_keys(today)

        # Role
        Select(
            self.driver.find_element(*self.role_dropdown)
        ).select_by_visible_text(role)

        # Joining Date
        joining = self.driver.find_element(*self.joining_date_input)
        joining.clear()
        joining.send_keys(joining_date)

        # Ending Date
        ending = self.driver.find_element(*self.ending_date_input)
        ending.clear()
        ending.send_keys(ending_date)

        # Scroll to bottom fields
        self.driver.execute_script(
            "window.scrollBy(0,350);"
        )

        time.sleep(1)

        # Department
        department_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.department_input
            )
        )

        department_field.clear()
        department_field.send_keys(department)

        # Reporting Manager
        manager_field = self.driver.find_element(
            *self.reporting_manager_input
        )

        manager_field.clear()
        manager_field.send_keys(manager)

        # Manager Email
        manager_email_field = self.driver.find_element(
            *self.reporting_manager_email_input
        )

        manager_email_field.clear()
        manager_email_field.send_keys(manager_email)

        time.sleep(2)

    def click_preview(self):
        preview = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.preview_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            preview
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            preview
        )

        print("Offer Letter Preview Opened")

        time.sleep(5)

    def open_service_letter(self):
        service = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.service_letter_tab
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            service
        )

        time.sleep(2)

    def fill_service_letter(
            self,
            name,
            designation,
            role,
            ending_date,
            joining_date,
            achievement
    ):
        today = datetime.now().strftime("%d/%m/%Y")

        # Name
        name_field = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.service_name
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            name_field
        )

        name_field.clear()
        name_field.send_keys(name)

        # Designation
        Select(
            self.driver.find_element(
                *self.service_designation
            )
        ).select_by_visible_text(designation)

        # Role
        Select(
            self.driver.find_element(
                *self.service_role
            )
        ).select_by_visible_text(role)

        # Current Date
        date = self.driver.find_element(
            *self.service_date
        )

        date.clear()
        date.send_keys(today)

        # End Date
        end = self.driver.find_element(
            *self.service_end_date
        )

        end.clear()
        end.send_keys(ending_date)

        # Join Date
        join = self.driver.find_element(
            *self.service_join_date
        )

        join.clear()
        join.send_keys(joining_date)

        # Scroll Down
        self.driver.execute_script(
            "window.scrollBy(0,400)"
        )

        time.sleep(1)

        # Add Achievement
        add = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.add_achievement
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add
        )

        time.sleep(1)

        # Achievement Text
        achievement_box = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.achievement_textbox
            )
        )

        achievement_box.clear()
        achievement_box.send_keys(achievement)

        time.sleep(2)

    def click_service_preview(self):
        preview = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.service_preview
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            preview
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            preview
        )

        print("Service Letter Preview Opened")

        time.sleep(5)