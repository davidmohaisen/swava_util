import json
from pprint import pprint
import csv
import os

direct = "./NVD_JSON/"

f = open('/media/seal06/HDD/Projects/Vulnerabilities/SWAVA/disclosure_date/pddate/cve_public_distribution_date_20081.csv')

cveDated = []
for lines in f:
    lines = lines.replace('\n', '')
    cve = lines.rsplit(',')[0]
    # print(cve)
    if cve not in cveDated:
        cveDated.append(cve)

print(len(cveDated))

dbdt_list = []
cveList = []
x=0
for file in os.listdir(direct):
    # print(file)
    if file == "nvdcve-1.0-recent.json":
        continue

    with open(direct+file) as data_file:
        data = json.load(data_file)

    cve_items=data['CVE_Items']
    #parse_json('null',cve_items)

    item_len = len(cve_items)
    #print item_len
    count, cnt = 0, 0
    for i in range(item_len):
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']
        count += 1
        x+=1
        if cve_id not in cveDated and cve_id not in cveList:
            cveList.append(cve_id)
            print(cve_id)

    print(count, x)
        # count = count+1
        # cvss2 = cve_items[i]['impact']['baseMetricV2']['severity']
        # db_dt1 = cve_items[i]['publishedDate']
        # db_dt = db_dt1[:10].lstrip().rstrip()
        # if db_dt not in dbdt_list:
        #     dbdt_list.append(db_dt)
        # # print(db_dt)
        #
        # if db_dt == "":
        #     cnt+=1
            # print(db_dt)
        # print db_dtprint(

#         vendor_data = cve_items[i]['cve']['affects']['vendor']['vendor_data']
#         for j in range(len(vendor_data)):
#             vendor_name = vendor_data[j]['vendor_name']
#
#             product_data = vendor_data[j]['product']['product_data']
#             for k in range(len(product_data)):
#                 product_name = product_data[k]['product_name']
#
#                 version_data = product_data[k]['version']['version_data']
#                 for l in range(len(version_data)):
#                     version = version_data[l]['version_value']
#
#                     out = cve_id+","+vendor_name+","+product_name+","+version+","+db_dt+"\n"
#                     print(out)
#                     # output_array_creater(out)
#
#                       # print cve_id, vendor_name , product_name, version, db_dt
#
#         problemtype_data = cve_items[i]['cve']['problemtype']['problemtype_data']
#         for i1 in range(len(problemtype_data)):
#
#             for i2 in range(len(problemtype_data[i1]['description'])):
#                 cwe_id = problemtype_data[i1]['description'][i2]['value']
#
#         reference_data = cve_items[i]['cve']['references']['reference_data']
#         for j1 in range(len(reference_data)):
#             url = reference_data[j1]['url']
#
#         description_data = cve_items[i]['cve']['description']['description_data']
#         # if len(description_data)>1:
#         #     print cve_id
#         for k1 in range(len(description_data)):
#             cve_desc = description_data[k1]['value']
#             if cve_desc[3:9] == "REJECT":
#                 count = count+1
#
# print(cnt)
# print(count)
# print(dbdt_list)


# cveList = set(cveList)
# cveDated = set(cveDated)
# print(cveList-cveDated)
# print(len(cveList-cveDated))
