f = open('./ConsistentVendor_prod_info.csv', 'rb')
pddFile = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

cve_pdd = {}
for line in pddFile:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[1]
    if cve not in cve_pdd:
        cve_pdd[cve] = pdd

vendor_product= {}
vendor_cve = {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    # print(line)
    cve = line[0]
    vendor = line[1]
    product = line[-2]
    date = line[-1]

    if vendor not in vendor_cve:
        vendor_cve[vendor] = set()
        vendor_cve[vendor].add(cve)
    else:
        vendor_cve[vendor].add(cve)

    if vendor not in vendor_product:
        vendor_product[vendor] = set()
        vendor_product[vendor].add(product)
    else:
        vendor_product[vendor].add(product)

for itm in vendor_cve:
    print(itm, len(vendor_cve[itm]), len(vendor_product[itm]))
    out = str(itm)+";"+str(len(vendor_cve[itm]))+";"+str(len(vendor_product[itm]))
    with open('./vendor_vulnCount_prodCount.csv', 'a') as foo:
        foo.write(out+'\n')