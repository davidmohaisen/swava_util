f = open('../Re-cvss_analysis/CVSS3prediction/cvss2-3-cwe-withNullV3.csv', 'rb')

lineSet = set()
v2_cve = {}
v3_cve = {}
for line in f:
    line =  line.decode().replace('\n', '')

    tkn = line.rsplit(';')
    cve = tkn[0]
    if cve in lineSet:
        continue

    v2, v3 = tkn[1], tkn[-1]
    # print(tkn[1], tkn[-1])

    if v2 not in v2_cve:
        v2_cve[v2] = set()
        v2_cve[v2].add(tkn[0])
    else:
        v2_cve[v2].add(tkn[0])

    if v3 not in v3_cve:
        v3_cve[v3] = set()
        v3_cve[v3].add(tkn[0])
    else:
        v3_cve[v3].add(tkn[0])
    lineSet.add(cve)


for itm in v2_cve:
    print(itm, len(v2_cve[itm]))

print("********************")
for itm in v3_cve:
    print(itm, len(v3_cve[itm]))