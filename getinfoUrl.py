



from lxml import etree

import pandas




def getdata(name , lb):
    # htmll = etree.parse(name, etree.HTMLParser())
    f = open(name, encoding="utf-8")
    # 输出读取到的数据
    text = f.read()
    f.close()

    # encode_type = chardet.detect(text)
    # text = text.decode(encode_type['encoding'])
    htmll = etree.HTML(text)

    # # /html/body/div[15]/button[1]/div/div/div/div/div/div/div/div[2]
    aa = htmll.xpath('//div[@class="Blockreact__Block-sc-1xf18x6-0 dRNFzr fresnel-greaterThanOrEqual-xs"]')
    # print(aa)
    # /html/body/div[17]/button[1]/div/div/div/div/div/div/div/div[2]/span[1]/div/a
    # print("----ffsf")
    allarr = []
    for a in aa:
        # print(a)
        arr = []
        assets      = a.xpath('./span/a/@href')
        collection  = a.xpath('./span/div/a/@href')
        if len(assets) > 0:
            arr.append(assets[0])
        else:
            arr.append("")

        if len(collection) > 0:
            arr.append(collection[0])
        else:
            arr.append("")
        allarr.append(arr)



    return allarr

    # return arr


if __name__ == '__main__':
    allarr = []
    filename = "list"
    lb = "家居"
    for i in range(0 , 14000):
        try:
            # print("______"+ str(i))
            arr = getdata('./html/'+ filename + str(i) +'.html' , lb)
            # print(arr)
            # arr.append(lb)
            # print(arr)
            allarr.extend(arr)
            # print(len(allarr))
            if i%2500 == 2449:
                print("---")
                print(i)
                kkk = [";".join(i) for i in allarr]
                kkk = list(set(kkk))
                print(len(kkk))
        except Exception as e :
            # print("------------****" , e)
            if i%2500 == 2449:
                print("---")
                print(i)
                kkk = [";".join(i) for i in allarr]
                kkk = list(set(kkk))
                print(len(kkk))
            continue

    print(len(allarr))
    kk = [";".join(i) for i in allarr]
    kk = list(set(kk))
    print(len(kk))
    # print(kk)
    bb = []
    for i in kk:
        # print(i)
        b =i.split(";")
        bb.append(b)
    name = ['assets','collection']
    test = pandas.DataFrame(columns=name, data=bb)
    test.to_csv("./csv/" + filename + '223.csv', encoding='utf-8')

