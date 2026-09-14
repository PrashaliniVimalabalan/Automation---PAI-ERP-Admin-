import time

from selenium.webdriver.common.by import By

from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


# ================================================================
# Helper
# ================================================================

def open_project_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    project_page = ProjectPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    project_page.open_project_page()

    time.sleep(3)

    return driver, project_page


# ================================================================
# TC_PROJ_NEG_001
# Invalid Project Search
# ================================================================

def test_tc_proj_neg_001_invalid_project_search():

    driver, project_page = open_project_page()

    try:

        project_page.search_project(
            "XYZ123"
        )

        time.sleep(3)

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert "XYZ123" not in page_text or \
               "No projects found" in page_text

        print(
            "TC_PROJ_NEG_001 - Invalid project search handled successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_NEG_002
# Create Project with Empty Fields
# ================================================================

def test_tc_proj_neg_002_create_project_empty_fields():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        time.sleep(2)

        project_page.create_project()

        time.sleep(2)

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        # Popup should remain open because mandatory fields are empty
        assert project_page.is_new_project_popup_displayed()

        print(
            "TC_PROJ_NEG_002 - Empty project fields validation handled successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_NEG_003
# Project Name Empty
# ================================================================

def test_tc_proj_neg_003_empty_project_name():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        time.sleep(2)

        project_page.enter_description(
            "Automation Testing Project"
        )

        project_page.create_project()

        time.sleep(2)

        assert project_page.is_new_project_popup_displayed()

        print(
            "TC_PROJ_NEG_003 - Empty Project Name validation handled successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_NEG_004
# Description Empty
# ================================================================

def test_tc_proj_neg_004_empty_description():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        time.sleep(2)

        project_page.enter_project_name(
            "Negative Test Project"
        )

        project_page.create_project()

        time.sleep(2)

        assert project_page.is_new_project_popup_displayed()

        print(
            "TC_PROJ_NEG_004 - Empty Description validation handled successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_NEG_005
# Task Mandatory Fields Empty
# ================================================================

def test_tc_proj_neg_005_empty_task_fields():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        time.sleep(2)

        project_page.create_task()

        time.sleep(2)

        # New Task popup should remain open
        # because mandatory fields are empty.
        task_input = driver.find_elements(
            *project_page.task_name_input
        )

        assert len(task_input) > 0

        assert task_input[0].is_displayed()

        print(
            "TC_PROJ_NEG_005 - Empty Task mandatory fields validation handled successfully"
        )

    finally:

        driver.quit()