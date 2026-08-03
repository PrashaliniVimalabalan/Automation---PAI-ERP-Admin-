from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class AddEmployeePage:

    def __init__(self, driver):

        self.driver = driver

        # =====================================================
        # STEP 1 - PERSONAL INFORMATION
        # =====================================================

        # Name
        self.name_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[1]/input'
        )

        # Gender Dropdown
        self.gender_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[2]/select'
        )

        # Date of Birth
        self.date_of_birth_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/input'
        )

        # Phone
        self.phone_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[4]/input'
        )

        # Address
        self.address_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[5]/input'
        )

        # Personal Email
        self.personal_email_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[6]/input'
        )

        # Password
        self.password_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/input'
        )

        # Work Email
        self.work_email_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[3]/input'
        )

        # Create Button
        self.create_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[3]/button[2]'
        )

        # =====================================================
        # STEP 2 - EDUCATIONAL INFORMATION
        # =====================================================

        # Qualification Dropdown
        self.education_qualification_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/select'
        )

        # Institute Name
        self.institute_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[2]/input'
        )

        # Year Dropdown
        self.year_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[2]/div[3]/div/select'
        )

        # Position
        self.position_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[1]/input'
        )

        # Company
        self.company_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[2]/input'
        )

        # Experience
        self.experience_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[3]/input'
        )

        # Continue Button
        self.continue_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[3]/button[2]'
        )

        # =====================================================
        # STEP 3 - DOCUMENT UPLOAD
        # =====================================================

        # NIC Upload
        self.nic_upload = (
            By.XPATH,
            '(//input[@type="file"])[1]'
        )

        # Birth Certificate Upload
        self.birth_upload = (
            By.XPATH,
            '(//input[@type="file"])[2]'
        )

        # Education Certificate Upload
        self.education_upload = (
            By.XPATH,
            '(//input[@type="file"])[3]'
        )

        # =========================================
        # STEP 3 - WORK INFORMATION
        # =========================================

        # Date of Joining
        self.date_of_joining_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/input'
        )

        # Designation Dropdown
        self.designation_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[2]/div/select'
        )

        # Role Dropdown
        self.role_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[3]/div/select'
        )

        # Management Role Dropdown
        self.management_role_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[4]/div/select'
        )

        # Reporting Manager Dropdown
        self.reporting_manager_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div[5]/div/select'
        )

        # Save Button
        self.save_employee_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div[3]/button[2]'
        )



    # =====================================================
    # SMOOTH SCROLL
    # =====================================================

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

    # =====================================================
    # STEP 1 - PERSONAL INFORMATION
    # =====================================================

    def fill_personal_information(
            self,
            name,
            gender,
            dob,
            phone,
            address,
            personal_email,
            password,
            work_email
    ):

        # Name
        name_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.name_input
            )
        )

        self.scroll_to_element(name_field)

        name_field.clear()
        name_field.send_keys(name)

        time.sleep(1)

        # Gender
        gender_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.gender_dropdown
            )
        )

        self.scroll_to_element(gender_dropdown)

        Select(gender_dropdown).select_by_visible_text(
            gender
        )

        time.sleep(1)

        # DOB
        dob_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.date_of_birth_input
            )
        )

        self.scroll_to_element(dob_field)

        dob_field.clear()
        dob_field.send_keys(dob)

        time.sleep(1)

        # Phone
        phone_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.phone_input
            )
        )

        self.scroll_to_element(phone_field)

        phone_field.clear()
        phone_field.send_keys(phone)

        time.sleep(1)

        # Address
        address_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.address_input
            )
        )

        self.scroll_to_element(address_field)

        address_field.clear()
        address_field.send_keys(address)

        time.sleep(1)

        # Personal Email
        personal_email_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.personal_email_input
            )
        )

        self.scroll_to_element(personal_email_field)

        personal_email_field.clear()
        personal_email_field.send_keys(personal_email)

        time.sleep(1)

        # Password
        password_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.password_input
            )
        )

        self.scroll_to_element(password_field)

        password_field.clear()
        password_field.send_keys(password)

        time.sleep(1)

        # =========================================
        # WORK EMAIL
        # =========================================

        work_email_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.work_email_input
            )
        )

        self.scroll_to_element(work_email_field)

        time.sleep(1)

        # Select existing value
        work_email_field.send_keys(
            Keys.CONTROL,
            "a"
        )

        time.sleep(1)

        # Delete selected value
        work_email_field.send_keys(
            Keys.DELETE
        )

        time.sleep(1)

        # Click again
        work_email_field.click()

        time.sleep(1)

        # Type slowly
        for char in work_email:
            work_email_field.send_keys(char)

            time.sleep(0.2)

        time.sleep(2)

        # Press TAB to trigger validation
        work_email_field.send_keys(Keys.TAB)

        time.sleep(2)



    # =====================================================
    # CLICK CREATE BUTTON
    # =====================================================

    def click_create_button(self):

        create = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.create_button
            )
        )

        self.scroll_to_element(create)

        self.driver.execute_script(
            "arguments[0].click();",
            create
        )

        time.sleep(3)

    # =====================================================
    # STEP 2 - EDUCATIONAL INFORMATION
    # =====================================================

    def fill_education_information(
            self,
            qualification,
            institute,
            year,
            position,
            company,
            experience
    ):

        # Qualification Dropdown
        qualification_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.education_qualification_dropdown
            )
        )

        self.scroll_to_element(
            qualification_dropdown
        )

        Select(
            qualification_dropdown
        ).select_by_visible_text(
            qualification
        )

        time.sleep(1)

        # Institute
        institute_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.institute_input
            )
        )

        self.scroll_to_element(institute_field)

        institute_field.clear()
        institute_field.send_keys(institute)

        time.sleep(1)

        # Year Dropdown
        year_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.year_dropdown
            )
        )

        self.scroll_to_element(year_dropdown)

        Select(year_dropdown).select_by_visible_text(
            year
        )

        time.sleep(1)

        # Position
        position_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.position_input
            )
        )

        self.scroll_to_element(position_field)

        position_field.clear()
        position_field.send_keys(position)

        time.sleep(1)

        # Company
        company_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.company_input
            )
        )

        self.scroll_to_element(company_field)

        company_field.clear()
        company_field.send_keys(company)

        time.sleep(1)

        # Experience
        experience_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.experience_input
            )
        )

        self.scroll_to_element(experience_field)

        experience_field.clear()
        experience_field.send_keys(experience)

        time.sleep(2)

    # =====================================================
    # CLICK CONTINUE BUTTON
    # =====================================================

    def click_continue_button(self):

        continue_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.continue_button
            )
        )

        self.scroll_to_element(continue_btn)

        self.driver.execute_script(
            "arguments[0].click();",
            continue_btn
        )

        time.sleep(3)

    # =====================================================
    # STEP 3 - DOCUMENT UPLOAD
    # =====================================================

    def upload_documents(
            self,
            nic_path,
            birth_path,
            education_path
    ):

        nic = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.nic_upload
            )
        )

        self.scroll_to_element(nic)

        nic.send_keys(nic_path)

        self.driver.find_element(
            *self.birth_upload
        ).send_keys(birth_path)

        self.driver.find_element(
            *self.education_upload
        ).send_keys(education_path)

        time.sleep(2)

    # =========================================
    # FILL WORK INFORMATION
    # =========================================

    def fill_work_information(
            self,
            joining_date,
            designation,
            role,
            management_role,
            reporting_manager
    ):
        # Date of Joining
        joining = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.date_of_joining_input
            )
        )

        self.scroll_to_element(joining)

        joining.clear()

        joining.send_keys(joining_date)

        time.sleep(2)

        # Designation Dropdown
        designation_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.designation_dropdown
            )
        )

        Select(designation_dropdown).select_by_visible_text(
            designation
        )

        time.sleep(2)

        # Role Dropdown
        role_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.role_dropdown
            )
        )

        Select(role_dropdown).select_by_visible_text(
            role
        )

        time.sleep(2)

        # Management Role Dropdown
        management_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.management_role_dropdown
            )
        )

        Select(management_dropdown).select_by_visible_text(
            management_role
        )

        time.sleep(2)

        # Reporting Manager
        reporting_dropdown = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.reporting_manager_dropdown
            )
        )

        reporting_select = Select(reporting_dropdown)

        for option in reporting_select.options:

            if "Laxshan" in option.text:
                reporting_select.select_by_visible_text(
                    option.text
                )

                break

    # =========================================
    # CLICK SAVE EMPLOYEE
    # =========================================


    def click_save_employee(self):
      save = WebDriverWait(self.driver, 20).until(
        ec.element_to_be_clickable(
            self.save_employee_button
        )
    )

      self.scroll_to_element(save)

      self.driver.execute_script(
        "arguments[0].click();",
        save
    )

    time.sleep(5)