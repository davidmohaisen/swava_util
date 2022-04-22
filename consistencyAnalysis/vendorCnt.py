f0 = open('../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')
cve_PDD = {}

for line in f0:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]

    pdd = line[1].rsplit(" ")[0]
    yearPDD = pdd.rsplit("-")[0]
    publishedDate = line[2].rsplit(" ")[0]
    yearPublished = publishedDate.rsplit("-")[0]

    if cve not in cve_PDD:
        cve_PDD[cve] = pdd


f = open('../ConsistentVendor_prod_info.csv', 'rb')

vendor_cve = {}
vendor_prod = {}
pdd_vendor = {}
year_vendor = {}
year_cve = {}
kVendor_cve = {}
cveSet = set()
for line in f:
    line = line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    vendor = line[1]
    consistentVendor = line[2]
    product = line[3]
    publishedDate = line[4]
    pdd = cve_PDD[cve]

    year = pdd.rsplit("-")[0]
    # print(pdd)
    # exit()

    if consistentVendor == "":
        consistentVendor = vendor

    if consistentVendor in vendor_cve:
        vendor_cve[consistentVendor].add(cve)
    else:
        vendor_cve[consistentVendor] = set()
        vendor_cve[consistentVendor].add(cve)

    if consistentVendor in vendor_prod:
        vendor_prod[consistentVendor].add(product)
    else:
        vendor_prod[consistentVendor] = set()
        vendor_prod[consistentVendor].add(product)
    # print(line)
    cveSet.add(cve)

    if pdd in pdd_vendor:
        pdd_vendor[pdd].add(consistentVendor)
    else:
        pdd_vendor[pdd] = set()
        pdd_vendor[pdd].add(consistentVendor)

    if year not in year_vendor:
        year_vendor[year] = set()
        year_vendor[year].add(consistentVendor)
    else:
        year_vendor[year].add(consistentVendor)

    if year not in year_cve:
        year_cve[year] = set()
        year_cve[year].add(cve)
    else:
        year_cve[year].add(cve)

    if int(year) <= 2018:
        if consistentVendor in kVendor_cve:
            kVendor_cve[consistentVendor].add(cve)
        else:
            kVendor_cve[consistentVendor] = set()
            kVendor_cve[consistentVendor].add(cve)



for itm in vendor_cve:
    print(itm, len(vendor_cve[itm]))

exit()

fn = open('../Re-cvss_analysis/CVSS3prediction/cvss2-3-cwe.csv', 'rb')
cveL, cveS = [], {}
for line in fn:
    line= line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    if cve in cveS:
        cveS[cve]+=1
    else:
        cveS[cve] = 1
    # cveS.add(cve)
    cveL.append(cve)
print(len(cveL), len(cveS))
# print(len(cveSet))

for itm in cveS:
    if cveS[itm] > 1:
        print(itm, cveS[itm])