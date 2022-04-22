cve_cvss = {}
cve_cvss3, cve_cvssPv3 = {}, {}
severity = open('../../tablesForPaper/severityByYear/cve2018s_v2_pdd_date_diff_v3_predV3-V2.csv')
for line in severity:
    line = line.replace('\n', '')
    # print(line)
    cve = line.rsplit(';')[0]
    cvss2 = line.rsplit(';')[1]
    cvss3 = line.rsplit(';')[-2]
    pv3 = line.rsplit(';')[-1]
    if cve not in cve_cvss:
        cve_cvss[cve] = cvss2
    if cve not in cve_cvss3:
        cve_cvss3[cve] = cvss3
    if cve not in cve_cvssPv3:
        cve_cvssPv3[cve] = pv3
# exit()
f = open('./cve_vendProd_ConsIncons_pdd_date.csv', 'rb')

cvss_cves = {}
pddyear_consven, pddyear_incvend, pddyear_consprod, pddyear_incprod = {}, {}, {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    incvend = line[1]
    incprod = line[2]
    consvend = line[3]
    consprod = line[4]

    if consvend == "":
        consvend = incvend
    if consprod == "":
        consprod = incprod

    pdd = line[5]
    pddyear = pdd.rsplit("-")[0]

    # if incvend != consvend:
    if incprod != consprod:
        cvss = cve_cvss3[cve]

        if cvss not in cvss_cves:
            cvss_cves[cvss] = set()
            cvss_cves[cvss].add(cve)
        else:
            cvss_cves[cvss].add(cve)

for itm in cvss_cves:
    print(itm, len(cvss_cves[itm]))
print(cvss_cves["HIGH"])

# product
# v2
# HIGH 159
# MEDIUM 196
# LOW 27

# pv3
# CRITICAL 54
#  171
# HIGH 109
# MEDIUM 48
# v3
#  211
# HIGH 96
# CRITICAL 14
# MEDIUM 57
# LOW 4


# vendor
# v2
# MEDIUM 2033
# HIGH 1206
# LOW 275

# pv3
# MEDIUM 808
#  782
# HIGH 1124
# CRITICAL 794
# LOW 7

# v3
# 2734
# CRITICAL 125
# HIGH 360
# MEDIUM 293
# LOW 3