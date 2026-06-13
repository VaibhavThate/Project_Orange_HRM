from playwright.sync_api import Playwright,expect,Page
import pytest
from pages.login_page import Login
from pages.PIM_page import PIM
from config import username, password, first_name, last_name, emp_id, base_url
from conftest import login_page, page
import allure
from utils.data_generator import generate_emp

@allure.feature("PIM module")
@allure.story("check emp ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_pim(login_page):

    pim_page = PIM(login_page)
    emp = generate_emp()
    pim_page.click_pim_option()
    pim_page.click_add_employee()
    pim_page.get_emp_details(emp["first_name"],emp["last_name"],emp["employee_id"])
    pim_page.click_save_btn()
    pim_page.check_success_msg()
    pim_page.verify_emp(emp["employee_id"])
    pim_page.check_emp(emp["employee_id"])


