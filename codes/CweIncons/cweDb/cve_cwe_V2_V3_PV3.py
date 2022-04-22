f = open('./cve_cwe_cwedb_cwedesc_ConsistentCwe.csv', 'rb')
cve_consCwe = {}
cve_CweId = {}

for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cwe = line[1]
    consCwe = line[4]
    cve = line[0]
    if cve not in cve_consCwe:
        cve_consCwe[cve] = set()
        cve_consCwe[cve] = consCwe
    if cve not in cve_CweId:
        cve_CweId[cve] = set()
        cve_CweId[cve] = cwe

f2 = open('../../tablesForPaper/severityByYear/cve2018s_v2_pdd_date_diff_v3_predV3-V2.csv', 'rb')
for line in f2:
    line = line.decode().replace('\n', '').rsplit(';')
    # print(line)
    cve = line[0]
    v2 = line[1]
    v3 = line[-2]
    pv3 = line[-1]
    pdd = line[2]
    date = line[3]
    conscwe = cve_consCwe[cve]
    cwe_id  = cve_CweId[cve]

    out = str(cve)+";"+str(conscwe)+";"+str(cwe_id)+";"+str(v2)+";"+str(v3)+";"+str(pv3)+";"+str(pdd)+";"+str(date)
    with open('./cve_consCwe_cwe_v2v3Pv3_Pdd_date.csv', 'a') as foo:
        foo.write(out+'\n')
    print(out)