import json, pickle
vendorVulnCount = open('../../../../vendorCount.csv', 'rb')

f = open('../../output2.0/vendorChains-Final.xlsx', 'rb').read().decode()
# print(f)

vendorVuln = {}
for line in vendorVulnCount:
    line = line.decode().replace('\n', '')
    # print(line)
    # exit()
    tkn = line.rsplit(';')
    vendor = tkn[0]
    vulnCnt = int(tkn[1])
    if vendor not in vendorVuln:
        vendorVuln[vendor] = vulnCnt
    else:
        vendorVuln[vendor] = vendorVuln[vendor] + vulnCnt

print(vendorVuln)
jsonObj = json.loads(f)
print(jsonObj)
# exit()
maxVendor_vendorSet = {}

for key in jsonObj:
    maxCnt = 0
    sumCnt = 0
    out = ""
    maxVendor = ""
    for ven in jsonObj[key]:
        try:
            cnt = int(vendorVuln[ven])
        except:
            cnt = 0
        sumCnt += cnt
        if out == "":
            out = str(ven) + "," + str(cnt)
        else:
            out = out + "," + str(ven) +"," + str(cnt)
        if cnt > maxCnt:
            maxCnt = int(cnt)
            maxVendor = ven
        # print(ven, vendorVuln[ven])
    # print(maxCnt, maxCnt/float(sumCnt), maxVendor, out)
    try:
        rate = maxCnt/float(sumCnt)
        out = str(rate) + ":" + str(maxCnt) + ":" + str(maxVendor) + ":" + out
        # with open('../output2.0/vendorNameConsistent-izerOnVulnCnt.xlsx', 'a') as f:
        #     f.write(out+'\n')

        # print(jsonObj[key])
        for i in range(len(jsonObj[key])):
            inconsVendor = jsonObj[key][i]
            # print(jsonObj[key], inconsVendor)
            if inconsVendor not in maxVendor_vendorSet:
                maxVendor_vendorSet[inconsVendor] = set()
                maxVendor_vendorSet[inconsVendor].add(maxVendor)
            else:
                maxVendor_vendorSet[inconsVendor].add(maxVendor)
    except:
        continue
print("aaya")
print(maxVendor_vendorSet)
# fout = open('./maxVendor_vendorSet.pkl', 'wb')
# pickle.dump(maxVendor_vendorSet, fout)

for itm in maxVendor_vendorSet:
    vendorName = list(maxVendor_vendorSet[itm])[0]
    if len(maxVendor_vendorSet[itm]) > 1:
        print(itm, maxVendor_vendorSet[itm])
x1,x2=0,0
exit()

f1 = open('/media/seal06/HDD/Projects/Vulnerabilities/SWAVA2.0/vendor_prod_info.csv', 'rb')
for line in f1:
    line = line.decode().replace('\n', '')
    tkn = line.rsplit(";")
    cve = tkn[0]
    vend = tkn[1]

    pubDt = tkn[3]
    if pubDt == "":
        print(cve)

    x1+=1
    vendorName = ""
    # for itm in maxVendor_vendorSet:
    if vend in maxVendor_vendorSet:
        vendorName = list(maxVendor_vendorSet[vend])[0]
        # print(cve, vend, vendorName)
        # x2+=1
    if vendorName != "":
        # print(cve, vend, vendorName)
        x2 += 1
    # with open('../../../ConsistentVendor_prod_info.csv', 'a') as foo:
    #     foo.write(str(cve)+";" + str(vend)+";" +str(vendorName)+";" + str(tkn[2])+";"+str(pubDt) + '\n')
print(x1,x2)