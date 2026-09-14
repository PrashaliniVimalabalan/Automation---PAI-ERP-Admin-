import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from datetime import datetime


class TemplatePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # ==========================================================
        # TEMPLATE MENU
        # ==========================================================

        self.template_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[5]/span'
        )

        # ==========================================================
        # OFFER LETTER
        # ==========================================================

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

        # Offer Letter buttons
        self.clear_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[2]/button[1]'
        )

        self.save_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[2]/button[3]'
        )

        # ==========================================================
        # SERVICE LETTER TAB
        # ==========================================================

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

        # ==========================================================
        # GENERIC PREVIEW ACTIONS
        # ==========================================================

        self.download_button = (
            By.XPATH,
            "//button[contains(normalize-space(),'Download')]"
        )

        self.email_button = (
            By.XPATH,
            "//button[contains(normalize-space(),'Email')]"
        )

        # ==========================================================
        # SERVICE LETTER SAVE
        # ==========================================================

        self.service_save_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[3]/button[2]'
        )

    # ==============================================================
    # COMMON CLICK
    # ==============================================================

    def click_element(self, locator):

        element = self.wait.until(
            ec.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(1)

        self.wait.until(
            ec.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        time.sleep(2)

    # ==============================================================
    # OPEN TEMPLATE
    # ==============================================================

    def open_template_page(self):

        self.click_element(
            self.template_menu
        )

        time.sleep(2)

    # ==============================================================
    # OFFER LETTER
    # ==============================================================

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
        name_field = self.wait.until(
            ec.visibility_of_element_located(
                self.name_input
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            name_field
        )

        name_field.clear()
        name_field.send_keys(name)

        # Employee Email
        email_field = self.wait.until(
            ec.visibility_of_element_located(
                self.employee_email_input
            )
        )

        email_field.clear()
        email_field.send_keys(email)

        # Address
        address_field = self.wait.until(
            ec.visibility_of_element_located(
                self.address_input
            )
        )

        address_field.clear()
        address_field.send_keys(address)

        # Date
        date_field = self.wait.until(
            ec.visibility_of_element_located(
                self.date_input
            )
        )

        date_field.clear()
        date_field.send_keys(today)

        # Role
        Select(
            self.wait.until(
                ec.presence_of_element_located(
                    self.role_dropdown
                )
            )
        ).select_by_visible_text(role)

        # Joining Date
        joining = self.wait.until(
            ec.visibility_of_element_located(
                self.joining_date_input
            )
        )

        joining.clear()
        joining.send_keys(joining_date)

        # Ending Date
        ending = self.wait.until(
            ec.visibility_of_element_located(
                self.ending_date_input
            )
        )

        ending.clear()
        ending.send_keys(ending_date)

        self.driver.execute_script(
            "window.scrollBy(0,350);"
        )

        time.sleep(1)

        # Department
        department_field = self.wait.until(
            ec.visibility_of_element_located(
                self.department_input
            )
        )

        department_field.clear()
        department_field.send_keys(department)

        # Manager
        manager_field = self.wait.until(
            ec.visibility_of_element_located(
                self.reporting_manager_input
            )
        )

        manager_field.clear()
        manager_field.send_keys(manager)

        # Manager Email
        manager_email_field = self.wait.until(
            ec.visibility_of_element_located(
                self.reporting_manager_email_input
            )
        )

        manager_email_field.clear()
        manager_email_field.send_keys(manager_email)

        time.sleep(2)

    # ==============================================================
    # OFFER PREVIEW
    # ==============================================================

    def click_preview(self):

        self.click_element(
            self.preview_button
        )

        print(
            "Offer Letter Preview Opened"
        )

        time.sleep(5)

    # ==============================================================
    # OFFER CLEAR
    # ==============================================================

    def click_clear(self):

        self.click_element(
            self.clear_button
        )

        time.sleep(2)

    # ==============================================================
    # OFFER SAVE
    # ==============================================================

    def click_save(self):

        self.click_element(
            self.save_button
        )

        time.sleep(3)

    # ==============================================================
    # SERVICE LETTER
    # ==============================================================

    def open_service_letter(self):

        self.click_element(
            self.service_letter_tab
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
        name_field = self.wait.until(
            ec.visibility_of_element_located(
                self.service_name
            )
        )

        name_field.clear()
        name_field.send_keys(name)

        # Designation
        Select(
            self.wait.until(
                ec.presence_of_element_located(
                    self.service_designation
                )
            )
        ).select_by_visible_text(designation)

        # Role
        Select(
            self.wait.until(
                ec.presence_of_element_located(
                    self.service_role
                )
            )
        ).select_by_visible_text(role)

        # Current Date
        date = self.wait.until(
            ec.visibility_of_element_located(
                self.service_date
            )
        )

        date.clear()
        date.send_keys(today)

        # End Date
        end = self.wait.until(
            ec.visibility_of_element_located(
                self.service_end_date
            )
        )

        end.clear()
        end.send_keys(ending_date)

        # Joining Date
        join = self.wait.until(
            ec.visibility_of_element_located(
                self.service_join_date
            )
        )

        join.clear()
        join.send_keys(joining_date)

        self.driver.execute_script(
            "window.scrollBy(0,400);"
        )

        time.sleep(1)

        # Add first achievement
        self.click_element(
            self.add_achievement
        )

        time.sleep(1)

        achievement_box = self.wait.until(
            ec.visibility_of_element_located(
                self.achievement_textbox
            )
        )

        achievement_box.clear()
        achievement_box.send_keys(achievement)

        time.sleep(2)

    # ==============================================================
    # ADD MULTIPLE ACHIEVEMENTS
    # ==============================================================

    def add_achievement_field(self):

        self.click_element(
            self.add_achievement
        )

        time.sleep(2)

    def get_achievement_fields(self):

        return self.driver.find_elements(
            By.XPATH,
            "//input"
        )

    # ==============================================================
    # SERVICE PREVIEW
    # ==============================================================

    def click_service_preview(self):

        self.click_element(
            self.service_preview
        )

        print(
            "Service Letter Preview Opened"
        )

        time.sleep(5)

    # ==============================================================
    # DOWNLOAD
    # ==============================================================

    def click_download(self):

        self.click_element(
            self.download_button
        )

        time.sleep(4)

        print(
            "Download button clicked"
        )

    # ==============================================================
    # EMAIL
    # ==============================================================

    def click_email(self):

        self.click_element(
            self.email_button
        )

        time.sleep(5)

        print(
            "Email button clicked"
        )

    # ==============================================================
    # SERVICE SAVE
    # ==============================================================

    def click_service_save(self):

        self.click_element(
            self.service_save_button
        )

        time.sleep(3)