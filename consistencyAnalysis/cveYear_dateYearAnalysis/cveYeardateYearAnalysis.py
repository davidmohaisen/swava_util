import random

f = open('./cve2018_discDay_NvdDay_pdd_date.csv', 'rb')

disclDiff_cve, nDate_cve, cve_discl, cve_Ndate, cve_CveYear = {}, {}, {}, {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[-2]
    Ndate = line[-1]
    pddYear = int(pdd.rsplit('-')[0])
    NdateYear = int(Ndate.rsplit('-')[0])
    cveYear = int(cve.rsplit('-')[1])
    cveDisclYeardiff = pddYear-cveYear
    cveNVDdateYeardiff = NdateYear - cveYear
    out = cve+";"+pdd+";"+Ndate+";"+str(cveYear)+";"+str(pddYear)+";"+str(cveDisclYeardiff)+";"+str(NdateYear)+";"+str(cveNVDdateYeardiff)
    # with open('./cve_pdd_Ndate_cveYearsDiff.csv', 'a') as foo:
    #     foo.write(out+'\n')
    # print(NdateYear-cveYear)
    if cve not in cve_discl:
        cve_discl[cve] = pdd
    if cve not in cve_Ndate:
        cve_Ndate[cve] = Ndate
    if cve not in cve_CveYear:
        cve_Ndate[cve] = cveYear

    if cveDisclYeardiff not in disclDiff_cve:
        disclDiff_cve[cveDisclYeardiff] = []
        disclDiff_cve[cveDisclYeardiff].append(cve)
    else:
        disclDiff_cve[cveDisclYeardiff].append(cve)

    if cveNVDdateYeardiff not in nDate_cve:
        nDate_cve[cveNVDdateYeardiff] = []
        nDate_cve[cveNVDdateYeardiff].append(cve)
    else:
        nDate_cve[cveNVDdateYeardiff].append(cve)


x=0
for itm in disclDiff_cve:
    if len(disclDiff_cve[itm]) > 20:
        cves = random.sample(disclDiff_cve[itm], 20)
        for i in range(len(cves)):
            cve = cves[i]
            pdd = cve_discl[cve]
            cveYear = cve.rsplit('-')[1]
            out = str(itm)+";"+str(cve)+";"+str(cveYear)+";"+str(pdd)
            with open('./disclDiff_cve_pdd_ForVerification.csv', 'a') as foo:
                foo.write(out+'\n')
    else:
        for i in range(len(disclDiff_cve[itm])):
            cve = disclDiff_cve[itm][i]
            pdd = cve_discl[cve]
            cveYear = cve.rsplit('-')[1]
            out = str(itm) + ";" + str(cve)+";"+str(cveYear)+ ";" + str(pdd)
            with open('./disclDiff_cve_pdd_ForVerification.csv', 'a') as foo:
                foo.write(out + '\n')

        # x+=1

print(x)