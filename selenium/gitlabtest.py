#!/usr/bin/env python
# -*- coding = utf-8 -*-
# 2017/10/04/ nipara
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml.html

class start(object):
    """docstring for start."""

    def __init__(self, url):
                # ブラウザ起動　ベースオブジェクト
        self.url = url
        self.web = webdriver.Firefox()
        self.web.get(self.url)

    def end(self):
                # ブラウザを閉じる
        self.web.close()

    def title(self):
                # サイトのタイトルを取得
        t = self.web.title
        print(t)
        return t

    def login(self, usr, pswd):
        us = self.web.find_element_by_id('user_login')
        ps = self.web.find_element_by_id('user_password')
        us.send_keys(usr)
        ps.send_keys(pswd)
        ps.submit()

    def move(self, go):
        self.web.get(go)
    def html(self):
        h=self.web.page_source.encode('utf-8')
        soup = BeautifulSoup(h, "lxml")
        return soup

if __name__ == '__main__':
    try:
        url = "www.google.com"
        usr = ""
        pswd = ""
        w = start("http://" + url)
        ht=w.html()
        #tit=w.title()
        t=open("text.txt","a")
        t.write(str(ht)+"\n")
        t.close()
    except:
        raise ("error")
    finally:
        w.end()
    #Sw.login(usr, pswd)
    #    w.move(usl + "dashboard/projects")

    # w.end()
