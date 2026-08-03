from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.project_page import ProjectPage
import time


def test_create_project():

    driver = get_driver()

    login_page = LoginPage(driver)
    project_page = ProjectPage(driver)

    # Open Login Page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # Open Project Page
    project_page.open_project_page()

    # Click New Project
    project_page.click_new_project()

    # Enter Project Details
    project_page.enter_project_details(
        "ERP Test case creation",
        "Manual Testing Project"
    )

    # Select Project Member
    project_page.select_project_member()

    # Click Add Button
    project_page.click_add_button()

    # Create Project
    project_page.create_project()

    print("Project Created Successfully")

    time.sleep(5)

    driver.quit()