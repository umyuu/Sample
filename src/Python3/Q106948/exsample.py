# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def main():
    base_dir = os.path.dirname(__file__)
    chrome_options = Options()
    # ヘッドレスモードを使用したい時は以下の行のコメントを解除してくださいな。
    #chrome_options.add_argument('headless')
    extension_path = os.path.join(base_dir, 'chrome_extension.crx')
    print(extension_path)
    chrome_options.add_extension(extension_path)
    # ChromeのWebDriverオブジェクトを作成する。
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("http://www.yahoo.co.jp")
    searchbox = driver.find_element_by_id("srchtxt")
    searchbox.send_keys("piyo")
    searchbtn = driver.find_element_by_id("srchbtn")
    searchbtn.click()
    driver.save_screenshot('search_results.png')


if __name__ == '__main__':
    main()
