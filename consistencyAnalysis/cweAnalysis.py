f1 = open('../../SWAVA2.0/Re-cvss_analysis/CVSS3prediction/cvss2-3-cwe-withNullV3.csv', 'rb')
f2 = open('../../SWAVA2.0/disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

cveSet = {}
yearSet = set()
for line in f2:
    line = line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    # cveSet.add(cve)
    pdd = line[1].rsplit(" ")[0]
    publishedDate = line[2].rsplit(" ")[0]
    year = publishedDate.rsplit("-")[0]
    yearSet.add(year)
    cveSet[cve] = publishedDate

# print(yearSet)
x=0
cweList = {}
for line in f1:
    line = line.decode().replace("\n", "").rsplit(";")
    cve = line[0]
    if cve not in cveSet:
        continue
    cweid = line[-3]
    year = cveSet[cve].rsplit("-")[0]
    # print(cweid)
    if int(year) == 2010:
        if cweid not in cweList:
            cweList[cweid] = 1
        else:
            cweList[cweid] += 1
    x+=1

print(x)
for itm in cweList:
    print(itm, cweList[itm])