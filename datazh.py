import pandas

import csv

info = csv.reader(open('./csv2/infov0505.csv', 'r'))
collection = csv.reader(open('./csv2/collectioncollectioninfo.csv', 'r'))
creater = csv.reader(open('./csv2/collectioncreaterAddrcreated.csv', 'r'))
owner = csv.reader(open('./csv2/collectionownerAddrRtcreated.csv', 'r'))

info = [row for row in info]
collection = [[row[1], row[2], row[3], row[4], row[5]] for row in collection]
creater = [[row[1], row[2], row[3], row[4], row[5], row[6]] for row in creater]
owner = [[row[1], row[2], row[3], row[4], row[5], row[6]] for row in owner]
collectionMap = {}
createrMap = {}
ownerMap = {}
for (k, c) in enumerate(info):
    if len(c[2]) > 0 and c[2] not in collectionMap:
        collectionMap[c[2]] = collection[k]
    if len(c[4]) > 0 and c[4] not in ownerMap:
        ownerMap[c[4]] = owner[k]
    if len(c[8]) > 0 and c[8] not in createrMap:
        createrMap[c[8]] = creater[k]
    if k > 100:
        break

allarr = []
collection2 = []
creater2 = []
owner2 = []
# collection
# creater
# owner

for (k, d) in enumerate(info):
    arr = []
    c = collection[k]
    arr.extend(info[k])
    if len(c[1]) > 0:
        arr.extend(c)
    else:
        if info[k][2] in collectionMap:
            arr.extend(collectionMap[info[k][2]])
        else:
            arr.extend(c)

    c = creater[k]

    if len(c[1]) > 0:
        arr.extend(c)
    else:
        if info[k][8] in createrMap:
            arr.extend(createrMap[info[k][8]])
        else:
            arr.extend(c)

    c = owner[k]

    if len(c[1]) > 0:
        arr.extend(c)
    else:
        if info[k][4] in ownerMap:
            arr.extend(ownerMap[info[k][4]])
        else:
            arr.extend(c)
    print(arr)
    allarr.append(arr)
# print(allarr)


name = ["index", 'name', 'collection addrRt', 'has collection', 'ownerAddr', 'owner', 'viewrt', 'fav', 'createrAddr',
        'createrrt', 'alltimePricrt', '是否有about', '是否有properties', '是否有levels', '是否有stats', 'isList', 'listPric',
        'isoffer', 'isofferP', 'salepri',
        'itemsrt', 'ownerrt', 'FloorPriceRt', 'All Time Avg. Price', 'All Time Volume',
        'creater collection','creater','fav','activity','bids','bidmid',
        'owner collection','owner','fav','activity','bids','bids_made'
        ]
test = pandas.DataFrame(columns=name, data=allarr)
test.to_csv('./csv2/0509.csv', encoding='utf-8')
