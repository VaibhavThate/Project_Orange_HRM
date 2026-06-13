from playwright.sync_api import Page,expect,Playwright
import pytest
from config import base_url
from pages.login_page import Login
from conftest import login_json_data, login_csv_data
import allure


@allure.feature("login ddt module")
@allure.story("json data login")
@pytest.mark.parametrize('data', login_json_data())
def test_json_login(data,page):
    page = page
    login_ddt = Login(page)
    page.goto(base_url)

    login_ddt.login_hrm(data["username"], data["password"])

    if data["expected"] == "success":
        expect(login_ddt.check_dashboard_page()).to_be_visible()
    else:
        expect(login_ddt.check_error_msg()).to_contain_text(data["expected"])


@allure.feature("login ddt module")
@allure.story("csv data login")
@pytest.mark.parametrize("data", login_csv_data())
def test_csv_login(data,page):
    login_csv = Login(page)
    page.goto(base_url)
    login_csv.login_hrm(data["username"], data["password"])

    if data["expected"] == "success":
        expect(login_csv.check_dashboard_page()).to_be_visible()
    else:
        expect(login_csv.check_error_msg()).to_contain_text(data["expected"])

