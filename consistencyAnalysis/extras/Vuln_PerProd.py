dir = './NVD_JSON/'

import os
import json

vendor_prod, vendor_vuln = {}, {}

jsons = os.listdir(dir)
no_sev2Cnt = 0
no_sev2CntNoRej = 0
noSev2ButUrl = 0
for z in range(len(jsons)):
    print(jsons[z])
    with open(dir+jsons[z]) as data_file:
        data = json.load(data_file)

    cve_items = data['CVE_Items']
    item_len = len(cve_items)

    for i in range(item_len):
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']

        vendor_data = cve_items[i]['cve']['affects']['vendor']['vendor_data']
        for j in range(len(vendor_data)):
            vendor = vendor_data[j]['vendor_name']

            # if vendor == "":
            #     continue
            # else:
            if vendor not in vendor_vuln:
                vendor_vuln[vendor] = set()
                vendor_vuln[vendor].add(cve_id)
            else:
                vendor_vuln[vendor].add(cve_id)

            product_data = vendor_data[j]['product']['product_data']
            for k in range(len(product_data)):
                product = product_data[k]['product_name']

                # out = cve_id + ',' + vendor + ',' + product
                # with open('./VulnVendProd.csv', "a") as of1:
                #     of1.write(str(out) + '\n')

                if vendor not in vendor_prod:
                    vendor_prod[vendor] = set()
                    vendor_prod[vendor].add(product)
                else:
                    vendor_prod[vendor].add(product)

print(len(vendor_vuln), len(vendor_prod))
for itm in vendor_prod:
    prods = len(list(vendor_prod[itm]))
    cves = len(list(vendor_vuln[itm]))

    # if cves != 1:
    #     print(itm, vendor_vuln[itm])

    # print(cves)

    avg = float(cves) / float(prods)
    #
    out = itm+','+str(cves)+','+str(prods)+','+str(avg)
    with open('./VendorProdCveCountAvg.csv', "a") as of1:
        of1.write(str(out) + '\n')
    #
    # #
    # # out1 = itm+','+str(avg)
    # # with open('./VendorAvg.csv', "a") as of:
    # #     of.write(str(out1) + '\n')
    #
    # print(itm, avg)
