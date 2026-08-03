from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.project_page import ProjectPage
import time

def test_empty_project_name():

    driver = get_driver()

    login_page = LoginPage(driver)
    project_page = ProjectPage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    project_page.open_project_page()
    project_page.click_new_project()

    project_page.enter_project_details(
        "",
        "Manual Testing Project"
    )

    project_page.create_project()

    print("Empty Project Name Validation Tested")

    driver.quit()

def test_empty_project_description():

    driver = get_driver()

    login_page = LoginPage(driver)
    project_page = ProjectPage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    project_page.open_project_page()
    project_page.click_new_project()

    project_page.enter_project_details(
        "ERP Testing Project",
        ""
    )

    project_page.create_project()

    print("Empty Description Validation Tested")

    driver.quit()

def test_empty_project_fields():

    driver = get_driver()

    login_page = LoginPage(driver)
    project_page = ProjectPage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    project_page.open_project_page()
    project_page.click_new_project()

    project_page.enter_project_details(
        "",
        ""
    )

    project_page.create_project()

    print("Empty Project Fields Validation Tested")

    driver.quit()

def test_special_character_project_name():

    driver = get_driver()

    login_page = LoginPage(driver)
    project_page = ProjectPage(driver)

    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    project_page.open_project_page()
    project_page.click_new_project()

    project_page.enter_project_details(
        "@@@###$$$",
        "Manual Testing Project"
    )

    project_page.create_project()

    print("Special Character Project Name Tested")

    driver.quit()

