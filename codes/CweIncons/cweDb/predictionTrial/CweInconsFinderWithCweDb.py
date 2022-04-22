import os, re
import json
import pickle

f0 = open('../../disclosure_date/Re-PDD/cve_pdd_diff.csv', 'rb')
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
        name_id[name] = []
        name_id[name].append(cwe_id)
    else:
        if cwe_id not in name_id[name]:
            name_id[name].append(cwe_id)

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
            print(cve_id, publishedDate, desc)
            exit()

        cwe_idFromDesc = re.findall(r'CWE-+\d{1,3}', desc)

        if len(cwe_idFromDesc) >= 1:
            out1 = cve_id+":"+cwe_id+":"+re.sub(r'\[|\]|\'', '', str(cwe_idFromDesc)).replace(", ", ',')+":"+publishedDate
            # with open('./cve_cwe_fromDesc_Date-V2', 'a') as oof:
            #     oof.write(out1+'\n')

            # print(cve_id, cwe_id, re.sub(r'\[|\]', '', str(cwe_idFromDesc)).replace(", ", ''))
            # print(desc)
        cweDesc = ""
        found = 0
        for itm in name_id:
            if itm in desc:
                print(itm, name_id[itm])
                print(desc)
                print(cwe_id)
                print("***********************")
                foundInNVD.add(cve_id)
                found = 1
                cdsc = "CWE-"+str(re.sub(r'\[|\]|\'|\"', "", str(name_id[itm]))).replace(", ", ",")
                if cweDesc == "":
                    cweDesc = cdsc
                else:
                    cweDesc = cweDesc+","+cdsc

        if cwe_id == "NVD-CWE-Other" or cwe_id == "NVD-CWE-noinfo": #OtherNoInfo, training
            OtherNoInfo.append([cve_id, str(cwe_id), str(desc)])
            OtherNoInfoStr = str(cve_id)+":"+str(cwe_id)+":"+str(re.sub(r'\:|\\', '', str(desc)).replace('\n', ''))
            with open('./OtherNoInfo.csv', 'a') as fooss:
                fooss.write(OtherNoInfoStr+'\n')
        else:
            training.append([cve_id, str(cwe_id), str(desc)])
            trainingStr = str(cve_id) + ":" + str(cwe_id) + ":" + str(re.sub(r'\:|\\', '', str(desc)).replace('\n', ''))
            with open('./training.csv', 'a') as fooss:
                fooss.write(trainingStr+'\n')

        if cwe_id != "NVD-CWE-Other" and cwe_id != cweDesc:
            if cweDesc == "":
                cweDesc = cwe_id
            else:
                cweDesc = cweDesc+","+cwe_id
                # out2 = cve_id+";"+"CWE-"+str(re.sub(r'\[|\]|\'|\"', "", str(name_id[itm]))).replace(", ", ",")+";"+str(cwe_id)+";"+str(pdd)+";"+str(publishedDate)+";"+str(itm)+";"+re.sub(r'\[|\]|\'', '', str(cwe_idFromDesc)).replace(", ", ',')
                # with open('./cve_cweDb_Cwe_PDD_Date-V2', 'a') as oof:
                #     oof.write(out2 + '\n')
        # if found == 0:
        #     out2 = cve_id + ";" +  str(cwe_id) + ";" + str(desc).replace(";", "").replace("\n", " ") + ";" + str(pdd) + ";" + str(publishedDate) + ";" + re.sub(r'\[|\]|\'', '', str(cwe_idFromDesc)).replace(", ", ',')
        #     Ahmed.append([cve_id, str(cwe_id), str(desc)])

        out3 = cve_id+";"+cwe_id+";"+cweDesc+";"+str(pdd)+";"+str(publishedDate)
        if cve_id in outUniques and (cweDesc == "" or cwe_id == ""):
            continue

        outUniques.add(cve_id)
        with open('./Cons-cve_cweId_CweDb_PDD_Date-V3.xlsx', 'a') as oof:
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
        # print(cve_id, severity_v2, baseScore_v2, exploit_v2, impact_v2, vectorString, exploit_v3, impact_v3, baseScore_v3, cwe_id)
        # out = str(cve_id) + ";" + str(severity_v2) + ";" + str(baseScore_v2) + ";" + str(exploit_v2) + ";" + str(impact_v2) + ";" + str(av) +";"+ str(ac) +";"+ str(au) +";"+ str(confid) +";"+ str(integ) +";"+ str(avail) + ";" + vectorString + ";" + str(accessVector) + ";" + str(accessComplexity) + ";" + str(authentication) + ";" + str(confidentialityImpact) + ";" + str(integrityImpact) + ";" + str(availabilityImpact) + ";" + str(obtainAllPrivilege) + ";" + str(obtainUserPrivilege) + ";" + str(obtainOtherPrivilege) + ";" + str(cwe_id) + ";" + str(baseScore_v3) + ";" + str(severity_v3)
        # # with open('./cvss2-3-cwe.csv', "a") as of:
        # #     of.write(out + '\n')

# OtherNoInfo, training
# with open('./ForThoseNotFoundBeforecve_cwe_desc_pdd_date_cweFromDescOtherNoInfo.pkl', 'wb') as fooss:
#     pickle.dump(OtherNoInfo, fooss)
#
# with open('./ForThoseNotFoundBeforecve_cwe_desc_pdd_date_cweFromDescTraining.pkl', 'wb') as fooss1:
#     pickle.dump(training, fooss1)

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