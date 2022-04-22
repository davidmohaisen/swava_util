# f = open('./ConsistentVendor_prod_info-Pre.csv', 'rb')
f = open('./ConsistentVendor_prod_info.csv', 'rb')
pddFile = open('./cve2018s_v2_pdd_date_diff_v3_predV3.csv', 'rb')

cve_pdd = {}
for line in pddFile:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[2]
    if cve not in cve_pdd:
        cve_pdd[cve] = pdd

x = 0
cves = set()
vendors, consvendors, products = set(), set(), set()
checkPre, checkPost = set(), set()
checkPre2, checkPost2 = set(), set()
pdd_vendorCount, pddYear_vendorCount, vendor_Vuln = {}, {}, {}
pddYear_PrevendorCount = {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    x+=1
    Ndate = line[-1]
    vendor = line[1]
    cve = line[0]
    consven = line[2]
    product = line[3]

    pdd = cve_pdd[cve]
    year = pdd.rsplit('-')[0]

    if year not in pddYear_PrevendorCount:
        pddYear_PrevendorCount[year] = set()
        pddYear_PrevendorCount[year].add(vendor)
    else:
        pddYear_PrevendorCount[year].add(vendor)

    if consven != "":
        checkPre2.add(vendor)
        checkPost2.add(consven)
    if Ndate > '2018-12-31':
        continue

    cves.add(cve)
    vendors.add(vendor)
    consvendors.add(consven)
    products.add(product)
    if consven != "":
        checkPre.add(vendor)
        checkPost.add(consven)
    if vendor != consven and consven != "":
        # print(vendor, consven)
        vendor = consven

    if pdd not in pdd_vendorCount:
        pdd_vendorCount[pdd] = set()
        pdd_vendorCount[pdd].add(vendor)
    else:
        pdd_vendorCount[pdd].add(vendor)

    if year not in pddYear_vendorCount:
        pddYear_vendorCount[year] = set()
        pddYear_vendorCount[year].add(vendor)
    else:
        pddYear_vendorCount[year].add(vendor)

    if vendor not in vendor_Vuln:
        vendor_Vuln[vendor] = set()
        vendor_Vuln[vendor].add(cve)
    else:
        vendor_Vuln[vendor].add(cve)

#
print("Vulnerabilities: ", len(cves), x)
print("Vendors: ", len(vendors), x)
print("ConsVendors: ", len(consvendors), x)
print("Products: ", len(products), x)

print("Pre: ", len(checkPre), "Post: ", len(checkPost), "Precount: ", len(checkPost2))
print((checkPre2-checkPre))

# Vulnerabilities:  109772 210491
# Vendors:  19235 210491
# ConsVendors:  872 210491
# Products:  45983 210491
# Conses:  19235 210491
# Pre:  1845 Post:  871

# for itm in pdd_vendorCount:
#     out = str(itm+";"+str(len(pdd_vendorCount[itm])))
#     with open('./pdd_Vendor.csv', 'a') as foo:
#         foo.write(out+'\n')
#
# for itm in pddYear_vendorCount:
#     out = str(itm)+";"+str(len(pddYear_vendorCount[itm]))+";"+str(len(pddYear_PrevendorCount[itm]))
#     with open('./pddYear_InconConsVendor.csv', 'a') as foo:
#         foo.write(out+'\n')

# for itm in vendor_Vuln:
#     out = str(itm+";"+str(len(vendor_Vuln[itm])))
#     with open('./vendor_VulnCount.csv', 'a') as foo:
#         foo.write(out+'\n')