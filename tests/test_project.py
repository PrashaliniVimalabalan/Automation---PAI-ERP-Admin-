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
# TC_PROJ_001
# Verify Projects page loads successfully
# ================================================================

def test_tc_proj_001_project_page_loads():

    driver, project_page = open_project_page()

    try:

        assert project_page.is_project_page_displayed()

        print(
            "TC_PROJ_001 - Projects page opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_002
# Verify project cards display correctly
# ================================================================

def test_tc_proj_002_project_cards():

    driver, project_page = open_project_page()

    try:

        cards = project_page.get_project_cards()

        assert len(cards) > 0

        print(
            "TC_PROJ_002 - Project cards displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_003
# Verify project statistics cards display
# ================================================================

def test_tc_proj_003_project_statistics():

    driver, project_page = open_project_page()

    try:

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert "Total Project" in page_text
        assert "Tasks" in page_text

        print(
            "TC_PROJ_003 - Project statistics displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_004
# Valid Project Search
# ================================================================

def test_tc_proj_004_valid_project_search():

    driver, project_page = open_project_page()

    try:

        project_page.search_project(
            "ERP Automation"
        )

        time.sleep(4)

        assert project_page.is_project_displayed(
            "ERP Automation"
        )

        print(
            "TC_PROJ_004 - Valid project search successful"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_006
# Filter button
# ================================================================

def test_tc_proj_006_project_filter():

    driver, project_page = open_project_page()

    try:

        project_page.click_project_filter()

        time.sleep(2)

        print(
            "TC_PROJ_006 - Project filter opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_007
# New Project button
# ================================================================

def test_tc_proj_007_new_project_button():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        assert project_page.is_new_project_popup_displayed()

        print(
            "TC_PROJ_007 - New Project popup opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_008
# New Project popup UI
# ================================================================

def test_tc_proj_008_new_project_popup_ui():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        assert project_page.is_new_project_popup_displayed()

        assert driver.find_element(
            *project_page.project_name_input
        ).is_displayed()

        assert driver.find_element(
            *project_page.description_input
        ).is_displayed()

        print(
            "TC_PROJ_008 - New Project popup UI displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_009
# Project Name valid input
# ================================================================

def test_tc_proj_009_project_name():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        project_page.enter_project_name(
            "ERP Automation"
        )

        value = driver.find_element(
            *project_page.project_name_input
        ).get_attribute("value")

        assert value == "ERP Automation"

        print(
            "TC_PROJ_009 - Project Name accepted valid input"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_011
# Description input
# ================================================================

def test_tc_proj_011_description():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        project_page.enter_description(
            "Automation Testing Project"
        )

        value = driver.find_element(
            *project_page.description_input
        ).get_attribute("value")

        assert value == "Automation Testing Project"

        print(
            "TC_PROJ_011 - Description accepted input"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_012
# Project member selection
# ================================================================

def test_tc_proj_012_project_member():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        project_page.select_project_member()

        project_page.click_add_button()

        print(
            "TC_PROJ_012 - Project member selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_013
# Create Project
# ================================================================

def test_tc_proj_013_create_project():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        project_page.enter_project_details(
            "ERP Web ",
            "Automation Testing Project"
        )

        project_page.select_project_member()

        project_page.click_add_button()

        project_page.create_project()

        time.sleep(4)

        print(
            "TC_PROJ_013 - Project created successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_016
# Close popup
# ================================================================

def test_tc_proj_016_close_popup():

    driver, project_page = open_project_page()

    try:

        project_page.click_new_project()

        assert project_page.is_new_project_popup_displayed()

        project_page.close_project_popup()

        time.sleep(3)

        assert project_page.is_project_popup_closed()

        print(
            "TC_PROJ_016 - Project popup closed successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_017
# View project
# ================================================================

def test_tc_proj_017_view_project():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(4)

        assert "/projects/" in driver.current_url.lower()

        print(
            "TC_PROJ_017 - Project details page opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_018
# Task list
# ================================================================

def test_tc_proj_018_task_list():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(4)

        assert project_page.is_task_list_displayed()

        print(
            "TC_PROJ_018 - Task list displayed correctly"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_019
# New Task
# ================================================================

def test_tc_proj_019_new_task():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        print(
            "TC_PROJ_019 - New Task popup opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_021
# Task Name
# ================================================================

def test_tc_proj_021_task_name():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        project_page.enter_task_name(
            "Admin Panel Testing"
        )

        value = driver.find_element(
            *project_page.task_name_input
        ).get_attribute("value")

        assert value == "Admin Panel Testing"

        print(
            "TC_PROJ_021 - Task Name accepted successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_022
# Assigned Employee
# ================================================================

def test_tc_proj_022_assigned_employee():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        project_page.select_assignee()

        print(
            "TC_PROJ_022 - Employee assigned successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_023
# Start Date
# ================================================================

def test_tc_proj_023_start_date():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        project_page.enter_start_date(
            "15/05/2026"
        )

        print(
            "TC_PROJ_023 - Start Date selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_024
# Due Date
# ================================================================

def test_tc_proj_024_due_date():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        project_page.enter_due_date(
            "20/05/2026"
        )

        print(
            "TC_PROJ_024 - Due Date selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_025
# Priority
# ================================================================

def test_tc_proj_025_priority():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        project_page.select_high_priority()

        print(
            "TC_PROJ_025 - High priority selected successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_027
# Create Task
# ================================================================

def test_tc_proj_027_create_task():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.click_new_task()

        project_page.enter_task_name(
            "Admin Panel Testing"
        )

        project_page.select_assignee()

        project_page.select_high_priority()

        project_page.enter_start_date(
            "15/05/2026"
        )

        project_page.enter_due_date(
            "20/05/2026"
        )

        project_page.enter_task_description(
            "Testing Admin Panel"
        )

        project_page.create_task()

        print(
            "TC_PROJ_027 - Task created successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_029
# Edit Task
# ================================================================

def test_tc_proj_029_edit_task():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.edit_task()

        print(
            "TC_PROJ_029 - Task edit popup opened successfully"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_030
# Delete Task
# ================================================================

#def test_tc_proj_030_delete_task():

   # driver, project_page = open_project_page()

   # try:

       # project_page.view_project(
       #     "ERP Test case creation"
       # )

       # time.sleep(3)

        #project_page.delete_task()

        #time.sleep(2)

      #  project_page.confirm_delete()

     #   print(
    #        "TC_PROJ_030 - Task deleted successfully"
      #  )

   # finally:

      #  driver.quit()


# ================================================================
# TC_PROJ_031
# Project Members
# ================================================================

def test_tc_proj_031_project_members():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert "Members" in page_text

        print(
            "TC_PROJ_031 - Project Members section displayed"
        )

    finally:

        driver.quit()


# ================================================================
# TC_PROJ_032
# Add Member
# ================================================================

def test_tc_proj_032_add_member():

    driver, project_page = open_project_page()

    try:

        project_page.view_project(
            "ERP Test case creation"
        )

        time.sleep(3)

        project_page.add_project_member()

        print(
            "TC_PROJ_032 - Project member added successfully"
        )

    finally:

        driver.quit()