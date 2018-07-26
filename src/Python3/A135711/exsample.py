# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import numpy as np
import cv2

def main() -> None:


    l =  np.array([(0, 0),(10, 0),(10, 10),(5, 4)])
    area = cv2.contourArea(l)
    print(area)


    html = """
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type"/>,
    <meta content="text/css" http-equiv="content-style-type"/>, 
    <meta content="驛傳馬車" name="DC.Title"/>, 
    <meta content="アーヴィング" name="DC.Creator"/>, 
    <meta content="青空文庫" name="DC.Publisher"/>
    """
    soup = BeautifulSoup(html, 'html.parser')

    for meta_tag in soup.find_all('meta', attrs={'name': 'DC.Title'}):
        print(meta_tag)
        print(meta_tag.get('content'))


if __name__ == "__main__":
    main()
