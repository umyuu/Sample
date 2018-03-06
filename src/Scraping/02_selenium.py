# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path


def get_options() -> Options:
    options = Options()
    # UIを表示しない。
    options.add_argument('--headless')
    options.add_argument('--verbose')
    return options


def main():
    driver_path = r'C:\selenium\chromedriver'
    log_path = str(Path(__file__).with_name("chromedriver.log"))
    driver = webdriver.Chrome(driver_path, chrome_options=get_options(), service_args=[f"--log-path={log_path}"])
    driver.get("https://www.google.co.jp/")
    driver.save_screenshot('screen.png')


if __name__ == '__main__':
    main()
