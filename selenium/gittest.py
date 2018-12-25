#!/usr/bin/env python
# -*- coding = utf-8 -*-

from selenium import webdriver
import time
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Key
version = "0"
# アクセス先
url = ""
gitid = ''
gitpw = ''


def broser():
    pass


def opFirefox():
                # ブラウザの起動
    driver = webdriver.Firefox()
    # ウィンドウの最大化
    driver.maximize_window()

    # Web サイトへのアクセス
    driver.get(url)

    # Web サイトのタイトルを取得
    print(driver.title)

    # id が emailの部分を見つける
    mail = driver.find_element_by_id('user_login')
    # id が passの部分を見つける
    passwd = driver.find_element_by_id('user_password')
    # emailを入力
    mail.send_keys(gitid)
    # passを入力
    passwd.send_keys(gitpw)
    # 送信
    passwd.submit()
    # driver.get(url+"dashboard/projects")
    time.sleep(5)
    driver.get(url + "projects/new")
    # new　project pass を決める部分IDを探す
    newpjname = driver.find_element_by_id('project_path')
    # new project コメントのID部分を探す
    pjcoment = driver.find_element_by_id('project_description')
    print("pjnameを入力")
    newpjname.send_keys(input())
    print("pjの説明を入力")
    pjcoment.send_keys(input())
    print("ニュープロジェクト作成しました")
    pjcoment.submit()

    # プロジェクトリスト
    # driver.get(url + "admin/projects")
    # findpj = driver.find_element_by_id('project-filter-form')
    # print("削除したいプロジェクトを入力")
    # findpj.send_keys(input())
    # findpj.submit
    # delete = driver.find_elements_by_class_name('project-row')
    # print(delete)
    # delete.send_keys("delete")
    # delete.submit

    print("end")


def makeProject():
    pass


def deleteProject():
    pass


if __name__ == '__main__':
    opFirefox()
