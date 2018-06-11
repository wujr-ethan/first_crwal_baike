# coding:utf-8
import csv

class StoreDatas(object):
    def __init__(self):
        self.datas = []
    
    def store_datas(self,data):
        if data is None:
            return
        self.datas.append(data)

    def store_as_csv(self):
        header = ['url', 'title', 'description']
        with open('baike.csv', 'w') as f:
            f_csv = csv.DictWriter(f, header)
            f_csv.writeheader()
            f_csv.writerows(self.datas)