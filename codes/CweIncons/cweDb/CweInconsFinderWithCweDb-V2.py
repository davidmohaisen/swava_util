import os, re
import json
import pickle

f0 = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')
cve_pdd = {}
for line in f0:
    line = line.decode().replace("\n","").rsplit(";")
    cve = line[0]
    pdd = line[1].rsplit(" ")[0]
    if cve not in cve_pdd:
        cve_pdd[cve] = pdd

f = open('./1000.csv', 'rb')
next(f)
name_id={}
foundInNVD = set()
outUniques = set()
for line in f:
    line = line.decode().replace("\n", '').rsplit(',')

    cwe_id = re.sub(r'\"|\'', '', line[0])
    name = re.sub(r'\"|\'', '', line[1])
    related= re.sub(r'\"|\'', '', line[6])
    if name not in name_id:
        name_id[name] = cwe_id

f1 = open('./1008.csv', 'rb')
next(f1)
for line in f1:
    line = line.decode().replace("\n", '').rsplit(',')

    cwe_id = re.sub(r'\"|\'', '', line[0])
    name = re.sub(r'\"|\'', '', line[1])
    related= re.sub(r'\"|\'', '', line[6])
    if name not in name_id:
        name_id[name] = cwe_id

f2 = open('./699.csv', 'rb')
next(f2)
for line in f2:
    line = line.decode().replace("\n", '').rsplit(',')

    cwe_id = re.sub(r'\"|\'', '', line[0])
    name = re.sub(r'\"|\'', '', line[1])
    related= re.sub(r'\"|\'', '', line[6])
    if name not in name_id:
        name_id[name] = cwe_id

direct = '../../json_and_csv/nvd_json/'
c,d=0,0
x=0
rejectedVulns = set()
outset = set()
cve_publishedDate = {}
cveVendorWale = set()
vendorNullExcludingRejectsAndnullv2 = set()
v2Nulls, nonNullV2 = set(), set()
v2v3 = set()
v2v3Nulled = set()
overallCves = set()
tkr = 0
cweID_Cnt = {}
OtherNoInfo, training = [], []
for file in os.listdir(direct):
    f = open(direct+file)
    data = json.load(f)

    cve_items = data['CVE_Items']
    for i in range(len(cve_items)):
        publishedDate = cve_items[i]['publishedDate'].rsplit("T")[0]
        year = publishedDate.rsplit("-")[0]
        if (publishedDate > "2018-05-17" and "recent" in file) or (publishedDate <= "2018-05-17" and "nvdcve-1.1-2018" in file):
            # print(cve_items[i]['publishedDate'].rsplit("T")[0])
            continue
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']

        description_data = cve_items[i]['cve']['description']['description_data']
        x+=1

        desc, cwe_id = '', ''

        for k1 in range(len(description_data)):
            cve_desc = description_data[k1]['value']
            desc = desc + ' ' + cve_desc


        if '** REJECT **' in desc:
            rejectedVulns.add(cve_id)
            continue

        # if "CWE-" in desc:
        #     print(cve_id, desc)

        # with open('./cve_publishedDate.csv', 'a') as foo:
        #     foo.write(str(cve_id)+";"+str(publishedDate)+"\n")

        cve_publishedDate[cve_id] = publishedDate
        vendor, product = "", ""
        try:
            vendor_data = cve_items[i]['cve']['affects']['vendor']['vendor_data']
            for j in range(len(vendor_data)):
                vendor_name = vendor_data[j]['vendor_name']
                vendor = vendor_name
                product_data = vendor_data[j]['product']['product_data']
                for k in range(len(product_data)):
                    product_name = product_data[k]['product_name']
                    product = product_name
                    out = cve_id + ';' + str(vendor_name) + ";" + str(product_name) + ";" + publishedDate
                    outset.add(out)
                    cveVendorWale.add(cve_id)

            # print(cve_items[i]['cve']['affects'].keys())
        except:
            if "nvdcve-1.1-2018" in file:
                nodes = cve_items[i]['configurations']['nodes']

                for ij in range(len(nodes)):
                    if len(nodes[ij]) == 1 and list(nodes[ij].keys())[0] == 'operator':
                        continue
                    try:
                        cpe_match = nodes[ij]['cpe_match']
                        for ik in range(len(cpe_match)):
                            uri = cpe_match[ik]['cpe23Uri']
                            vendor = uri.rsplit(":")[3]
                            product = uri.rsplit(":")[4]
                            out = cve_id + ';' + str(vendor) + ";" + str(product) + ";" + publishedDate
                            outset.add(out)
                            cveVendorWale.add(cve_id)
                    except:
                        children = nodes[ij]['children']
                        for ijk in range(len(children)):
                            cpe_match = children[ijk]['cpe_match']
                            for ijkl in range(len(cpe_match)):
                                uri = cpe_match[ijkl]['cpe23Uri']
                                vendor = uri.rsplit(":")[3]
                                product = uri.rsplit(":")[4]
                                # print(cve_id, vendor, product)
                                out = cve_id+';'+str(vendor)+";"+str(product) + ";" + publishedDate
                                outset.add(out)
                                cveVendorWale.add(cve_id)
            c+=1
            # print(cve_items[i])
            # print(file)
            # print(publishedDate)
            # exit()

        overallCves.add(cve_id)
        problemtype_desc = cve_items[i]['cve']['problemtype']['problemtype_data'][0]['description']
        # if len(problemtype_desc) > 1:
        cwe_pre = []

        for i2 in range(len(problemtype_desc)):
            cwe_id_p = problemtype_desc[i2]['value']
            cwe_pre.append(cwe_id_p)

        for x in range(len(cwe_pre)):
            if cwe_id != "":
                cwe_id = cwe_id + "," + cwe_pre[x]
            else:
                cwe_id = cwe_pre[x]

        if cwe_id not in cweID_Cnt:
            cweID_Cnt[cwe_id] = set()
            cweID_Cnt[cwe_id].add(cve_id)
        else:
            cweID_Cnt[cwe_id].add(cve_id)

        try:
            pdd = cve_pdd[cve_id]
        except:
            continue

        cwe_idFromDesc = re.findall(r'CWE-[0-9]*', desc)
        cweDesc = ""
        if len(cwe_idFromDesc) >= 1:
            cweDesc = re.sub(r'\[|\]|\'', '', str(cwe_idFromDesc)).replace(", ", ',')

        cweDb = ""
        found = 0
        for itm in name_id:
            if itm in desc:
                # print(itm, name_id[itm])
                # print(desc)
                # print(cwe_id)
                print("***********************")
                foundInNVD.add(cve_id)
                found = 1
                cdsc = "CWE-"+str(re.sub(r'\'|\"', "", str(name_id[itm]))).replace(", ", ",")
                if cweDb == "":
                    cweDb = cdsc
                else:
                    cweDb = cweDb+","+cdsc
                print(cweDb, cdsc, itm, name_id[itm])

        if cve_id in outUniques and (cweDb == "" or cwe_id == ""):
            continue

        outUniques.add(cve_id)

        pddYear = pdd.rsplit('-')[0]
        NvdYear = publishedDate.rsplit('-')[0]
        out3 = cve_id + ";" + str(pdd) + ";" + str(publishedDate) + ";" + str(pddYear) + ";" + str(NvdYear) + ";" + cwe_id + ";" + cweDb+ ";" + cweDesc
        with open('./cve_pdd_date_pddYear_nvdYear_cweId_cweDb_cweDesc-V2.csv', 'a') as oof:
            oof.write(out3 + '\n')

        impact = cve_items[i]['impact']
        severity_v2, severity_v3 = "", ""
        if len(impact) != 0:
            severity_v2 = cve_items[i]['impact']['baseMetricV2']['severity']
        if 'baseMetricV3' in impact:
            severity_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseSeverity']

        d+=1
        if vendor == "" and severity_v2 != "":
            # print(cve_items[i])
            vendorNullExcludingRejectsAndnullv2.add(cve_id)

            tkr +=1
        if severity_v2  == "":
            v2Nulls.add(cve_id)
            # if vendor != "":
            # print(cve_items[i])
            # exit()
        if severity_v2 != "" and severity_v3 != "":
            v2v3.add(cve_id)
        if severity_v2 == "" and severity_v3 == "":
            v2v3Nulled.add(cve_id)
        if severity_v2 != "":
            nonNullV2.add(cve_id)

print(c,d)
print(len(outset))
# print(outset)
print("Rejected: ", len(rejectedVulns), x)
print(len(cve_publishedDate), len(cveVendorWale))
print(cve_publishedDate.keys() - cveVendorWale)
print(tkr)
print("Rejected: ", len(rejectedVulns))
print("Overall CVEs: ", len(overallCves))
print("vendorNull And Nullv2: ", len(vendorNullExcludingRejectsAndnullv2))
print("Null v2: ", len(v2Nulls))
print("non-null V2: ", len(nonNullV2))
print("Both v2 and v3 non-Null: ", len(v2v3))
print("Both v2 and v3 Null: ", len(v2v3Nulled))
# for itm in cweID_Cnt:
#     with open('./cweID_cnt.txt', 'a') as ood:
#         ood.write(str(itm)+":"+str(len(cweID_Cnt[itm]))+"\n")
print("foundInNVD", len(foundInNVD))
print(len(outUniques))
# for itm in outset:
#     with open('./vendor_prod_info.csv', "a") as of:
#         of.write(itm + '\n')