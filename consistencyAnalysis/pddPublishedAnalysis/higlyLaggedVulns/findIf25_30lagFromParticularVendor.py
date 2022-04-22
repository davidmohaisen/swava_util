import re
f0 = open('./lagbetween25to30days.txt', 'rb')
cveSet = set()
for line in f0:
    line = re.sub(r'\ |\'|"', '', line.decode()).rsplit(',')
    cveSet = set(line)
    # print(line)
    # exit()

vendor_prod = {}
f = open('../../../vendor_prod_info.csv', 'rb')
for line in f:
    line = line.decode().replace("\n", '').rsplit(";")
    cve = line[0]
    vendor = line[1]
    # consVendor = line[2]
    # if consVendor != "":
    #     vendor = consVendor
    product = line[2]
    if vendor not in vendor_prod:
        vendor_prod[vendor] = set()
        vendor_prod[vendor].add(product)
    else:
        vendor_prod[vendor].add(product)
    rest = ";".join(line[1:-1])
    # if cve in cveSet and ("drupal" in rest or "wp" in rest or "wordpress" in rest):
    #     print(line)
# exit()

for itm in vendor_prod:
    print(itm, len(vendor_prod[itm]))