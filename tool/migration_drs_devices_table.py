#!/bin/sh/ python
#coding:utf-8

# MySQLdbのインポート
import MySQLdb


# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    db='')
cursor = connection.cursor()

# ここに実行したいコードを入力します
cursor.execute("SELECT * FROM am--- WHERE deleted_at is NULL")
amazon_drs_devices = cursor.fetchall()

cursor.execute("SELECT * FROM am--")
old_models = cursor.fetchall()

cursor.execute("SELECT * FROM am--")
new_models = cursor.fetchall()

for amazon_drs_device in amazon_drs_devices:
    target_id = amazon_drs_device['a--']

    for old_model in old_models:
        if target_id == old_model['id']:




for new_model in new_models:
    print(new_model)

# # 保存を実行
# connection.commit()

# 接続を閉じる
connection.close()