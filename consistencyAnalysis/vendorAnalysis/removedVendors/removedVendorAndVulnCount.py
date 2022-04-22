import json

chain = open('../../../inconsistency/nvd/output2.0/vendorChains-Final.xlsx', 'r')

cnt1 = 0
affectedVends = []

for line in chain:
    f = json.loads(line)
    for itm in f:
        affectedVends.append(f[itm])
#         # print(itm, f[itm])
#         cnt1+=len(f[itm])
#         affectedVends = affectedVends | set(f[itm])
#         print(len(affectedVends))
print(affectedVends)
# exit()
# check the count in inconsistent file and get the one with less #vuln

incons = open('../../../vendor_prod_info.csv', 'r')

vendor_cves = {}
inconsvendor = set()
for line in incons:
    line = line.replace('\n', '')
    year = int(line.rsplit(';')[-1].rsplit('-')[0])
    # print(year)
    if year > 2018:
        continue
    # exit()

    vendor = line.rsplit(';')[1]
    cve = line.rsplit(';')[0]
    if vendor not in vendor_cves:
        vendor_cves[vendor] = set()
        vendor_cves[vendor].add(cve)
    else:
        vendor_cves[vendor].add(cve)
    # print(vendor)
print(vendor_cves)

# handle date condition above

# Removing the most contributing vendor
nahiMila  = set()
RemovedVendor_CveCount = {}
for vendorList in affectedVends:
    maxVendor = ""
    maxVuln = 0
    for ven in vendorList:
        if ven == "":
            continue
        try:
            try:
                vulns = len(vendor_cves[ven])
            except:
                continue
            # print(ven, vulns)
            if ven not in RemovedVendor_CveCount:
                RemovedVendor_CveCount[ven] = (vendor_cves[ven])
            if vulns > maxVuln:
                maxVuln = vulns
                maxVendor = ven
        except:
            nahiMila.add(ven)
            del RemovedVendor_CveCount[ven]
            continue
    # print("Before: ",len(RemovedVendor_CveCount))
    try:
        del RemovedVendor_CveCount[maxVendor]
    except:
        continue
        # print(affectedVends)
        # print(ven)
        # exit()
    # print("Before: ", len(RemovedVendor_CveCount))
print(RemovedVendor_CveCount)
print(nahiMila)

cve_cvss = {}
severity = open('../../../tablesForPaper/severityByYear/cve2018s_v2_pdd_date_diff_v3_predV3-V2.csv')
for line in severity:
    line = line.replace('\n', '')
    cve = line.rsplit(';')[0]
    cvss2 = line.rsplit(';')[1]
    cvss3 = line.rsplit(';')[-1]
    if cve not in cve_cvss:
        cve_cvss[cve] = cvss2
    # print(line)
print(cve_cvss)
cvss_Vulns = {}
for itm in RemovedVendor_CveCount:
    for cve in RemovedVendor_CveCount[itm]:
        cvss = cve_cvss[cve]
        print(cvss_Vulns)

        if cvss not in cvss_Vulns:
            cvss_Vulns[cvss] = 1
        else:
            cvss_Vulns[cvss] += 1
print(cvss_Vulns)
exit()
for itm in RemovedVendor_CveCount:
    print(itm, RemovedVendor_CveCount[itm])
    # with open('./removedVendorsByVulnCount.csv', 'a') as fo:
    #     fo.write(str(itm)+";"+str(len(RemovedVendor_CveCount[itm]))+'\n')