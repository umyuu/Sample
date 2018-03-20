import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


def get_url() -> str:
    URLS = ["https://www.google.co.jp/", "https://teratail.com/", "http://www.example.com/"]
    return random.choice(URLS)


def condition(driver) -> bool:
    look_for = ['google', 'treratail', 'example']
    url = driver.current_url
    if any(url.find(s) != -1 for s in look_for):
        print("match:{}".format(url))
        return True

    return False


def main() -> None:
    driver = webdriver.Chrome()
    url = get_url()
    print("req:{}".format(url))
    try:
        driver.get(url)
        try:
            WebDriverWait(driver, timeout=10).until(condition)
            print("done:{}".format(driver.current_url))
        except TimeoutException as ex:
            print("#" * 80)
            print(ex)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
