import json

venChain = open('../output2.0/vendorChains-Final.xlsx', 'rb')
looseVenChain = open('../Relaxed/outputRel/vendorChains-Final.xlsx', 'rb')

for line in venChain:
    line = line.decode().replace('\n', '')

    jsonLine = json.loads(line)
    for itm in jsonLine:
        with open('./strictInconsCounts.csv', 'a') as fw:
            fw.write(str(itm)+":"+str(len(jsonLine[itm]))+"\n")

for line in looseVenChain:
    line = line.decode().replace('\n', '')

    jsonLine = json.loads(line)
    for itm in jsonLine:
        with open('./relaxInconsCounts.csv', 'a') as fw:
            fw.write(str(itm) + ":" + str(len(jsonLine[itm])) + "\n")