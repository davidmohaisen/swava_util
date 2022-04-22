import os, re
import json, pickle

direct = '../../json_and_csv/nvd_json/'
c,d=0,0
x=0
rejectedVulns = set()
outset = set()
cve_publishedDate = {}
cveVendorWale = set()
vendorNullExcludingRejectsAndnullv2 = set()
v2Nulls, nonNullV2 = set(), set()
v2v3, v2v3Nulled = set(), set()
overallCves = set()
cweNulls, cvssNulls, descNulls, vendorNulls, referenceNulls = set(), set(), set(), set(), set()
tkr = 0
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
        if publishedDate > "2018-12-31":
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

        if "CWE-" in desc:
            print(cve_id, desc)

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

        cwe_idFromDesc = re.findall(r'[CWE-]+\d{1,3}', desc)

        impact = cve_items[i]['impact']
        severity_v2, severity_v3 = "", ""
        if len(impact) != 0:
            severity_v2 = cve_items[i]['impact']['baseMetricV2']['severity']
        if 'baseMetricV3' in impact:
            severity_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseSeverity']

        urlPresent = ""
        reference_data = cve_items[i]['cve']['references']['reference_data']
        for ij in range(len(reference_data)):
            url = reference_data[ij]['url']
            if urlPresent == "":
                urlPresent = url

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
            cvssNulls.add(cve_id)
        if severity_v2 != "":
            nonNullV2.add(cve_id)

        if vendor == "":
            vendorNulls.add(cve_id)
        if cwe_id == "":
            cweNulls.add(cve_id)
        if desc == "":
            descNulls.add(cve_id)
        if urlPresent == "":
            referenceNulls.add(cve_id)
        # print(cve_id, severity_v2, baseScore_v2, exploit_v2, impact_v2, vectorString, exploit_v3, impact_v3, baseScore_v3, cwe_id)
        # out = str(cve_id) + ";" + str(severity_v2) + ";" + str(baseScore_v2) + ";" + str(exploit_v2) + ";" + str(impact_v2) + ";" + str(av) +";"+ str(ac) +";"+ str(au) +";"+ str(confid) +";"+ str(integ) +";"+ str(avail) + ";" + vectorString + ";" + str(accessVector) + ";" + str(accessComplexity) + ";" + str(authentication) + ";" + str(confidentialityImpact) + ";" + str(integrityImpact) + ";" + str(availabilityImpact) + ";" + str(obtainAllPrivilege) + ";" + str(obtainUserPrivilege) + ";" + str(obtainOtherPrivilege) + ";" + str(cwe_id) + ";" + str(baseScore_v3) + ";" + str(severity_v3)
        # # with open('./cvss2-3-cwe.csv', "a") as of:
        # #     of.write(out + '\n')

print(c,d)
print(len(outset))
print(outset)
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

print("NULLS   || Vendor: ", len(vendorNulls), " || CWE: ", len(cweNulls), " || CVSS: ", len(cvssNulls), " || Description: ", len(descNulls), " || Reference Links: ", len(referenceNulls))

# with open('./vendorNulls.pkl', 'wb') as foot:
#     pickle.dump(list(vendorNulls), foot)
# with open('./cweNulls.pkl', 'wb') as foot:
#     pickle.dump(list(cweNulls), foot)
# with open('./cvssNulls.pkl', 'wb') as foot:
#     pickle.dump(list(cvssNulls), foot)
# with open('./descNulls.pkl', 'wb') as foot:
#     pickle.dump(list(descNulls), foot)
# with open('./rejectedVulns.pkl', 'wb') as foot:
#     pickle.dump(list(rejectedVulns), foot)
# with open('./referenceNulls.pkl', 'wb') as foot:
#     pickle.dump(list(referenceNulls), foot)
# for itm in outset:
#     with open('./vendor_prod_info.csv', "a") as of:
#         of.write(itm + '\n')