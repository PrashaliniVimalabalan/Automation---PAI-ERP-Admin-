from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time


def test_dashboard():

    driver = get_driver()

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    # Login
    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # Dashboard
    dashboard_page.open_dashboard()

    # Attendance View All
    dashboard_page.open_attendance_page()
    time.sleep(3)
    driver.back()

    # Project View All
    dashboard_page.open_project_page()
    time.sleep(3)
    driver.back()

    # Compose Message
    dashboard_page.open_compose_message()
    time.sleep(3)

    print("Dashboard Tested Successfully")

    driver.quit()