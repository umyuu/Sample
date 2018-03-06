# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys


def main():
    import platform
    print(platform.architecture())
    print(sys.version)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\selenium\chromedriver.exe")

    driver.get('https://www.google.co.jp')
    driver.save_screenshot('screen.png')


if __name__ == "__main__":
    main()
