import csv

import requests







import time

import numpy as np

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
from selenium.common.exceptions import TimeoutException
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
from handledetail import getdata
import re
import time

# /Users/mokai/Desktop/project/pythonProject3/pc-opensea/infohtml
def save_to_file(file_name, contents):
    file_name = file_name.replace("/", ";")
    file_name += ".html"
    file_name = "./info2html/" + file_name
    print(file_name)
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()



def scroll(driver):
    driver.execute_script("""   
        (function () {   
            var y = document.body.scrollTop;   
            var step = 100;   
            window.scroll(0, y);   


            function f() {   
                if (y < document.body.scrollHeight) {   
                    y += step;   
                    window.scroll(0, y);   
                    setTimeout(f, 50);   
                }  
                else {   
                    window.scroll(0, y);   
                    document.title += "scroll-done";   
                }   
            }   


            setTimeout(f, 1000);   
        })();   
        """)




if __name__ == '__main__':
    print(input("输入"))
    url  = "https://opensea.io/activity?search[chains][0]=ETHEREUM&search[eventTypes][0]=AUCTION_SUCCESSFUL"
    #     # getHtml(url)
    # 声明一个CookieJar对象实例来保存cookie
    # saveCookie(url)
    # getCookie(url)
    # getHtmlWithCookie(url)
    # 定义文件名
    option = webdriver.ChromeOptions()  # 实例化option对象
    # option.add_argument("--headless")  # 给option对象添加无头参数
    # option.binary_location = "\browser\Google\Chrome\Application\chrome.exe"

    driver = webdriver.Chrome('chromedriver',  # 实例化浏览器对象,可以指定chromedriver的路径,不指定的话 默认会去找python解释器的同级目录
                              options=option)  # 实例化浏览器对象的时候 把option对象带进来
    print(9999)

    option.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    option.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')


    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'images': 2,
    #     }
    # }
    # option.add_experimental_option('prefs', prefs)

    # print("设置浏览器宽480、高800显示")
    # driver.set_window_size(480, 80000)

    aa = input("输入")

    csv_reader = csv.reader(open('./csv/infov0505.csv', 'r'))
    i = -1
    arrall = []
    infoAllArr = []
    mapp = {}
    mapp[''] = 1
    for row in csv_reader:
        try:
            arr = []
            i += 1
            print("-------------", i)
            if i <= 0:
                continue
            if i >= 5:
                break

            collection = ""
            ownerAddrRt = ""
            createrAddr = ""
            path = "http://opensea.io"
            if len(row[2]) > 1 and row[2] not in mapp:
                mapp[row[2]] = i
                collection      = path + row[2]
                print(collection)
                driver.get(collection)

                # //*[@id="main"]/div/div/div[2]/ul/li[2]
                tex = driver.find_element("xpath" ,'//*[@id="main"]/div/div/div[2]/ul/li[2]')
                tex.click()
                time.sleep(2)
                tex = driver.find_element("xpath", '//*[@id="main"]/div/div/div/div/div/div/div/div/div/div/div/div/input')
                tex.click()
                time.sleep(2)
                tex = driver.find_elements("xpath", '//*[@id="main"]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/ul/li')
                if len(tex) > 0:
                    tex[len(tex) - 1].click()
                # print(tex.get_attribute("outerHTML"))
                # //*[@id="tippy-320"]/div/div/div/ul/li/button/div
                time.sleep(2)
                save_to_file("collection" + str(i), driver.page_source)

            # ?tab=created
            # ?tab=bids
            # ?tab=bids_made
            # "".split()
            if len(row[4]) > 1 and row[4] not in mapp:
                mapp[row[4]] = i
                row4 = row[4].split("?")
                if len(row4) > 1:
                    row[4] = row4[0]
                mapp[row[4]] = i
                ownerAddrRt     = path + row[4] + "?tab=activity"
                print(ownerAddrRt)
                driver.get(ownerAddrRt)
                time.sleep(2)
                save_to_file("ownerAddrRtcreated" + str(i), driver.page_source)


                ownerAddrRt = path + row[4] + "?tab=bids"
                print(ownerAddrRt)
                driver.get(ownerAddrRt)
                time.sleep(2)
                save_to_file("ownerAddrRtbids" + str(i), driver.page_source)


                ownerAddrRt = path + row[4] + "?tab=bids_made"
                print(ownerAddrRt)
                driver.get(ownerAddrRt)
                time.sleep(2)
                save_to_file("ownerAddrRtbids_made" + str(i), driver.page_source)


            if len(row[8]) > 1 and row[8] not in mapp:
                mapp[row[8]] = i
                row8 = row[8].split("?")
                if len(row8) > 1:
                    row[8] = row8[0]
                mapp[row[8]] = i
                createrAddr     = path + row[8]  + "?tab=activity"
                print(createrAddr)
                driver.get(createrAddr)
                time.sleep(2)
                save_to_file("createrAddrcreated" + str(i), driver.page_source)


                createrAddr = path + row[8]+ "?tab=bids"
                print(createrAddr)
                driver.get(createrAddr)
                time.sleep(2)
                save_to_file("createrAddrbids" + str(i), driver.page_source)


                createrAddr = path + row[8]+ "?tab=bids_made"
                print(createrAddr)
                driver.get(createrAddr)
                time.sleep(2)
                save_to_file("createrAddrbids_made" + str(i), driver.page_source)


            arr.append(row[2])
            arr.append(row[4])
            arr.append(row[8])
            arr.append(mapp[row[2]])
            arr.append(mapp[row[4]])
            arr.append(mapp[row[8]])
            arrall.append(arr)


            # driver.get(path)
            #
            # elems = driver.find_elements("xpath" ,'//button[@class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL BasePanel--header Panel--header"]')
            # for e in elems:
            #     tex = e.find_element("xpath" ,"./span")
            #     if tex.text =="Listings":
            #         e.click()
            # time.sleep(3)
            # save_to_file("info" + str(i), driver.page_source)
            # # infoarr = getdata(driver.page_source)
            # # infoAllArr.append(infoarr)
            # arr.append(path)
            # arr.append(i)
            #
        except Exception as e:
            print("error", e)
            continue


    name = ['collection', 'ownerAddrRt' , 'createrAddr' , 'ind1', 'ind2', 'ind3']
    test = pandas.DataFrame(columns=name, data=arrall)
    test.to_csv('./csv/infov2-0505.csv', encoding='utf-8')

    # name = ['name', 'collection addrRt', 'collection', "ownerAddrRt", "ownerRz", "viewrt", "fav", "createrAddr",
    #         "createrrt", "alltiomPricrt ", "是否有about", "是否有properties", "是否有levels", "是否有stats", "isList", "listPric",
    #         "isoffer", "isofferP", "salepri"]
    # test = pandas.DataFrame(columns=name, data=infoAllArr)
    # test.to_csv('./csv/infoAllArr.csv', encoding='utf-8')
    # time.sleep(1)
        # //*[@id="J_bottomPage"]/span[1]/a[2]
        # //*[@id="comment-0"]/div/div/div/a[@class="ui-page-curr"]/following-sibling::*[1]
        # /html/body/div[5]/div[2]/div[2]/div[1]/div/div[3]/div/span[1]/a[3]
        # xyy = driver.find_element("xpath" , '//*[@id="J_bottomPage"]/span/a[@class="curr"]/following-sibling::*[1]')
        # print(driver.get_attribute("outerHTML"))
        # print(xyy.text)

        # save_to_file("list" + str(i), driver.page_source)
        # scroll(driver)
        # xyy.
        # xyy.click()






