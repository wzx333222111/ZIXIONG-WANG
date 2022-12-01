



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
    items = htmll.xpath('//*[@id="main"]/div/div/div/div/div/div/div[1]/a/div/div/div/span/div/text()')
    itemsrt = ""
    # print(items)
    if len(items) >0:
        itemsrt = items[0]
    print("itemsrt" , itemsrt)
    arr.append(itemsrt)
    #                    //*[@id="main"]/div/div/div/div/div/div/div[3]/a/div/div[1]/div/span/div
    owner = htmll.xpath('//*[@id="main"]/div/div/div/div/div/div/div[2]/a/div/div/div/span/div/text()')
    ownerrt = ""
    print(owner)
    if len(owner) > 0:
        ownerrt = owner[0]
    print("ownerrt", ownerrt)
    arr.append(ownerrt)

    FloorPrice = htmll.xpath('//*[@id="main"]/div/div/div/div/div/div/div[3]/a/div/div[1]/div/span/div/text()')
    FloorPriceRt = ""
    print(FloorPrice)
    if len(FloorPrice) > 0:
        FloorPriceRt = FloorPrice[0]
    print("FloorPriceRt", FloorPriceRt)
    arr.append(FloorPriceRt)
    # //*[@id="main"]/div/div/div/div/div/div/div[2]/a/div/div/div/span/div

    prices = htmll.xpath('//div[@class="PriceHistoryStats--stat"]')
    p011 = ""
    p111 = ""


    if len(prices) >=1:
        p00 = prices[0].xpath("./div[1]/text()")
        p01 = prices[0].xpath("./div[2]/text()")
        p10 = prices[1].xpath("./div[1]/text()")
        p11 = prices[1].xpath("./div[2]/text()")
        p011 = p01[0]
        p111 = p11[0]
        print(p00)
        print(p01)
        print(p10)
        print(p11)
    arr.append(p011)
    arr.append(p111)
    # PriceHistoryStats--stat

    # Owners数
    # Floor price

    # 进行相应解码，赋给原标识符（变量）
    # print(htmll)
    # title = htmll.xpath('/html/head/title/text()')#商品主题
    # url = ""
    # urll = htmll.xpath('//meta[@http-equiv="mobile-agent"]/@content')
    # reht = re.compile('format=xhtml; url=(.*)', re.S)
    #
    # if len(urll) > 0:
    #     urlarr = reht.findall(urll[0])
    #     url = urlarr[0]
    # per = htmll.xpath('//div[@class="comment-percent"]/div[@class="percent-con"]/text()')
    # pjj = htmll.xpath('//span[@class=" tag-1"]/text()')
    # pj = ";".join(pjj)
    # # /html/body/div[15]/button[1]/div/div/div/div/div/div/div/div[2]
    # Blockreact__Block-sc-1xf18x6-0 elqhCm item--title
    # name = htmll.xpath('//h1[@class="Blockreact__Block-sc-1xf18x6-0 elqhCm item--title"]/text()')
    #
    # namert = ""
    # if len(name) > 0:
    #     namert = name[0]
    # print("name ", namert)
    # allarr.append(namert)
    # //*[@id="main"]/div/div/div/div[1]/div/div[1]/div[2]/section[1]/div/div[1]/div/a
    # nameAndcollection = htmll.xpath('//div[@class="CollectionLinkreact__DivContainer-sc-gv7u44-0 jMcPQU"]/button')
    # addr = htmll.xpath('//div[@class="CollectionLinkreact__DivContainer-sc-gv7u44-0 jMcPQU"]/a/@href')
    # addrRt = ""
    # collection = 0
    # if len(nameAndcollection) > 0:
    #     collection = 1
    # if len(addr) > 0:
    #     addrRt = addr[0]
    #
    # print("collection addrRt" , addrRt)
    # print("collection " ,collection)
    # allarr.append(addrRt)
    # allarr.append(collection)
    # select = htmll.xpath('//section[@class="item--counts"]')
    # ownerAddrRt = ""
    # ownerRz = 0
    # viewrt = ""
    # favrt = ""
    # item--creator
    # if len(select) > 0:
    #     selectt = select[0]
        # Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 kyhBeu jYqxGr ksFzlZ iXcsEj cgnEmv
        # owner = selectt.xpath(
        #     './div[@class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 kyhBeu jYqxGr ksFzlZ iXcsEj cgnEmv"]')
        #
        # ownerAddr = selectt.xpath(
        #     './div[@class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 kyhBeu jYqxGr ksFzlZ iXcsEj cgnEmv"]/div/a/@href')
        #
        # if len(owner) > 0:
        #     ohtml = tostring(owner[0])
        #     reht = re.compile('<svg', re.S)
        #     rt = reht.findall(str(ohtml))
        #     if len(rt) > 0:
        #         ownerRz = 1
        # if len(ownerAddr) > 0:
        #     ownerAddrRt = ownerAddr[0]
        #
        # print("ownerAddrRt", ownerAddrRt)
        # print("ownerRz " ,ownerRz)
        # allarr.append(ownerAddrRt)
        # allarr.append(ownerRz)
        # view  = selectt.xpath('./div[@class="Blockreact__Block-sc-1xf18x6-0 Countreact__Container-sc-13kp31z-0 cayhdi"]/text()')
        #
        # if len(view) > 0:
        #     viewrt = view[0]
        #
        # print("viewrt " , viewrt)
        # allarr.append(viewrt)
        # fav = selectt.xpath(
        #     './button[@class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL Blockreact__Block-sc-1xf18x6-0 Countreact__Container-sc-13kp31z-0 cayhdi iMVWtI"]/text()')
        #
        # if len(fav) > 0:
        #     favrt = fav[0]
        #
        # print("fav " , favrt)
        # allarr.append(favrt)
        # item--counts
    #
    #
    # creater = htmll.xpath('//section[@class="item--creator"]')
    # createrAddr = htmll.xpath('//section[@class="item--creator"]/div/a[1]/@href')
    # createrrt = 0
    # createrAddrRt = ""
    # if len(creater) > 0:
    #     ohtml = tostring(creater[0])
    #     reht = re.compile('<svg', re.S)
    #     rt = reht.findall(str(ohtml))
    #     if len(rt) > 0:
    #         createrrt = 1
    # if len(createrAddr) > 0:
    #     createrAddrRt = createrAddr[0]
    # print("createrAddr" , createrAddrRt)
    # print("createrrt", createrrt)
    # allarr.append(createrAddrRt)
    # allarr.append(createrrt)
    # alltiomPric = htmll.xpath('//div[@class="PriceHistoryStats--value"]/text()')
    # alltiomPricrt = ""
    # if len(alltiomPric) > 0:
    #     alltiomPricrt = alltiomPric[0]
    # print("alltiomPricrt ", alltiomPricrt)
    # allarr.append(alltiomPricrt)
    # spanSelect = htmll.xpath('//*[@id="main"]/div/div/div/div/div/div/div/section/div/div/div/button/span/text()')
    # about = 0
    # properties = 0
    # levels = 0
    # stats = 0
    #
    # if len(spanSelect) > 0:
    #     string = ";;".join(spanSelect).lower()
    #     reht = re.compile('about', re.S)
    #     aboutrt = reht.findall(string)
    #     if len(aboutrt) > 0:
    #         about = 1
    #     reht = re.compile('properties', re.S)
    #     aboutrt = reht.findall(string)
    #     if len(aboutrt) > 0:
    #         properties = 1
    #     reht = re.compile('levels', re.S)
    #     aboutrt = reht.findall(string)
    #     if len(aboutrt) > 0:
    #         levels = 1
    #     reht = re.compile('stats', re.S)
    #     aboutrt = reht.findall(string)
    #     if len(aboutrt) > 0:
    #         stats = 1
    # print("是否有about",about)
    # print("是否有properties",properties)
    # print("是否有levels",levels)
    # print("是否有stats",stats)
    #
    # allarr.append(about)
    # allarr.append(properties)
    # allarr.append(levels)
    # allarr.append(stats)
    # list = htmll.xpath('//*[@class="BasePanel--body Panel--body"]/div/div/div/div/ul/li[2]/div/div/div/div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--fiat-amount"]/text()')
    # print("list", list)
    # isList = 0
    # listPric = ""
    # if len(list) > 0:
    #     isList = 1
    #     listPric = list[0]
    # print("isList", isList)
    # print("listPric", listPric)
    #
    # allarr.append(isList)
    # allarr.append(listPric)
    # //*[@class="BasePanel--body Panel--body"]/div/div/div/div/ul/li[2]/div[2]/div/div/div[@class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--fiat-amount"]
    # UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL BasePanel--header Panel--header
    # //button[@class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL BasePanel--header Panel--header"]
    # offer = htmll.xpath(
    #     '//div[@class="BasePanel--body Panel--body"]/div/div/div/div/ul/li[2]/div[2]/div/span/text()')
    # print("offer" , offer)
    # isoffer = 0
    # offerPric = ""
    # if len(offer) > 0:
    #     isoffer = 1
    #     offerPric = offer[0]
    # print("isoffer", isoffer)
    # print("offerPric", offerPric)
    # allarr.append(isoffer)
    # allarr.append(offerPric)
    # //div[@class="BasePanel--body Panel--body"]/div/div/div/div/ul/li[2]/div[2]/div/span
    #
    # sale = htmll.xpath(
    #     '//*[@class="BasePanel--body Panel--body"]/div/div/div[2]/div/div/div[2]/div/div/div[2]/text()')
    # print("sale", sale)
    #
    # salepri = ""
    # if len(sale) > 0:
    #     salepri = ";".join(sale)
    #
    # print("salepri", salepri)
    #
    #
    #
    # allarr.append(salepri)
    # //*[@class="BasePanel--body Panel--body"]/div/div/div[2]/div/div/div[2]/div/div/div[2]



    # //*[@id="main"]/div/div/div/div/div/div/div/section/div/div/div/button/span
    # properties //*[@id="Header react-aria-23"]
    # //*[@id="Header react-aria-83"]/span
    # Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isOpen Panel--isFramed

    # Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed



    createrrt = 0
        # PriceHistoryStats--value
        # nameAndcollection[0].xpath("./")
    # print(aa)
    # /html/body/div[17]/button[1]/div/div/div/div/div/div/div/div[2]/span[1]/div/a
    # print("----ffsf")
    # allarr = []
    # for a in aa:
        # print(a)
        # arr = []
        # assets      = a.xpath('./span/a/@href')
        # collection  = a.xpath('./span/div/a/@href')

        #

        # print(a.get_attribute("outerHTML"))

        # 姓名
        # /html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[2]/strong/i
        # price = a.xpath('./div/div/strong/i/text()')

        # name = a.xpath('./div/div/a/em/text()')

        # dpname = a.xpath('./div/div/span/a/text()')

        # pj = a.xpath('./div/div/strong/a/text()')

        # pj = a.xpath('./@content')
        # strr = str(tostring(a ,encoding='utf-8' , pretty_print=True).decode('utf-8'))
        # strr = strr.encode('utf-8')
        # .decode('utf-8')
        # print(str)
        # reht = re.compile('免邮|包邮', re.S)




    return arr

    # return arr


if __name__ == '__main__':
    allarr = []
    filename = "collection"
    lb = "家居"
    for i in range(0 , 15000):
        try:
            print("______"+ str(i))
            arr = getdata('./info2html/collection' + str(i) +'.html')
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



    name = ['itemsrt' ,'ownerrt' , 'FloorPriceRt' ,"All Time Avg. Price" ,"All Time Volume" ]
    test = pandas.DataFrame(columns=name, data=allarr)
    test.to_csv("./csv/" + filename + 'collectioninfo.csv', encoding='utf-8')

