import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        # ============================================================
        # PROJECT PAGE
        # ============================================================

        self.project_menu = (
            By.XPATH,
            "//*[@id='root']/div/div[1]/nav/a[4]/span"
        )

        self.project_search = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[2]/input"
        )

        self.project_filter = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div[1]/button/img"
        )

        # Project cards container
        self.project_cards = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[3]/div[2]/div"
        )

        # ============================================================
        # NEW PROJECT
        # ============================================================

        self.new_project_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[1]/div/button/img"
        )

        self.project_name_input = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/input"
        )

        self.description_input = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/textarea"
        )

        self.choose_person_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/button[1]"
        )

        self.first_project_member = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]"
        )

        self.add_button = (
            By.XPATH,
            "//button[contains(text(),'Add')]"
        )

        self.create_project_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]/div/div[2]/form/button[2]"
        )

        self.project_popup_close = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]/div/div[1]/button/img"
        )

        self.new_project_popup = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[4]"
        )

        # ============================================================
        # PROJECT DETAILS
        # ============================================================

        self.project_view_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/button/svg"
        )

        # ============================================================
        # TASK
        # ============================================================

        self.new_task_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[1]/div/button[2]/img"
        )

        self.task_name_input = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/input"
        )

        self.assignee_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/div[1]/div[1]/button"
        )

        self.assignee_checkbox = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[5]/div/div[2]/div[2]/div[1]"
        )

        self.add_assignee_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[5]/div/div[2]/button"
        )

        self.priority_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/div[1]/div[2]/button"
        )

        self.high_priority = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[5]/div/div[2]/div/div[3]/div[1]"
        )

        self.add_priority_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[5]/div/div[2]/button"
        )

        self.start_date_input = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/div[2]/div[1]/div/input"
        )

        self.due_date_input = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/div[2]/div[2]/div/input"
        )

        self.task_description_input = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/textarea"
        )

        self.create_task_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/form/button"
        )

        self.edit_task_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr/td[8]/button[2]/img"
        )

        self.delete_task_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[2]/div[2]/table/tbody/tr/td[8]/button[1]/svg"
        )

        self.yes_delete_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div/button[1]"
        )

        self.no_delete_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div/button[2]"
        )

        # ============================================================
        # PROJECT MEMBERS
        # ============================================================

        self.add_member_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[3]/div[2]/div/button/span[1]"
        )

        self.member_checkbox = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div[2]/div[1]"
        )

        self.add_member_confirm_button = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div[4]/div/div[2]/button"
        )

    # ================================================================
    # COMMON CLICK
    # ================================================================

    def click_element(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(1)

        self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        time.sleep(1)

    # ================================================================
    # OPEN PROJECT PAGE
    # ================================================================

    def open_project_page(self):

        self.click_element(self.project_menu)

        self.wait.until(
            EC.url_contains("/projects")
        )

        time.sleep(2)

    # Keep compatibility with both names
    def is_project_displayed(self, project_name=None):

        if project_name:

            elements = self.driver.find_elements(
                By.XPATH,
                f"//*[normalize-space()='{project_name}']"
            )

            return len(elements) > 0

        return "/projects" in self.driver.current_url.lower()

    def is_project_page_displayed(self):

        return self.is_project_displayed()

    # ================================================================
    # PROJECT CARDS
    # ================================================================

    def get_project_cards(self):

        time.sleep(2)

        return self.driver.find_elements(
            *self.project_cards
        )

    # ================================================================
    # SEARCH
    # ================================================================

    def search_project(self, project_name):

        search = self.wait.until(
            EC.presence_of_element_located(
                self.project_search
            )
        )

        search.clear()

        search.send_keys(project_name)

        time.sleep(3)

    # ================================================================
    # FILTER
    # ================================================================

    def click_project_filter(self):

        self.click_element(
            self.project_filter
        )

        time.sleep(2)

    # ================================================================
    # NEW PROJECT
    # ================================================================

    def click_new_project(self):

        self.click_element(
            self.new_project_button
        )

        self.wait.until(
            EC.presence_of_element_located(
                self.new_project_popup
            )
        )

        time.sleep(2)

    def is_new_project_popup_displayed(self):

        elements = self.driver.find_elements(
            *self.new_project_popup
        )

        for element in elements:
            try:
                if element.is_displayed():
                    return True
            except:
                pass

        return False

    def enter_project_name(self, name):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.project_name_input
            )
        )

        element.clear()
        element.send_keys(name)

        time.sleep(1)

    def enter_description(self, description):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.description_input
            )
        )

        element.clear()
        element.send_keys(description)

        time.sleep(1)

    def enter_project_details(self, name, description):

        self.enter_project_name(name)
        self.enter_description(description)

    # ================================================================
    # PROJECT MEMBER SELECTION
    # ================================================================

    def select_project_member(self):

        self.click_element(
            self.choose_person_button
        )

        time.sleep(2)

        self.click_element(
            self.first_project_member
        )

        time.sleep(1)

    def click_add_button(self):

        self.click_element(
            self.add_button
        )

        time.sleep(2)

    # ================================================================
    # CREATE PROJECT
    # ================================================================

    def create_project(self):

        self.click_element(
            self.create_project_button
        )

        time.sleep(4)

    # ================================================================
    # CLOSE PROJECT POPUP
    # ================================================================

    def close_project_popup(self):

        self.click_element(
            self.project_popup_close
        )

        time.sleep(2)

    def is_project_popup_closed(self):

        elements = self.driver.find_elements(
            *self.new_project_popup
        )

        for element in elements:
            try:
                if element.is_displayed():
                    return False
            except:
                pass

        return True

    # ================================================================
    # VIEW SPECIFIC PROJECT
    # ================================================================

    def view_project(self, project_name="ERP Test case creation"):

        time.sleep(2)

        cards = self.get_project_cards()

        if not cards:
            raise Exception(
                "No project cards were found on the Projects page."
            )

        target_card = None

        for card in cards:

            try:

                card_text = card.text.strip()

                if project_name.lower() in card_text.lower():

                    target_card = card
                    break

            except:
                continue

        if target_card is None:

            raise Exception(
                f"Project '{project_name}' was not found in the project cards."
            )

        # Find View button inside the matching project card.
        # The card contains buttons with SVG icons.
        buttons = target_card.find_elements(
            By.XPATH,
            ".//button"
        )

        if not buttons:

            raise Exception(
                f"No buttons found inside project '{project_name}'."
            )

        clicked = False

        for button in buttons:

            try:

                if button.is_displayed() and button.is_enabled():

                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        button
                    )

                    time.sleep(1)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        button
                    )

                    clicked = True
                    break

            except:
                continue

        if not clicked:

            raise Exception(
                f"Could not click View for project '{project_name}'."
            )

        time.sleep(4)

    # ================================================================
    # TASK LIST
    # ================================================================

    def is_task_list_displayed(self):

        elements = self.driver.find_elements(
            By.XPATH,
            "//*[contains(normalize-space(),'Task List')]"
        )

        for element in elements:

            try:

                if element.is_displayed():
                    return True

            except:
                pass

        return False

    # ================================================================
    # NEW TASK
    # ================================================================

    def click_new_task(self):

        self.click_element(
            self.new_task_button
        )

        time.sleep(2)

    def enter_task_name(self, name):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.task_name_input
            )
        )

        element.clear()
        element.send_keys(name)

        time.sleep(1)

    # ================================================================
    # ASSIGNEE
    # ================================================================

    def select_assignee(self):

        self.click_element(
            self.assignee_button
        )

        time.sleep(2)

        self.click_element(
            self.assignee_checkbox
        )

        time.sleep(1)

        self.click_element(
            self.add_assignee_button
        )

        time.sleep(2)

    # ================================================================
    # PRIORITY
    # ================================================================

    def select_high_priority(self):

        self.click_element(
            self.priority_button
        )

        time.sleep(2)

        self.click_element(
            self.high_priority
        )

        time.sleep(1)

        # Click Add for priority popup
        try:

            self.click_element(
                self.add_priority_button
            )

        except:

            pass

        time.sleep(2)

    # ================================================================
    # DATES
    # ================================================================

    def enter_start_date(self, date_value):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.start_date_input
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.click()

        element.clear()

        element.send_keys(date_value)

        time.sleep(1)

    def enter_due_date(self, date_value):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.due_date_input
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.click()

        element.clear()

        element.send_keys(date_value)

        time.sleep(1)

    # ================================================================
    # TASK DESCRIPTION
    # ================================================================

    def enter_task_description(self, description):

        element = self.wait.until(
            EC.presence_of_element_located(
                self.task_description_input
            )
        )

        element.clear()

        element.send_keys(description)

        time.sleep(1)

    # ================================================================
    # CREATE TASK
    # ================================================================

    def create_task(self):

        self.click_element(
            self.create_task_button
        )

        time.sleep(4)

    # ================================================================
    # EDIT TASK
    # ================================================================

    def edit_task(self):

        self.click_element(
            self.edit_task_button
        )

        time.sleep(3)

    # ================================================================
    # DELETE TASK
    # ================================================================

    def delete_task(self):

        self.click_element(
            self.delete_task_button
        )

        time.sleep(2)

    def confirm_delete(self):

        self.click_element(
            self.yes_delete_button
        )

        time.sleep(4)

    def cancel_delete(self):

        self.click_element(
            self.no_delete_button
        )

        time.sleep(2)

    # ================================================================
    # PROJECT MEMBERS
    # ================================================================

    def add_project_member(self):

        self.click_element(
            self.add_member_button
        )

        time.sleep(2)

        self.click_element(
            self.member_checkbox
        )

        time.sleep(1)

        self.click_element(
            self.add_member_confirm_button
        )

        time.sleep(3)