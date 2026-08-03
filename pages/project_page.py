from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class ProjectPage:

    def __init__(self, driver):

        self.driver = driver

        # =========================================
        # PROJECT MENU
        # =========================================

        self.project_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[4]/span'
        )

        # =========================================
        # NEW PROJECT BUTTON
        # =========================================

        self.new_project_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div/div[1]/div/button/img'
        )

        # =========================================
        # PROJECT NAME
        # =========================================

        self.project_name_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/input'
        )

        # =========================================
        # DESCRIPTION
        # =========================================

        self.description_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/textarea'
        )

        # =========================================
        # CHOOSE PERSON BUTTON
        # =========================================

        self.choose_person_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/button[1]'
        )

        # =========================================
        # FIRST MEMBER
        # =========================================

        self.first_member = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]'
        )

        # =========================================
        # ADD BUTTON
        # =========================================

        self.add_button = (
            By.XPATH,
            "//button[contains(text(),'Add')]"
        )

        # =========================================
        # CREATE PROJECT BUTTON
        # =========================================

        self.create_project_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/button[2]'
        )

    # =========================================
    # SMOOTH SCROLL
    # =========================================

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

        time.sleep(1)

    # =========================================
    # OPEN PROJECT PAGE
    # =========================================

    def open_project_page(self):

        project = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.project_menu
            )
        )

        self.scroll_to_element(project)

        self.driver.execute_script(
            "arguments[0].click();",
            project
        )

        time.sleep(2)

    # =========================================
    # CLICK NEW PROJECT
    # =========================================

    def click_new_project(self):

        new_project = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.new_project_button
            )
        )

        self.scroll_to_element(new_project)

        self.driver.execute_script(
            "arguments[0].click();",
            new_project
        )

        time.sleep(2)

    # =========================================
    # ENTER PROJECT DETAILS
    # =========================================

    def enter_project_details(
            self,
            project_name,
            description
    ):

        # Project Name
        project_name_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.project_name_input
            )
        )

        self.scroll_to_element(project_name_field)

        project_name_field.clear()

        project_name_field.send_keys(project_name)

        time.sleep(1)

        # Description
        description_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.description_input
            )
        )

        self.scroll_to_element(description_field)

        description_field.clear()

        description_field.send_keys(description)

        time.sleep(2)

    # =========================================
    # SELECT PROJECT MEMBER
    # =========================================

    def select_project_member(self):

        # Open Choose Person Popup
        choose_person = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.choose_person_button
            )
        )

        self.scroll_to_element(choose_person)

        self.driver.execute_script(
            "arguments[0].click();",
            choose_person
        )

        time.sleep(3)

        # Select Member
        member = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.first_member
            )
        )

        self.scroll_to_element(member)

        self.driver.execute_script(
            "arguments[0].click();",
            member
        )

        time.sleep(2)

    # =========================================
    # CLICK ADD BUTTON
    # =========================================

    def click_add_button(self):

        add_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.add_button
            )
        )

        self.scroll_to_element(add_btn)

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        time.sleep(2)

    # =========================================
    # CREATE PROJECT
    # =========================================

    def create_project(self):

        create_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.create_project_button
            )
        )

        self.scroll_to_element(create_btn)

        self.driver.execute_script(
            "arguments[0].click();",
            create_btn
        )

        time.sleep(5)