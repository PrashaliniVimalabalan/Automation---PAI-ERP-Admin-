from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class SettingsPage:

    def __init__(self, driver):

        self.driver = driver

        # =========================================
        # SETTINGS MENU
        # =========================================

        self.settings_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[6]'
        )

        # =========================================
        # ROLE INPUT
        # =========================================

        self.role_input = (
            By.XPATH,
            '//input'
        )

        # =========================================
        # ADD ROLE BUTTON
        # =========================================

        self.add_role_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/button'
        )

        # =========================================
        # VIEW BUTTON
        # =========================================

        self.view_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/button[1]/img'
        )

        # =========================================
        # EDIT BUTTON
        # =========================================

        self.edit_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/button[2]/img'
        )
        # =========================================
        # CHANGE BUTTON
        # =========================================

        self.change_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/button'
        )

        # =========================================
        # EDIT ROLE INPUT
        # =========================================

        self.edit_role_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/input'
        )
        # =========================================
        # DELETE BUTTON
        # =========================================

        self.delete_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[3]/div[1]/div[2]/button[3]'
        )

        # =========================================
        # DELETE POPUP - NO BUTTON
        # =========================================

        self.delete_no_button = (
            By.XPATH,
            '/html/body/div[2]/div/div[2]/button[1]'
        )

        # =========================================
        # DELETE POPUP - YES BUTTON
        # =========================================

        self.delete_yes_button = (
            By.XPATH,
            '/html/body/div[2]/div/div[2]/button[2]'
        )


        # =========================================
        # BACK BUTTON
        # =========================================

        self.back_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div[1]/button/img'

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
    # OPEN SETTINGS PAGE
    # =========================================

    def open_settings_page(self):

        settings = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.settings_menu
            )
        )

        self.scroll_to_element(settings)

        self.driver.execute_script(
            "arguments[0].click();",
            settings
        )

        time.sleep(2)

    # =========================================
    # ADD ROLE
    # =========================================

    def add_role(self, role_name):

        # Enter Role
        role_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.role_input
            )
        )

        self.scroll_to_element(role_field)

        role_field.clear()

        role_field.send_keys(role_name)

        time.sleep(1)

        # Click Add Role Button
        add_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.add_role_button
            )
        )

        self.scroll_to_element(add_btn)

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        time.sleep(3)

    # =========================================
    # VIEW ROLE
    # =========================================

    def view_role(self):

        view = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.view_button
            )
        )

        self.scroll_to_element(view)

        self.driver.execute_script(
            "arguments[0].click();",
            view
        )

        time.sleep(3)

    # =========================================
    # CLICK BACK BUTTON
    # =========================================

    def click_back_button(self):
        back = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.back_button
            )
        )

        self.scroll_to_element(back)

        self.driver.execute_script(
            "arguments[0].click();",
            back
        )

        time.sleep(3)

    # =========================================
    # EDIT ROLE
    # =========================================

    def edit_role(self, new_role_name):
        time.sleep(3)

        # Click Edit Button
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

        # Edit Input
        role_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.edit_role_input
            )
        )

        role_field.clear()

        role_field.send_keys(
            new_role_name
        )

        time.sleep(2)

        # Click Change Button
        change = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.change_button
            )
        )

        self.scroll_to_element(change)

        self.driver.execute_script(
            "arguments[0].click();",
            change
        )

        time.sleep(3)


        # Click Change Button
        change = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.change_button
            )
        )

        self.scroll_to_element(change)

        self.driver.execute_script(
            "arguments[0].click();",
            change
        )

        time.sleep(3)

    # =========================================
    # DELETE ROLE
    # =========================================

    def delete_role(self):
        time.sleep(3)

        # Click Delete Button
        delete = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.delete_button
            )
        )

        self.scroll_to_element(delete)

        self.driver.execute_script(
            "arguments[0].click();",
            delete
        )

        time.sleep(2)

        # Click YES Popup Button
        yes_button = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.delete_yes_button
            )
        )

        self.scroll_to_element(yes_button)

        self.driver.execute_script(
            "arguments[0].click();",
            yes_button
        )

        time.sleep(3)