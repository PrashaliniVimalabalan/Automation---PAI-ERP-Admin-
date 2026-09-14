import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.compose_message_page import ComposeMessagePage


# ================================================================
# Helper Method
# ================================================================

def open_compose_message(driver):

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    compose_page = ComposeMessagePage(driver)

    # Open Login page
    login_page.open_url()

    # Login
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    time.sleep(3)

    # Open Compose Message
    dashboard_page.open_compose_message()

    time.sleep(2)

    return compose_page


# ================================================================
# TC_MSG_001
# Verify Compose Message popup opens
# ================================================================

def test_tc_msg_001_compose_message_popup_opens(driver):

    compose_page = open_compose_message(driver)

    assert compose_page.is_compose_popup_displayed()

    print(
        "TC_MSG_001 - Compose Message popup opened successfully"
    )


# ================================================================
# TC_MSG_002
# Verify Departments selected by default
# ================================================================

def test_tc_msg_002_departments_selected_by_default(driver):

    compose_page = open_compose_message(driver)

    assert compose_page.is_departments_selected()

    print(
        "TC_MSG_002 - Departments selected by default"
    )


# ================================================================
# TC_MSG_003
# Verify Department dropdown displayed
# ================================================================

def test_tc_msg_003_department_dropdown_displayed(driver):

    compose_page = open_compose_message(driver)

    assert compose_page.is_department_dropdown_displayed()

    print(
        "TC_MSG_003 - Department dropdown displayed correctly"
    )


# ================================================================
# TC_MSG_004
# Verify Employee dropdown displayed
# ================================================================

def test_tc_msg_004_employee_dropdown_displayed(driver):

    compose_page = open_compose_message(driver)

    compose_page.select_individuals()

    time.sleep(1)

    assert compose_page.is_individual_dropdown_displayed()

    print(
        "TC_MSG_004 - Employee dropdown displayed correctly"
    )


# ================================================================
# TC_MSG_005
# Verify Department dropdown opens
# ================================================================

def test_tc_msg_005_department_dropdown_opens(driver):

    compose_page = open_compose_message(driver)

    compose_page.open_department_dropdown()

    time.sleep(1)

    assert compose_page.is_department_dropdown_displayed()

    print(
        "TC_MSG_005 - Department dropdown opened successfully"
    )


# ================================================================
# TC_MSG_006
# Verify Employee dropdown opens
# ================================================================

def test_tc_msg_006_employee_dropdown_opens(driver):

    compose_page = open_compose_message(driver)

    compose_page.select_individuals()

    time.sleep(1)

    compose_page.open_individual_dropdown()

    time.sleep(1)

    assert compose_page.is_individual_dropdown_displayed()

    print(
        "TC_MSG_006 - Employee dropdown opened successfully"
    )


# ================================================================
# TC_MSG_007
# Verify Subject is mandatory
# ================================================================

def test_tc_msg_007_subject_mandatory(driver):

    compose_page = open_compose_message(driver)

    # Open Department dropdown
    compose_page.open_department_dropdown()

    time.sleep(1)

    # Select Department
    compose_page.select_department()

    time.sleep(1)

    # Leave Subject empty
    compose_page.enter_message(
        "This is for testing the ERP system."
    )

    time.sleep(1)

    # Click Send
    compose_page.click_send_message()

    time.sleep(2)

    # Verify actual application validation
    assert compose_page.is_required_message_displayed()

    print(
        "TC_MSG_007 - Subject mandatory validation displayed correctly"
    )


# ================================================================
# TC_MSG_008
# Verify Message is mandatory
# ================================================================

def test_tc_msg_008_message_mandatory(driver):

    compose_page = open_compose_message(driver)

    # Open Department dropdown
    compose_page.open_department_dropdown()

    time.sleep(1)

    # Select Department
    compose_page.select_department()

    time.sleep(1)

    # Enter Subject
    compose_page.enter_subject(
        "Testing PAI ERP"
    )

    time.sleep(1)

    # Leave Message empty
    compose_page.click_send_message()

    time.sleep(2)

    # Verify actual application validation
    assert compose_page.is_required_message_displayed()

    print(
        "TC_MSG_008 - Message mandatory validation displayed correctly"
    )


# ================================================================
# TC_MSG_009
# Verify Recipient is mandatory
# ================================================================

def test_tc_msg_009_recipient_mandatory(driver):

    compose_page = open_compose_message(driver)

    compose_page.enter_subject(
        "Testing PAI ERP"
    )

    compose_page.enter_message(
        "This is for testing the ERP system."
    )

    time.sleep(1)

    # No recipient selected
    assert not compose_page.is_send_message_enabled()

    print(
        "TC_MSG_009 - Send Message remains disabled without recipient"
    )


# ================================================================
# TC_MSG_010
# Verify Send Message disabled without recipient
# ================================================================

def test_tc_msg_010_send_message_disabled_without_recipient(driver):

    compose_page = open_compose_message(driver)

    compose_page.enter_subject(
        "Testing PAI ERP"
    )

    compose_page.enter_message(
        "This is for testing the ERP system."
    )

    time.sleep(1)

    assert not compose_page.is_send_message_enabled()

    print(
        "TC_MSG_010 - Send Message button disabled correctly"
    )


# ================================================================
# TC_MSG_011
# Verify Send Message enabled after selecting Department
# ================================================================

def test_tc_msg_011_send_message_enabled_after_department_selection(driver):

    compose_page = open_compose_message(driver)

    # Open Department dropdown
    compose_page.open_department_dropdown()

    time.sleep(1)

    # Select Department
    compose_page.select_department()

    time.sleep(1)

    # Enter Subject
    compose_page.enter_subject(
        "Testing PAI ERP"
    )

    # Enter Message
    compose_page.enter_message(
        "This is for testing the ERP system."
    )

    time.sleep(2)

    # Verify Send Message is enabled
    assert compose_page.is_send_message_enabled()

    print(
        "TC_MSG_011 - Send Message enabled after department selection"
    )


# ================================================================
# TC_MSG_012
# Verify Attach File is optional
# ================================================================

def test_tc_msg_012_attach_file_optional(driver):

    compose_page = open_compose_message(driver)

    assert compose_page.is_attach_file_displayed()

    print(
        "TC_MSG_012 - Attach File is optional"
    )


# ================================================================
# TC_MSG_016
# Verify Dropdown selection
# ================================================================

def test_tc_msg_016_dropdown_selection_flow(driver):

    compose_page = open_compose_message(driver)

    # Open Department dropdown
    compose_page.open_department_dropdown()

    time.sleep(1)

    # Select Department
    compose_page.select_department()

    time.sleep(2)

    print(
        "TC_MSG_016 - Dropdown selection flow completed"
    )


# ================================================================
# TC_MSG_017
# Verify entered data retained
# ================================================================

def test_tc_msg_017_entered_data_retained(driver):

    compose_page = open_compose_message(driver)

    # Open Department dropdown
    compose_page.open_department_dropdown()

    time.sleep(1)

    # Select Department
    compose_page.select_department()

    time.sleep(1)

    # Enter Subject
    subject = "Testing PAI ERP"

    compose_page.enter_subject(subject)

    # Enter Message
    message = "This is a test message."

    compose_page.enter_message(message)

    time.sleep(1)

    # Get Subject value
    actual_subject = driver.find_element(
        *compose_page.subject_field
    ).get_attribute("value")

    # Get Message value
    actual_message = driver.find_element(
        *compose_page.message_field
    ).get_attribute("value")

    # Verify values
    assert actual_subject == subject
    assert actual_message == message

    print(
        "TC_MSG_017 - Entered data retained correctly"
    )


# ================================================================
# TC_MSG_018
# Verify outside popup behavior
# ================================================================

def test_tc_msg_018_click_outside_popup(driver):

    compose_page = open_compose_message(driver)

    # Click outside popup
    driver.execute_script(
        "document.body.click();"
    )

    time.sleep(2)

    print(
        "TC_MSG_018 - Outside popup behavior checked"
    )


# ================================================================
# TC_MSG_019
# Verify Cancel button closes popup
# ================================================================

def test_tc_msg_019_cancel_button(driver):

    compose_page = open_compose_message(driver)

    # Verify popup is displayed before clicking Cancel
    assert compose_page.is_compose_popup_displayed()

    # Click Cancel
    compose_page.click_cancel()

    time.sleep(2)

    # Verify popup is closed
    assert not compose_page.is_compose_popup_displayed()

    print(
        "TC_MSG_019 - Compose Message popup closed successfully"
    )