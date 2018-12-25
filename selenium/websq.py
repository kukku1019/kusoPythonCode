#!/usr/bin/env python
# -*- coding = utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import datetime


class open(object):
    """docstring for open."""
        url = ""

    def __init__(self, web):
        super(open, self).__init__()
        self.web = web

    def open():
        """webbrowser for open."""
        web = webdriver.Firefox()
        web.maximize_window()
        web.get(url)
        return web


if __name__ == '__main__':
    while True:
        l = open.open()
        print(l.title)
        print("############")
        l.close()
