from playwright.sync_api import Playwright,Page,expect
from config import base_url, username, password
from pages.login_page import Login
import pytest
import os
import allure
import time
import json
import pandas as pd
import csv

def pytest_sessionstart(session):
    os.makedirs("reports/allure-results", exist_ok=True)

    with open("reports/allure-results/environment.properties", "w") as f:
        f.write("Browser=Chromium\n")
        f.write("Framework=playwright + pytest\n")
        f.write("Environment=stage\n")


os.makedirs("screenshot", exist_ok=True)
os.makedirs("trace",exist_ok=True)

@pytest.fixture(scope="function")
def page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page

    trace_path = f"trace/file.zip"
    context.tracing.stop(path='trace/file.zip')

    allure.attach.file(
        trace_path,
        name="Playwright Trace",
        attachment_type=allure.attachment_type.ZIP
    )
    context.close()
    browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def login_page(page):
    page.goto(base_url)
    login = Login(page)

    login.login_hrm(username,password)
    page.wait_for_url('**/dashboard/**')

    return page

def login_json_data():
    with open("ddt_files/login_data.json", 'r') as f:
        return json.load(f)


def login_csv_data():
    df = pd.read_csv("ddt_files/login_data.csv")
    return df.to_dict(orient='records')