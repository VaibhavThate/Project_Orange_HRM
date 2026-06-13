from playwright.sync_api import expect
import pytest
from config import base_url, username, password, invalid_username, invalid_password, valid_username, valid_password
from pages.login_page import Login
import allure


@allure.feature("login module")
@allure.story("valid login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_page(page):
    page = page
    login = Login(page)

    page.goto(base_url)
    #case-1 verify the company logo should be visible
    expect(login.check_hrm_logo()).to_be_visible()

    #case-4 verify the copyright section
    expect(login.check_copyright_section()).to_be_visible()

    #case-5 verify the social site section
    expect(login.check_social_site()).to_be_visible()

    #case-2 Verify the login successful
    login.login_hrm(username,password)

    #debug
    #print(login.check_dashboard_page().inner_text())
    expect(login.check_dashboard_page()).to_contain_text("Dashboard")


@allure.feature("login module")
@allure.story("invalid login 1")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login_1(page):
    page = page

    login = Login(page)
    #case-7 verify the invalid login using invalid username and valid password
    page.goto(base_url)
    login.login_hrm(invalid_username, valid_password)
    expect(login.check_error_msg()).to_contain_text("Invalid credentials")

@allure.feature("login module")
@allure.story("invalid login 2")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login_2(page):
    page = page
    login = Login(page)

    #case-8 verify the invalid login uding valid username and invalid password
    page.goto(base_url)
    login.login_hrm(valid_username, invalid_password)
    expect(login.check_error_msg()).to_contain_text("Invalid credentials")

@allure.feature("login module")
@allure.story("forgot process")
@allure.severity(allure.severity_level.NORMAL)
def test_forgot_process(page):
    page = page
    login = Login(page)

    page.goto(base_url)

    #case-3 verify to check the forgot password button
    login.click_forgot_password()
    #debug
    #print(login.check_reset_pwd_page().inner_text())
    expect(login.check_reset_pwd_page()).to_contain_text('Reset Password')

@allure.feature("login module")
@allure.story("all right button")
def test_all_right_btn(page):
    page = page

    login = Login(page)

    page.goto(base_url)

    #check-6 verify all right button should click
    login.click_all_right_btn()

