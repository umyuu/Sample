# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import argparse
import codecs
import sys
from contextlib import closing
import pprint

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)


class Scraper:
    def __init__(self):
        self.target_url = "https://antlion.xsrv.jp/"
        self.driver = webdriver.PhantomJS()
        self.DELAY_SLEEP = 1  # sec

    def close(self):
        if self.driver is not None:
            self.driver.close()
            self.driver = None

    def scrap(self, jan):
        v = {}
        v['jan'] = jan
        try:
            self.driver.implicitly_wait(self.DELAY_SLEEP)
            # JAN code
            self.driver.get(self.target_url)
            self.driver.implicitly_wait(self.DELAY_SLEEP)
            elem = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/form/input[2]')
            elem.send_keys(jan)
            elem = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/form/input[3]')
            elem.click()
            elems = self.driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[5]/ul/li')
            for e in elems:
                desc = e.get_attribute('textContent')
                if desc.startswith("ASIN"):
                    v['asin'] = desc.split()[-1]
        except NoSuchElementException:
            print("not available")
        except Exception as e:
            print(e)

        return v


def get_input(debug=True):
    if debug:
        class MimicArgs:
            def __init__(self):
                self.jan = ['9781449355739', '9784873117584', '9784873112992']
        return MimicArgs()
    parser = argparse.ArgumentParser(description='Get asin from JANJAN_URL')
    parser.add_argument('--jan', nargs='+')
    return parser.parse_args()


def main():
    args = get_input()
    pp = pprint.PrettyPrinter()
    with closing(Scraper()) as sc:
        for jan in args.jan:
            products = sc.scrap(jan)
            pp.pprint(products)


if __name__ == "__main__":
    main()
