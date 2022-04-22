f = open('./cve_vendProd_ConsIncons_pdd_date.csv', 'rb')

cves, vendorsSet, ProdsSet = set(), set(), set()
BefVuln_Vendor, AftVuln_Vendor, BefProd_Vendor, AftProd_Vendor = {}, {}, {}, {}

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

    cves.add(cve)
    vendorsSet.add(incvend)
    ProdsSet.add(incvend+"-"+incprod)



    if incvend not in BefVuln_Vendor:
        BefVuln_Vendor[incvend] = set()
        BefVuln_Vendor[incvend].add(cve)
    else:
        BefVuln_Vendor[incvend].add(cve)

    if consvend not in AftVuln_Vendor:
        AftVuln_Vendor[consvend] = set()
        AftVuln_Vendor[consvend].add(cve)
    else:
        AftVuln_Vendor[consvend].add(cve)

    if incvend not in BefProd_Vendor:
        BefProd_Vendor[incvend] = set()
        BefProd_Vendor[incvend].add(incprod)
    else:
        BefProd_Vendor[incvend].add(incprod)

    if consvend not in AftProd_Vendor:
        AftProd_Vendor[consvend] = set()
        AftProd_Vendor[consvend].add(consprod)
    else:
        AftProd_Vendor[consvend].add(consprod)



# for itm in BefVuln_Vendor:
#     print(itm, len(BefVuln_Vendor[itm]), len(BefProd_Vendor[itm]))
#     out = str(itm)+";"+str(len(BefVuln_Vendor[itm]))+";"+str(len(BefProd_Vendor[itm]))
#     with open('./InconsVulnAndProdPerVendor.csv', 'a') as fo:
#         fo.write(out+'\n')
#
# for itm in AftVuln_Vendor:
#     print(itm, len(AftVuln_Vendor[itm]), len(AftProd_Vendor[itm]))
#     out = str(itm)+";"+str(len(AftVuln_Vendor[itm]))+";"+str(len(AftProd_Vendor[itm]))
#     with open('./ConsVulnAndProdPerVendor.csv', 'a') as foo:
#         foo.write(out+'\n')

print(len(cves), len(vendorsSet), len(ProdsSet))