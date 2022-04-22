import pandas as pd, re

f1 = open('./cve_cwe_cwedb_cwedesc_ConsistentCwe.csv', 'rb')
consCwe_cve = {}
cve_cwe, cve_consCwe = {}, {}
for line in f1:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    cwe = line[1]
    Conscwe = line[4]
    if Conscwe not in consCwe_cve:
        consCwe_cve[Conscwe] = set()
        consCwe_cve[Conscwe].add(cve)
    else:
        consCwe_cve[Conscwe].add(cve)

    if cve not in cve_cwe:
        cve_cwe[cve] = cwe

    if cve not in cve_consCwe:
        cve_consCwe[cve] = Conscwe


f = open('./cve2018s_v2_pdd_date_diff_v3_predV3-V2.csv', 'rb')
year_cve = {}
cve_v2, cve_v3, cve_predV3 = {}, {}, {}
year_cwe, year_ConsCwe = {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    v2 = line[1]
    discYear = line[2].rsplit('-')[0]
    v3 = line[-2]

    cwe = cve_cwe[cve]
    conscwe = cve_consCwe[cve]
    if conscwe == "":
        conscwe = cwe
    predV3 = line[-1]
    if predV3 == "":
        predV3 = v3

    if cve not in cve_predV3:
        cve_predV3[cve] = predV3

    if discYear not in year_cwe:
        year_cwe[discYear] = set()
        year_cwe[discYear].add(cwe)
    else:
        year_cwe[discYear].add(cwe)

    if discYear not in year_ConsCwe:
        year_ConsCwe[discYear] = set()
        year_ConsCwe[discYear].add(conscwe)
    else:
        year_ConsCwe[discYear].add(conscwe)

for year in year_ConsCwe:
    print(year, len(year_ConsCwe[year]), len(year_cwe[year]))
exit()
cwe_severity = {}
for cwe in consCwe_cve:
    cves = consCwe_cve[cwe]

    predV3_cve, predV3_cveCount = {}, {}
    for cve in cves:
        predV3 = cve_predV3[cve]
        if predV3 not in predV3_cve:
            predV3_cve[predV3] = set()
            predV3_cve[predV3].add(cve)
        else:
            predV3_cve[predV3].add(cve)

    for predV3 in predV3_cve:
        if predV3 not in predV3_cveCount:
            predV3_cveCount[predV3] = len(predV3_cve[predV3])

    if cwe not in cwe_severity:
        cwe_severity[cwe] = predV3_cveCount

for itm in cwe_severity:
    severity = re.sub(r'\{|\}|\'|\"', '', str(cwe_severity[itm])).replace(', ', ',')
    vulnCount = len(consCwe_cve[itm])
    try:
        critical = cwe_severity[itm]['CRITICAL']
    except:
        critical = 0
    try:
        high = cwe_severity[itm]['HIGH']
    except:
        high = 0
    try:
        medium = cwe_severity[itm]['MEDIUM']
    except:
        medium = 0
    try:
        low = cwe_severity[itm]['LOW']
    except:
        low = 0

    out = itm+";"+str(vulnCount)+";"+str(critical)+";"+str(high)+";"+str(medium)+";"+str(low)
    with open('./cwe_VulnCount_Severity.csv', 'a') as foo:
        foo.write(out+'\n')
    print(itm, len(consCwe_cve[itm]), critical, high, medium, low)