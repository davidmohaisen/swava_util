import os, re, json

dir = './newSnapshot/'

cweNulls_date = {}
for line in open('./CweIdNull.csv', 'rb'):
    line = line.decode().replace('\n', '').rsplit(';')
    cweNulls_date[line[0]] = line[1]

linksNulls_date = {}
for line in open('./linksNull.csv', 'rb'):
    line = line.decode().replace('\n', '').rsplit(';')
    linksNulls_date[line[0]] = line[1]

v2Nulls_date = {}
for line in open('./v2Null.csv', 'rb'):
    line = line.decode().replace('\n', '').rsplit(';')
    v2Nulls_date[line[0]] = line[1]

vendorNulls_date = {}
for line in open('./vendorNull.csv', 'rb'):
    line = line.decode().replace('\n', '').rsplit(';')
    vendorNulls_date[line[0]] = line[1]

# exit()
# vendorNulls_date, v2Nulls_date, linksNulls_date, cweNulls_date
x=0
for file in os.listdir(dir):
    file = open(dir+file)
    data = json.load(file)

    cve_items = data['CVE_Items']
    for i in range(len(cve_items)):
        publishedDate = cve_items[i]['publishedDate'].rsplit("T")[0]
        lastModifiedDate = cve_items[i]['lastModifiedDate'].rsplit("T")[0]
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
            continue

        # if "CWE-" in desc:
        #     print(cve_id, desc)

        # with open('./cve_publishedDate.csv', 'a') as foo:
        #     foo.write(str(cve_id)+";"+str(publishedDate)+"\n")

        vendor, product = "", ""
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
                    # print(cve_id, vendor, product)
                    out = cve_id + ';' + str(vendor) + ";" + str(product) + ";" + publishedDate
            except:
                children = nodes[ij]['children']
                for ijk in range(len(children)):
                    try:
                        cpe_match = children[ijk]['cpe_match']
                        for ijkl in range(len(cpe_match)):
                            uri = cpe_match[ijkl]['cpe23Uri']
                            vendor = uri.rsplit(":")[3]
                            product = uri.rsplit(":")[4]
                            # print(cve_id, vendor, product)
                            out = cve_id+';'+str(vendor)+";"+str(product) + ";" + publishedDate
                    except:
                        continue


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

        if cve_id in vendorNulls_date:
            changed = ""
            if vendor != "":
                changed = lastModifiedDate
            with open('./vendorNullsCurrentStatus.csv', 'a') as foo:
                foo.write(str(cve_id)+";"+str(vendorNulls_date[cve_id])+";"+str(changed)+'\n')

        if cve_id in v2Nulls_date:
            changed = ""
            if severity_v2 != "":
                changed = lastModifiedDate
            with open('./v2NullsCurrentStatus.csv', 'a') as foo:
                foo.write(str(cve_id)+";"+str(v2Nulls_date[cve_id])+";"+str(changed)+'\n')

        if cve_id in linksNulls_date:
            changed = ""
            if referenceLink != "":
                changed = lastModifiedDate
            with open('./linksNullsCurrentStatus.csv', 'a') as foo:
                foo.write(str(cve_id)+";"+str(linksNulls_date[cve_id])+";"+str(changed)+'\n')

        if cve_id in cweNulls_date:
            changed = ""
            if cwe_id != "":
                changed = lastModifiedDate
            with open('./cweIdNullsCurrentStatus.csv', 'a') as foo:
                foo.write(str(cve_id)+";"+str(cweNulls_date[cve_id])+";"+str(changed)+'\n')

# vendorNulls_date, v2Nulls_date, linksNulls_date, cweNulls_date
