#!/bin/sh/ python
#coding:utf-8
import pandas as pd
import pathlib
import os
import sys

class DrsProducts():
    def __init__(self):
        self.PDObj = ''

    def readCSV(self):
        os.chdir("/Users/---/workspace/CSVTOSQL")
        fileName= str(sys.argv[1])
        self.PDObj = pd.read_csv(fileName, encoding='UTF-8')

    def makeSQL(self):
        with open('NEWDRSPRODUCTSQL.txt','w') as newFile:
            for index,row in self.PDObj.iterrows():
                print(index)
                print(row['SS ASIN追加作業'])
                SQL = 'INSERT INTO amazon_drs_products ' \
                      '(asin, title, weight, weight_unit,category, medium_image_url, updated_at, created_at, deleted_at)' \
                      'VALUES ("{asin}","{title}",{weight},"{weight_unit}","{category}","",NOW(),NOW(),NULL);' \
                      '\n'.format(asin=row['ASIN'],title=row['Title'],weight=row['重量'],weight_unit=row['重量単位'],category=row['Model ID'])
                newFile.write(SQL)


if __name__ == "__main__":
    instance = DrsProducts()
    instance.readCSV()
    instance.makeSQL()