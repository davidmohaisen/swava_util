# f1 = open('./CVE_Day_Lag_cvss2.csv','rb')
#
# f2 = open('./prod_info_out.csv','rb')
#
# have_cvss = []
# no_cvss = []
# for line in f1:
#     line = line.decode()
#     tkn = line.rsplit(',')
#     # print(tkn[0])
#     # exit()
#     have_cvss.append(tkn[0])
#
# print("ye ho gya")
# cnt=0
# for l2 in f2:
#     l2 = l2.decode()
#
#     tkn2 = l2.rsplit(',')
#
#     if tkn2[0] not in have_cvss:
#         no_cvss.append(tkn2[0])
#         cnt+=1
#         print(cnt)
#
# # print(cnt)
# print(len(no_cvss))




#################################################

dir = './NVD_JSON/'

import os
import json

jsons = os.listdir(dir)
no_sev2Cnt = 0
no_sev2CntNoRej = 0
noSev2ButUrl = 0
for z in range(len(jsons)):
    print(jsons[z])
    with open(dir+jsons[z]) as data_file:
        data = json.load(data_file)

    cve_items = data['CVE_Items']

    # year = x[z]

    item_len = len(cve_items)
    # print item_len
    count = 0
    count1 = 0
    for i in range(item_len):
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']

        db_dt1 = cve_items[i]['publishedDate']
        db_dt = db_dt1[:10]

        vendor = []
        product = []
        desc, cwe_id, vendr, prod = "", "", "", ""
        severity_v2, vectorStringV2 = "", ""
        severity_v3, vectorStringV3 = "", ""

        vendor_data = cve_items[i]['cve']['affects']['vendor']['vendor_data']
        for j in range(len(vendor_data)):
            vendor_x = vendor_data[j]['vendor_name']
            # vendor.append(vendor_name)

            product_data = vendor_data[j]['product']['product_data']
            for k in range(len(product_data)):
                product_x = product_data[k]['product_name']

                version_data = product_data[k]['version']['version_data']
                for l in range(len(version_data)):
                    version_value = version_data[l]['version_value']
                    product_name = vendor_x+'|'+product_x+'|'+version_value
                    product.append(product_name)
                    # print(product_name)
        # print(product)


        problemtype_desc = cve_items[i]['cve']['problemtype']['problemtype_data'][0]['description']
        for i2 in range(len(problemtype_desc)):
            cwe_id = cwe_id + ";" + problemtype_desc[i2]['value']

        cwe_id = cwe_id[1:]

        url = cve_items[i]['cve']['references']['reference_data']
        # if len(url) == 0:
        #     print(cve_id)

        description_data = cve_items[i]['cve']['description']['description_data']
        # if len(description_data)>1:
        #     print cve_id
        for k1 in range(len(description_data)):
            desc = desc + ' ' + description_data[k1]['value']

        desc = desc[1:]

        PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_- "
        desc = "".join(c for c in desc if c in PERMITTED_CHARS)

        # if len(vendor)>1:
        #     print cve_id, vendor

        impact = cve_items[i]['impact']
        if len(impact) != 0:
            severity_v2 = cve_items[i]['impact']['baseMetricV2']['severity']
            vectorStringV2 = cve_items[i]['impact']['baseMetricV2']['cvssV2']['vectorString']
            if 'baseMetricV3' in impact:
                severity_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseSeverity']
                vectorStringV3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['vectorString']
                # print(cve_id, severity_v2, vectorStringV2, severity_v3, vectorStringV3)
        else:
            no_sev2Cnt += 1
            if len(url) != 0:
                noSev2ButUrl+=1
                print(cve_id)

        if len(product) != 0:
            # vendr = vendor[0]
            prod = product[0]
            # for w in range(1,len(vendor)):
            #     vendr = vendr+'/'+vendor[w]
            for t in range(1,len(product)):
                prod = prod+'/'+product[t]
        #
        # if desc[1:7] != "REJECT":
        #     # vendr + "," +
        #     out = cve_id + "," + prod + "," + severity_v2 + "," + severity_v3 + "," + vectorStringV2 + "," +vectorStringV3 + "," + db_dt + "," + cwe_id + "," + desc + "\n"
        #     # output_array_creater(out)
        #     # print(out)
        #     # exit()


        if desc[1:7] == "REJECT":
            no_sev2CntNoRej+=1
            # print(cve_id,desc)

print(no_sev2Cnt,no_sev2CntNoRej,noSev2ButUrl)
