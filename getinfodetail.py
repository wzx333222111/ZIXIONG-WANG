import csv

import requests






import csv

import pandas
import re
from selenium import webdriver

import time

# /Users/mokai/Desktop/project/pythonProject3/pc-opensea/infohtml
def save_to_file(file_name, contents):
    file_name = file_name.replace("/", ";")
    file_name += ".html"
    file_name = "./infohtml/" + file_name
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


    aa = input("输入")

    csv_reader = csv.reader(open('./csv/list22.csv', 'r'))
    i = -1
    arrall = []
    infoAllArr = []
    for row in csv_reader:
        try:
            arr = []

            i += 1
            print("-------------", i)
            if i <= 0:
                continue
            print(row[1])
            path = "http://opensea.io" + row[1]
            print(path)
            driver.get(path)
            #
            elems = driver.find_elements("xpath" ,'//button[@class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 btgkrL BasePanel--header Panel--header"]')
            for e in elems:
                tex = e.find_element("xpath" ,"./span")
                if tex.text =="Listings":
                    e.click()
            time.sleep(3)
            save_to_file("info" + str(i), driver.page_source)
            # infoarr = getdata(driver.page_source)
            # infoAllArr.append(infoarr)
            arr.append(path)
            arr.append(i)
            arrall.append(arr)
        except Exception as e:
            print("error", e)
            continue
    name = ['url', 'name']
    test = pandas.DataFrame(columns=name, data=arrall)
    test.to_csv('./csv/infov2.csv', encoding='utf-8')





