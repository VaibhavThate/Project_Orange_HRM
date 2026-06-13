from playwright.sync_api import Playwright,Page,expect
import pytest

class Login:
    def __init__(self, page:Page):
        self.page = page
        self.company_logo = self.page.locator("img[alt='company-branding']")
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.get_by_role("button", name=" Login ")
        self.forgot_password = self.page.locator(".orangehrm-login-forgot")
        self.copyright_section = self.page.locator(".orangehrm-copyright-wrapper")
        self.all_right_btn = self.page.locator("a[href='http://www.orangehrm.com']")
        self.social_sites = self.page.locator(".orangehrm-login-footer-sm")
        self.reset_pwd_page = self.page.locator(".oxd-text.oxd-text--h6.orangehrm-forgot-password-title")
        self.dashboard_page = self.page.locator(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
        self.error_msg = self.page.locator(".oxd-text.oxd-text--p.oxd-alert-content-text")

    def check_hrm_logo(self):
        return self.company_logo

    def login_hrm(self,username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def click_forgot_password(self):
        self.forgot_password.click()

    def check_reset_pwd_page(self):
        return self.reset_pwd_page


    def check_copyright_section(self):
        return self.copyright_section

    def click_all_right_btn(self):
        self.all_right_btn.click()

    def check_social_site(self):
        return self.social_sites

    def check_dashboard_page(self):
        return self.dashboard_page

    def check_error_msg(self):
        return self.error_msg
