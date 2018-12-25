#!/usr/bin/env python
# -*- coding = utf-8 -*-
import time as t


class MyTimer:
    def __init__(self):
        self.unit = ["年", "月", "日", "時", "分", "秒"]
        self.prompt = "カウントスタートできてません"
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 開始
    def start(self):
        self.begin = t.localtime()
        self.prompt = "stop()を使ってカウントを止めてください"
        print("カウント開始")
    # 停止

    def stop(self):
        if not self.begin:
            print("start()を使って開始してください")
        self.end = t.localtime()
        self._calc()
        print("カウント終了")

    # 内部方法、計算運用時間
    def _clac(self):
        self.lasted = []
        self.prompt = "合計時間"
        for index in range(6): ı
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index] + self.unit[index])

if __name__ == '__main__':
    t1=MyTimer()
    t1.start()

