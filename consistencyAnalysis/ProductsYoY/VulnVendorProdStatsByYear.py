import numpy as np

f = open('./cve_vendProd_ConsIncons_pdd_date.csv', 'rb')

Yearvuln_Prod, Yearvuln_Vendor, year_prod, year_vend = {}, {}, {}, {}
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

    date = line[-1]
    year = date.rsplit("-")[0]

    if year not in year_vend:
        year_vend[year] = set()
        year_vend[year].add(consvend)
    else:
        year_vend[year].add(consvend)


    if year not in year_prod:
        year_prod[year] = set()
        year_prod[year].add(consvend+"-"+consprod)
    else:
        year_prod[year].add(consvend+"-"+consprod)


    if year not in Yearvuln_Vendor:
        Yearvuln_Vendor[year] = {}
        Yearvuln_Vendor[year][incvend] = set()
        Yearvuln_Vendor[year][incvend].add(cve)
    else:
        if incvend not in Yearvuln_Vendor[year]:
            Yearvuln_Vendor[year][incvend] = set()
            Yearvuln_Vendor[year][incvend].add(cve)
        else:
            Yearvuln_Vendor[year][incvend].add(cve)



    # out = str(cve)+";"+str(consvend)+";"+str(consprod)+";"+str(incvend)+";"+\
    #       str(incprod)+";"+str(pddyear)+";"+str(year)+";"+str(pdd)+";"+str(date)
    #
    # with open('./cveConsInconsVendProdPddDate-StatsAnalysis.csv', 'a') as foo:
    #     foo.write(out+"\n")

    # cves.add(cve)
    # vendorsSet.add(incvend)
    # ProdsSet.add(incvend+"-"+incprod)
    # consProdsSet.add(consvend+"-"+consprod)


# for year in year_prod:
#     print(year, len(year_vend[year]), len(year_prod[year]))

for itm in Yearvuln_Vendor:
    values = []
    for itm2 in Yearvuln_Vendor[itm]:
        values.append(len(Yearvuln_Vendor[itm][itm2]))
        # print(itm, itm2, len(Yearvuln_Vendor[itm][itm2]))
    print(itm, len(values), np.average(np.array(values)), np.median(np.array(values)))