import os, re, random
import json

direct = '../../json_and_csv/nvd_json/'
c,d=0,0
x=0
rejectedVulns = set()
outset = set()
cve_publishedDate = {}
cveVendorWale = set()
overallCves = set()
vendorNullExcludingRejectsAndnullv2, vendorNulls, cweIdNulls, referenceLinkNull, publishedDateNull = set(), set(), set(), set(), set()
v2Nulls, nonNullV2 = set(), set()
v2v3 = set()
v2v3Nulled, v2NotNullv3Null = set(), set()
tkr = 0
for file in os.listdir(direct):
    f = open(direct+file)
    data = json.load(f)

    cve_items = data['CVE_Items']
    for i in range(len(cve_items)):
        publishedDate = cve_items[i]['publishedDate'].rsplit("T")[0]
        year = publishedDate.rsplit("-")[0]
        if (publishedDate > "2018-05-17" and "recent" in file) or (publishedDate <= "2018-05-17" and "nvdcve-1.1-2018" in file) or publishedDate > '2018-12-31':
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

        cwe_idFromDesc = re.findall(r'[CWE-]+\d{1,3}', desc)

        impact = cve_items[i]['impact']
        severity_v2, severity_v3 = "", ""
        if len(impact) != 0:
            severity_v2 = cve_items[i]['impact']['baseMetricV2']['severity']
        if 'baseMetricV3' in impact:
            severity_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseSeverity']

        reference_data = cve_items[i]['cve']['references']['reference_data']
        referenceLink = ""
        for ij in range(len(reference_data)):
            url = reference_data[ij]['url']
            if url != "":
                referenceLink = url

        d+=1
        if vendor == "" and severity_v2 != "":
            # print(cve_items[i])
            vendorNullExcludingRejectsAndnullv2.add(cve_id)

        if vendor == "":
            vendorNulls.add(cve_id)
        if cwe_id == "":
            cweIdNulls.add(cve_id)

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
        elif severity_v2 != "" and severity_v3 == "":
            v2NotNullv3Null.add(cve_id)
        if severity_v2 != "":
            nonNullV2.add(cve_id)

        if referenceLink == "":
            referenceLinkNull.add(cve_id)

        if publishedDate == "":
            publishedDateNull.add(cve_id)


print(c,d)
print(len(outset))
# print(outset)
print("Rejected: ", len(rejectedVulns), x)
print(len(cve_publishedDate), len(cveVendorWale))
# print(cve_publishedDate.keys() - cveVendorWale)
print(tkr)
print("********* Starts *********")
print("Rejected: ", len(rejectedVulns))
print("Overall CVEs: ", len(overallCves))
print("Null v2: ", len(v2Nulls))
print("Both v2 and v3 Null: ", len(v2v3Nulled))
print("Null vendors: ", len(vendorNulls))
print("Null CWE-IDs: ", len(cweIdNulls))
print("Null Published Date: ", len(publishedDateNull))
print("Null reference Links: ", len(referenceLinkNull))
print("********** Granular Details **********")
print("********** Reference Links Details **********")
print("Null Reference Links: ", len(referenceLinkNull))
for cve in referenceLinkNull:
    date = cve_publishedDate[cve]
    with open('./linksNull.csv', 'a') as foo:
        foo.write(str(cve)+";"+str(date)+'\n')
print("With v2", len(referenceLinkNull - v2Nulls))
print("Reference Links null but not V2", random.sample(referenceLinkNull - v2Nulls, 10))
print("With vendor", len(referenceLinkNull - vendorNulls))
print("Reference Links null but not vendor", random.sample(referenceLinkNull - vendorNulls, 10))
print("With CWE-ID", len(referenceLinkNull - cweIdNulls))
print("Reference Links null but not CWE-ID", random.sample(referenceLinkNull - cweIdNulls, 10))
print("********** Reference Links Details Ends **********")
print(len(vendorNulls.union(cweIdNulls.union(referenceLinkNull.union(v2Nulls)))))
exit()
print("********** Vendor Details **********")
print("Null Vendors: ", len(vendorNulls))
for cve in vendorNulls:
    date = cve_publishedDate[cve]
    with open('./vendorNull.csv', 'a') as foo:
        foo.write(str(cve)+";"+str(date)+'\n')
print("With v2", len(vendorNulls - v2Nulls))
print("Vednor vull but not V2", random.sample(vendorNulls - v2Nulls, 10))
print("With reference Links", len(vendorNulls - referenceLinkNull))
print("Vednor vull but not reference Links", random.sample(vendorNulls - referenceLinkNull, 10))
print("With CWE-ID", len(vendorNulls - cweIdNulls))
print("Vednor vull but not CWE-ID", random.sample(vendorNulls - cweIdNulls, 10))
print("********** Vendor Details Ends **********")

print("********** CWE-ID Details **********")
print("Null CWE-IDs: ", len(cweIdNulls))
for cve in cweIdNulls:
    date = cve_publishedDate[cve]
    with open('./CweIdNull.csv', 'a') as foo:
        foo.write(str(cve)+";"+str(date)+'\n')
print("With v2", len(cweIdNulls - v2Nulls))
print("With reference Links", len(cweIdNulls - referenceLinkNull))
print("CWE-ID null but not reference Links", random.sample(cweIdNulls - referenceLinkNull, 10))
print("With vendors", len(cweIdNulls - vendorNulls))
print("********** CWE-ID Details Ends **********")

print("********** Severity Details **********")
print("Null V2: ", len(v2Nulls))
for cve in v2Nulls:
    date = cve_publishedDate[cve]
    with open('./v2Null.csv', 'a') as foo:
        foo.write(str(cve)+";"+str(date)+'\n')
print("With CWE-IDs", len(v2Nulls - cweIdNulls))
print("With reference Links", len(v2Nulls - referenceLinkNull))
print("V2 null but not reference Links", random.sample(v2Nulls - referenceLinkNull, 10))
print("With vendors", len(v2Nulls - vendorNulls))
print("********** Severity Details Ends **********")


print("non-null V2: ", len(nonNullV2))
print("Both v2 and v3 not Null: ", len(v2v3))
print("V3 null but v2 not null: ", len(v2NotNullv3Null))
print("vendorNull And Nullv2: ", len(vendorNullExcludingRejectsAndnullv2))
print("********************************************")

# print("V2 null but not reference Links", random.sample(v2Nulls - referenceLinkNull, 10))
# print("CWE-ID null but not reference Links", random.sample(cweIdNulls - referenceLinkNull, 10))
# print("Vednor vull but not V2", random.sample(vendorNulls - v2Nulls, 10))
# print("Vednor vull but not reference Links", random.sample(vendorNulls - referenceLinkNull, 10))
# print("Vednor vull but not CWE-ID", random.sample(vendorNulls - cweIdNulls, 10))
# print("Reference Links null but not V2", random.sample(referenceLinkNull - v2Nulls, 10))
# print("Reference Links null but not vendor", random.sample(referenceLinkNull - vendorNulls, 10))
# print("Reference Links null but not CWE-ID", random.sample(referenceLinkNull - cweIdNulls, 10))

# for itm in outset:
#     with open('./vendor_prod_info.csv', "a") as of:
#         of.write(itm + '\n')


# Rejected:  5893
# Overall CVEs:  109719
# vendorNull And Nullv2:  1254
# Null v2:  1293
# non-null V2:  108503
# Both v2 and v3 non-Null:  34948
# Both v2 and v3 Null:  1293