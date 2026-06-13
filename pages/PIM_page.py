from playwright.sync_api import Playwright,Page,expect
import pytest
from config import first_name,last_name, emp_id
from utils.data_generator import generate_emp
class PIM:
    def __init__(self, page:Page):
        self.page = page
        self.pim_option = self.page.get_by_text("PIM",exact=True)
        self.add_employee_option = self.page.get_by_text("Add Employee",exact=True)
        self.emp_fname_field = self.page.get_by_placeholder("First Name")
        self.emp_lname_field = self.page.get_by_placeholder("Last Name")
        self.emp_id = self.page.locator("(//label[text()='Employee Id']/../following-sibling::div/input)[1]")
        self.emp_profile_photo = self.page.locator("input[type='file']")
        self.save_btn = self.page.get_by_role('button',name='Save')
        self.success_msg = self.page.locator(".oxd-toast-container.oxd-toast-container--bottom")
        self.emp_list_btn = self.page.get_by_text("Employee List",exact=True)
        self.search_button = self.page.get_by_role("button", name="Search")
        self.emp_lst_id = self.page.locator(".oxd-table-body")

    def click_pim_option(self):
        self.pim_option.click()

    def click_add_employee(self):
        self.add_employee_option.click()

    def get_emp_details(self, firstname, lastname, employee_id):
        self.emp_fname_field.fill(firstname)
        self.emp_lname_field.fill(lastname)
        self.emp_profile_photo.set_input_files("profile_photo/photo.png")
        expect(self.emp_id).to_be_visible(), f"failed locator"
        self.emp_id.fill(str(employee_id))


    def click_save_btn(self):
        self.save_btn.click()

    def check_success_msg(self):
        expect(self.success_msg).to_be_visible(), f"locator not found for success msg"
        return self.success_msg

    def verify_emp(self,employee_id: str):
        self.emp_list_btn.click()
        self.emp_id.fill(employee_id)
        self.search_button.click()

    def check_emp(self, employee_id):
        expect(self.emp_lst_id).to_be_visible(timeout=10000)
        row = self.emp_lst_id.first
        row_data = row.locator(".oxd-table-cell.oxd-padding-cell div")
        count = row_data.count()
        print("count is: ", count)
        lst = []
        for i in range(count):
            individual_data = row_data.nth(i).inner_text()
            if individual_data == str(employee_id):
                lst.append(individual_data)

        print(lst)
        assert lst == [str(employee_id)], f"verified emp ID not successful"




