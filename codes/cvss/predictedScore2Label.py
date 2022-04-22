f0 = open('./CVSS3prediction/cvss2-3-cwe-withNullV3.csv', 'rb')

cve_v3 = {}
for line in f0:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    v3 = line[1]
    cve_v3[cve] = v3

# print(len(cve_v3))
# exit()


f = open('./predicted2.0.csv', 'rb')

for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    score = float(line[1])
    labelV3 = ""
    if score > 0 and score < 4:
        labelV3 = "LOW"
    elif score >= 4 and score < 7:
        labelV3 = "MEDIUM"
    elif score >= 7 and score < 9:
        labelV3 = "HIGH"
    elif score >= 9 and score < 10:
        labelV3 = "CRITICAL"
    else:
        labelV3 = "NONE"
    labelV2 = cve_v3[cve]
    out = cve+","+labelV2+","+labelV3
    with open('./cve_v2_v3.csv', 'a') as foo:
        foo.write(out+'\n')
    # print(line)