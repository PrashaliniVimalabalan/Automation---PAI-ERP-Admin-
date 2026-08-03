from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver

        # Dashboard Menu
        self.dashboard_menu = (
            By.XPATH,
            "//a[contains(@href,'dashboard')]"
        )

        # Attendance View All
        self.attendance_view_all = (
            By.CSS_SELECTOR,
            "button.view-all-button"
        )

        # Project View All
        self.project_view_all = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/section[2]/div/button"
        )

        # Compose Message
        self.compose_message = (
            By.XPATH,
            "//*[@id='root']/div/div[2]/div/div/div/div[2]/div/section[3]/button"
        )

        self.logout_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[7]'
        )

    # ----------------------------------------------------
    # Open Dashboard
    # ----------------------------------------------------

    def open_dashboard(self):

        dashboard = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(self.dashboard_menu)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            dashboard
        )

        WebDriverWait(self.driver,20).until(
            lambda d: "dashboard" in d.current_url
        )

    # ----------------------------------------------------
    # Attendance View All
    # ----------------------------------------------------

    def open_attendance_page(self):

        button = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(
                self.attendance_view_all
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(
                self.attendance_view_all
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # ----------------------------------------------------
    # Project View All
    # ----------------------------------------------------

    def open_project_page(self):

        button = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(
                self.project_view_all
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    # ----------------------------------------------------
    # Compose Message
    # ----------------------------------------------------

    def open_compose_message(self):

        button = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(
                self.compose_message
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


    def is_dashboard_displayed(self):
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("dashboard")
        )

        return "dashboard" in self.driver.current_url.lower()

    def click_logout(self):
        logout = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                self.logout_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            logout
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("login")
        )

<<<<<<< HEAD
        print("Logout Successful")
=======
        print("Logout Successful")
>>>>>>> dba01bf3daaa1927d91b2b84ee9979d3dc677922
