import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LeavePage:

    def __init__(self, driver):

        self.driver = driver

        # =========================================================
        # LEAVE MENU
        # =========================================================

        self.leave_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[3]'
        )

        # =========================================================
        # TODAY BUTTON
        # =========================================================

        self.today_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/button[1]'
        )

        # =========================================================
        # WEEK BUTTON
        # =========================================================

        self.week_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/button[2]'
        )

        # =========================================================
        # SEARCH BOX
        # =========================================================

        self.search_box = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[1]/div/div[2]/input'
        )

        # =========================================================
        # LEAVE TABLE ROWS
        # =========================================================

        self.leave_table_rows = (
            By.XPATH,
            "//table/tbody/tr"
        )

        # =========================================================
        # COUNT CARDS
        # =========================================================

        self.all_leaves_card = (
            By.XPATH,
            "//*[contains(normalize-space(),'All Leaves')]"
        )

        self.pending_approvals_card = (
            By.XPATH,
            "//*[contains(normalize-space(),'Pending Approvals')]"
        )

        self.approved_leaves_card = (
            By.XPATH,
            "//*[contains(normalize-space(),'Approved Leaves')]"
        )

        self.rejected_leaves_card = (
            By.XPATH,
            "//*[contains(normalize-space(),'Rejected Leaves')]"
        )

        # =========================================================
        # LEAVE REQUESTS
        # =========================================================

        self.leave_requests_text = (
            By.XPATH,
            "//*[contains(normalize-space(),'Leave Requests')]"
        )

        # =========================================================
        # LEAVE TYPE
        # =========================================================

        self.leave_type_text = (
            By.XPATH,
            "//*[contains(normalize-space(),'Leave Type')]"
        )

        # =========================================================
        # STATUS
        # =========================================================

        self.status_text = (
            By.XPATH,
            "//*[normalize-space()='Status']"
        )

        # =========================================================
        # FILTER BUTTON
        # Green funnel icon
        # Exact locator provided by user
        # =========================================================

        self.filter_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[1]/div/div[1]/button/img'
        )

        # =========================================================
        # FULL DAY FILTER
        # Exact locator provided by user
        # =========================================================

        self.full_day_option = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[1]/div/div[1]/div/div[1]/button[1]/span[1]'
        )

        # =========================================================
        # CLEAR ALL
        # Exact locator provided by user
        # =========================================================

        self.clear_all_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[1]/div/div[1]/div/button'
        )

        # =========================================================
        # NO RECORDS MESSAGE
        # =========================================================

        self.no_records_message = (
            By.XPATH,
            "//*[contains(normalize-space(),'No records') "
            "or contains(normalize-space(),'No Record') "
            "or contains(normalize-space(),'No leave') "
            "or contains(normalize-space(),'No leaves')]"
        )

        # =========================================================
        # LEAVE DETAILS - VIEW ACTION
        # Exact locator provided by user
        # =========================================================

        self.view_leave_action = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[1]/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[7]/div/button/img'
        )

        # =========================================================
        # LEAVE DETAILS POPUP
        # =========================================================

        self.leave_details_popup = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]'
        )

        # =========================================================
        # PENDING RADIO BUTTON
        # Exact locator provided by user
        # =========================================================

        self.pending_radio = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/span[2]'
        )

        # =========================================================
        # REJECTED RADIO BUTTON
        # Exact locator provided by user
        # =========================================================

        self.rejected_radio = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[2]/div[3]/div[1]/div[3]/span[2]'
        )

        # =========================================================
        # APPROVED RADIO BUTTON
        # Exact locator provided by user
        # =========================================================

        self.approved_radio = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[2]/div[3]/div[1]/div[5]/span[2]'
        )

        # =========================================================
        # REJECTED REASON
        # Exact ID provided by user
        # =========================================================

        self.rejected_reason = (
            By.ID,
            "rejected-reason"
        )

        # =========================================================
        # VIEW DOCUMENT
        # Exact locator provided by user
        # =========================================================

        self.view_document_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[2]/div[3]/div[2]/button'
        )

        # =========================================================
        # UPDATE BUTTON
        # Exact locator provided by user
        # =========================================================

        self.update_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]/div/div/div[2]/button'
        )

        # =========================================================
        # CLOSE POPUP BUTTON
        # =========================================================

        self.popup_close_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div[3]/div/div/button/img'
        )

    # =============================================================
    # SCROLL TO ELEMENT
    # =============================================================

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

    # =============================================================
    # OPEN LEAVE PAGE
    # =============================================================

    def open_leave_page(self):

        leave = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.leave_menu
            )
        )

        self.scroll_to_element(leave)

        self.driver.execute_script(
            "arguments[0].click();",
            leave
        )

        time.sleep(3)

        print(
            "Leave Page Opened Successfully"
        )

    # =============================================================
    # VERIFY LEAVE PAGE
    # =============================================================

    def is_leave_page_displayed(self):

        try:

            WebDriverWait(self.driver, 20).until(
                ec.presence_of_element_located(
                    self.leave_requests_text
                )
            )

            return True

        except Exception:

            return False

    # =============================================================
    # CLICK TODAY BUTTON
    # =============================================================

    def click_today_button(self):

        today = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.today_button
            )
        )

        self.scroll_to_element(today)

        self.driver.execute_script(
            "arguments[0].click();",
            today
        )

        time.sleep(3)

        print(
            "Today Button Working Successfully"
        )

    # =============================================================
    # CLICK WEEK BUTTON
    # =============================================================

    def click_week_button(self):

        week = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.week_button
            )
        )

        self.scroll_to_element(week)

        self.driver.execute_script(
            "arguments[0].click();",
            week
        )

        time.sleep(3)

        print(
            "Week Button Working Successfully"
        )

    # =============================================================
    # SEARCH LEAVE EMPLOYEE
    # =============================================================

    def search_leave_employee(self, employee_name):

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

        search.send_keys(
            employee_name
        )

        time.sleep(3)

    # =============================================================
    # CLEAR SEARCH
    # =============================================================

    def clear_search(self):

        search = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.search_box
            )
        )

        search.clear()

        time.sleep(3)

    # =============================================================
    # GET LEAVE TABLE ROWS
    # =============================================================

    def get_leave_rows(self):

        return self.driver.find_elements(
            *self.leave_table_rows
        )

    # =============================================================
    # VERIFY EMPLOYEE LEAVE DISPLAYED
    # =============================================================

    def is_employee_leave_displayed(self, employee_name):

        rows = self.get_leave_rows()

        employee_name = employee_name.lower()

        for row in rows:

            if employee_name in row.text.lower():

                return True

        return False

    # =============================================================
    # VERIFY NO RECORDS DISPLAYED
    # =============================================================

    def is_no_records_displayed(self):

        try:

            messages = self.driver.find_elements(
                *self.no_records_message
            )

            for message in messages:

                if message.is_displayed():

                    return True

        except Exception:

            pass

        return False

    # =============================================================
    # VERIFY LEAVE TABLE DISPLAYED
    # =============================================================

    def is_leave_table_displayed(self):

        try:

            rows = self.get_leave_rows()

            return len(rows) > 0

        except Exception:

            return False

    # =============================================================
    # VERIFY ALL LEAVES
    # =============================================================

    def is_all_leaves_displayed(self):

        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.all_leaves_card
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # =============================================================
    # VERIFY PENDING APPROVALS
    # =============================================================

    def is_pending_approvals_displayed(self):

        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.pending_approvals_card
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # =============================================================
    # VERIFY APPROVED LEAVES
    # =============================================================

    def is_approved_leaves_displayed(self):

        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.approved_leaves_card
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # =============================================================
    # VERIFY REJECTED LEAVES
    # =============================================================

    def is_rejected_leaves_displayed(self):

        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.rejected_leaves_card
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # =============================================================
    # VERIFY LEAVE TYPE
    # =============================================================

    def is_leave_type_displayed(self):

        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.leave_type_text
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # =============================================================
    # VERIFY STATUS
    # =============================================================

    def is_status_displayed(self):

        try:

            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.status_text
                )
            )

            return element.is_displayed()

        except Exception:

            return False

    # =============================================================
    # OPEN FILTER
    # =============================================================

    def click_filter(self):

        filter_icon = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.filter_button
            )
        )

        self.scroll_to_element(filter_icon)

        self.driver.execute_script(
            "arguments[0].click();",
            filter_icon
        )

        time.sleep(2)

        print(
            "Filter opened successfully"
        )

    # =============================================================
    # SELECT FULL DAY
    # =============================================================

    def select_full_day(self):

        full_day = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.full_day_option
            )
        )

        self.scroll_to_element(full_day)

        self.driver.execute_script(
            "arguments[0].click();",
            full_day
        )

        time.sleep(3)

        print(
            "Full Day filter selected successfully"
        )

    # =============================================================
    # CLEAR ALL FILTERS
    # =============================================================

    def click_clear_all(self):

        clear = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.clear_all_button
            )
        )

        self.scroll_to_element(clear)

        self.driver.execute_script(
            "arguments[0].click();",
            clear
        )

        time.sleep(3)

        print(
            "Clear All clicked successfully"
        )

    # =============================================================
    # OPEN LEAVE DETAILS
    # =============================================================

    def open_leave_details(self):

        view_button = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located(
                self.view_leave_action
            )
        )

        self.scroll_to_element(view_button)

        self.driver.execute_script(
            "arguments[0].click();",
            view_button
        )

        time.sleep(3)

        print(
            "Leave Details popup opened successfully"
        )

    # =============================================================
    # VERIFY LEAVE DETAILS POPUP
    # =============================================================

    def is_leave_popup_displayed(self):

        try:

            popup = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.leave_details_popup
                )
            )

            return popup.is_displayed()

        except Exception:

            return False

    # =============================================================
    # GET LEAVE DETAILS POPUP TEXT
    # =============================================================

    def get_leave_popup_text(self):

        popup = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                self.leave_details_popup
            )
        )

        time.sleep(1)

        return popup.text

    # =============================================================
    # SELECT PENDING
    # =============================================================

    def select_pending_status(self):

        pending = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                self.pending_radio
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            pending
        )

        time.sleep(2)

        print(
            "Pending status selected successfully"
        )

    # =============================================================
    # SELECT APPROVED
    # =============================================================

    def select_approved_status(self):

        approved = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                self.approved_radio
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            approved
        )

        time.sleep(2)

        print(
            "Approved status selected successfully"
        )

    # =============================================================
    # SELECT REJECTED
    # =============================================================

    def select_rejected_status(self):

        rejected = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                self.rejected_radio
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            rejected
        )

        time.sleep(2)

        print(
            "Rejected status selected successfully"
        )

    # =============================================================
    # VERIFY REJECTED REASON DISPLAYED
    # =============================================================

    def is_rejected_reason_displayed(self):

        try:

            reason = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(
                    self.rejected_reason
                )
            )

            return reason.is_displayed()

        except Exception:

            return False

    # =============================================================
    # ENTER REJECTED REASON
    # =============================================================

    def enter_rejected_reason(self, reason):

        reason_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(
                self.rejected_reason
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            reason_field
        )

        time.sleep(1)

        reason_field.clear()

        reason_field.send_keys(
            reason
        )

        time.sleep(2)

        print(
            "Rejected reason entered successfully"
        )

    # =============================================================
    # UPDATE LEAVE
    # =============================================================

    def click_update(self):

        update = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                self.update_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            update
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            update
        )

        time.sleep(4)

        print(
            "Update button clicked successfully"
        )

    # =============================================================
    # VIEW DOCUMENT
    # =============================================================

    def click_view_document(self):

        document_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                self.view_document_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            document_button
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            document_button
        )

        time.sleep(4)

        print(
            "View Document clicked successfully"
        )

    # =============================================================
    # CLOSE LEAVE DETAILS POPUP
    # =============================================================

    def close_leave_popup(self):

        close_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(
                self.popup_close_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            close_button
        )

        time.sleep(3)

        print(
            "Leave Details popup closed successfully"
        )

    # =============================================================
    # VERIFY POPUP CLOSED
    # =============================================================

    def is_leave_popup_closed(self):

        try:

            elements = self.driver.find_elements(
                *self.leave_details_popup
            )

            for element in elements:

                if element.is_displayed():

                    return False

            return True

        except Exception:

            return True