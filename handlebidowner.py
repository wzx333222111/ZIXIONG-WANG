



from lxml.html import fromstring, tostring
import time
import csv
from lxml import etree
import jieba.analyse
import requests
from urllib3.util import url
import pandas
import re
from selenium import webdriver
import http.cookiejar
import urllib.request
import chardet   #需要导入这个模块，检测编码格式


def getdata(name):
    arr = []
    # htmll = etree.parse(name, etree.HTMLParser())
    f = open(name, encoding="utf-8")
    # 输出读取到的数据
    text = f.read()
    f.close()

    # encode_type = chardet.detect(text)
    # text = text.decode(encode_type['encoding'])
    htmll = etree.HTML(text)
    # 是否有twitter链接
    # 总items数
    #//*[@id="main"]/div/div/div/div/div/div/div/div/div/p
    collection = htmll.xpath('//*[@id="main"]/div/div/div[1]/ul/li[1]/a/div/span/text()')
    collectionrt = ""
    # print(items)
    if len(collection) >0:
        collectionrt = collection[0]
    print("collectionrt" , collectionrt)
    arr.append(collectionrt)

    collection = htmll.xpath('//*[@id="main"]/div/div/div/ul/li[2]/a/div/span/text()')
    collectionrt = 1
    print(collection)
    if len(collection) > 0:
        collectionr = collection[0]
        if collectionr == "0":
            collectionrt = 0
    print("creater" , collectionrt)
    arr.append(collectionrt)

    collection = htmll.xpath('//*[@id="main"]/div/div/div[1]/ul/li[3]/a/div/span/text()')
    collectionrt = ""
    # print(items)
    if len(collection) >0:
        collectionrt = collection[0]
    print("fav" , collectionrt)
    arr.append(collectionrt)
    # //*[@id="main"]/div/div/div/div/div/div/div/div/div/div/div/div/div/img
    collection = htmll.xpath('//div[@class="Orders--no-data-text"]/text()')
    collectionrt = "y"
    # print(items)
    if len(collection) >0:
        collectionrt = collection[0]
    print("activity" , collectionrt)
    arr.append(collectionrt)


    # //*[@id="main"]/div/div/div[3]/div/div[3]/div[2]/div/p
    return arr

    # return arr


if __name__ == '__main__':
    allarr = []
    filename = "collection"
    lb = "家居"
    for i in range(0 , 15000):
        try:
            print("______"+ str(i))
            arr = getdata('./info2html/ownerAddrRtbids' + str(i) +'.html')
            allarr.append(arr)
        except Exception as e :
            allarr.append([])
            print("------------****" , e)
            continue

    print(len(allarr))
    # kk = [";".join(i) for i in allarr]
    # kk = list(set(kk))
    # print(len(kk))
    # # print(kk)
    # bb = []
    # for i in kk:
    #     # print(i)
    #     b =i.split(";")
    #     bb.append(b)



    name = ['collection' ,'creater' , 'fav' ,"ownerAddrbids" ]
    test = pandas.DataFrame(columns=name, data=allarr)
    test.to_csv("./csv/" + filename + 'ownerAddrbids.csv', encoding='utf-8')

