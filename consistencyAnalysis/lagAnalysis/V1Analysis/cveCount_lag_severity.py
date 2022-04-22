from datetime import date

cve_pdd_diff = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

cve_v2 = {}
cve_v3 = {}
v2 = open('../../Re-cvss_analysis/CVSS3prediction/cvss2-3-cwe-withNullV3.csv', 'rb')
for line in v2:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    v2 = line[1]
    v3 = line[-1]

    if cve not in cve_v2:
        cve_v2[cve] = v2
    if cve not in cve_v3:
        cve_v3[cve] = v3

cve_PredV3 = {}
predictedv3File = open('../../Re-cvss_analysis/predicted2.0.csv', 'rb')
for line in predictedv3File:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    score = float(line[1])
    v3 = ""
    if score == 0:
        v3 = "None"
    elif score < 4.0:
        v3 = "LOW"
    elif score < 7.0:
        v3 = "MEDIUM"
    elif score < 9.0:
        v3 = "HIGH"
    elif score <= 10.0:
        v3 = "CRITICAL"
    if cve not in cve_PredV3:
        cve_PredV3[cve] = v3

    print(score)
exit()
# print(len(cve_v2))
cves = set()
for line in cve_pdd_diff:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[1].rsplit(' ')[0]
    date = line[2].rsplit(' ')[0]
    diff = line[3].rsplit(' ')[0]
    v2 = cve_v2[cve]
    v3 = cve_v3[cve]
    predV3 = cve_PredV3[cve]

    if date > '2018-12-31':
        # with open('../2019Cves.txt', 'a') as foo:
        #     foo.write(str(cve)+'\n')
        continue

    out = str(cve)+';'+str(v2)+";"+str(pdd)+";"+str(diff)+';'+str(v3)+';'+str(predV3)
    with open('./cve2018s_v2_pdd_date_diff_v3_predV3.csv', 'a') as foo:
        foo.write(str(out) + '\n')

print(len(cves))