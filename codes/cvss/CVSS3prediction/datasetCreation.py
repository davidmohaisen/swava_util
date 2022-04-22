import os, re
import json

direct = '../../json_and_csv/nvd_json/'
c,d, x =0,0, 0
x1, x2 =  0, 0
v2_cve, v3_cve = {}, {}
rejectedVulns = set()
v2Nulls = set()
cwe_idCVEs = set()
OverallCves = set()
distinctCWEs = set()
for file in os.listdir(direct):
    f = open(direct+file)
    data = json.load(f)

    cve_items = data['CVE_Items']
    for i in range(len(cve_items)):
        publishedDate = cve_items[i]['publishedDate'].rsplit("T")[0]
        x+=1
        if (publishedDate > "2018-05-17" and "recent" in file) or (publishedDate <= "2018-05-17" and "nvdcve-1.1-2018" in file):
            # print(cve_items[i]['publishedDate'].rsplit("T")[0])
            continue
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']
        description_data = cve_items[i]['cve']['description']['description_data']

        desc = ''

        for k1 in range(len(description_data)):
            cve_desc = description_data[k1]['value']
            desc = desc + ' ' + cve_desc

        if '** REJECT **' in desc:
            rejectedVulns.add(cve_id)
            continue

        x1+=1

        impact = cve_items[i]['impact']
        desc = ''
        severity_v2 = ""
        exploit_v2 = ""
        impact_v2 = ""
        baseScore_v2 = ""
        severity_v3 = ""
        exploit_v3 = ""
        impact_v3 = ""
        baseScore_v3 = ""
        vectorString = ""
        accessVector = ""
        accessComplexity = ""
        authentication = ""
        confidentialityImpact = ""
        integrityImpact = ""
        availabilityImpact = ""
        obtainAllPrivilege = ""
        obtainUserPrivilege = ""
        obtainOtherPrivilege = ""
        userInteractionRequired = ""
        cwe_id = ""
        sv2 = ""
        sv3 = ""
        vectorStringTokenized = ""


        if len(impact) != 0:
            severity_v2 = cve_items[i]['impact']['baseMetricV2']['severity']
            baseScore_v2 = cve_items[i]['impact']['baseMetricV2']['cvssV2']['baseScore']
            exploit_v2 = cve_items[i]['impact']['baseMetricV2']['exploitabilityScore']
            impact_v2 = cve_items[i]['impact']['baseMetricV2']['impactScore']
            vectorString = cve_items[i]['impact']['baseMetricV2']['cvssV2']['vectorString']
            accessVector = cve_items[i]['impact']['baseMetricV2']['cvssV2']['accessVector']
            accessComplexity = cve_items[i]['impact']['baseMetricV2']['cvssV2']['accessComplexity']
            authentication = cve_items[i]['impact']['baseMetricV2']['cvssV2']['authentication']
            confidentialityImpact = cve_items[i]['impact']['baseMetricV2']['cvssV2']['confidentialityImpact']
            integrityImpact = cve_items[i]['impact']['baseMetricV2']['cvssV2']['integrityImpact']
            availabilityImpact = cve_items[i]['impact']['baseMetricV2']['cvssV2']['availabilityImpact']
            obtainAllPrivilege = cve_items[i]['impact']['baseMetricV2']['obtainAllPrivilege']
            obtainUserPrivilege = cve_items[i]['impact']['baseMetricV2']['obtainUserPrivilege']
            obtainOtherPrivilege = cve_items[i]['impact']['baseMetricV2']['obtainOtherPrivilege']
            try:
                userInteractionRequired = cve_items[i]['impact']['baseMetricV2']['userInteractionRequired']
            except:
                pass
            if severity_v2 not in v2_cve:
                v2_cve[severity_v2] = set()
                v2_cve[severity_v2].add(cve_id)
            else:
                v2_cve[severity_v2].add(cve_id)
            # except:
                # pass
            # print(vectorString)
            #     for keys in impact['baseMetricV2']:
            #         print(keys, impact['baseMetricV2'][keys])
            # exit()
        #
        # print("******************")

        if 'baseMetricV3' in impact:
            severity_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseSeverity']
            baseScore_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseScore']
            exploit_v3 = cve_items[i]['impact']['baseMetricV3']['exploitabilityScore']
            impact_v3 = cve_items[i]['impact']['baseMetricV3']['impactScore']
            x2 += 1

            if severity_v3 not in v3_cve:
                v3_cve[severity_v3] = set()
                v3_cve[severity_v3].add(cve_id)
            else:
                v3_cve[severity_v3].add(cve_id)
            # for keys in impact['baseMetricV3']:
            #     print(keys, impact['baseMetricV3'][keys])#, impact['baseMetricV2'][keys])
            # exit()


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
        # print(cwe_id)
        # print(cve_id, cwe_id)
        vects = re.sub(r'\(|\)', '', vectorString).rsplit("/")
        # if len(vects) > 6:
        #     print(vects)
        #     exit()
        try:
            av = vects[0].rsplit(':')[-1]
            ac = vects[1].rsplit(':')[-1]
            au = vects[2].rsplit(':')[-1]
            confid = vects[3].rsplit(':')[-1]
            integ = vects[4].rsplit(':')[-1]
            avail = vects[5].rsplit(':')[-1]
        except:
            av = ""
            ac = ""
            au = ""
            confid = ""
            integ = ""
            avail = ""

        OverallCves.add(cve_id)
        if cwe_id != "":
            cwe_idCVEs.add(cve_id)
            distinctCWEs.add(cwe_id)
        # else:
        #     print(cve_items[i])
        #     exit()
        if severity_v2 == "":
            # x2+=1
            v2Nulls.add(cve_id)
            continue
        if baseScore_v3 != "":
            c+=1
        d+=1
        # print(cve_id, severity_v2, baseScore_v2, exploit_v2, impact_v2, vectorString, exploit_v3, impact_v3, baseScore_v3, cwe_id)
        out = str(cve_id) + ";" + str(severity_v2) + ";" + str(baseScore_v2) + ";" + str(exploit_v2) + ";" + str(impact_v2) + ";" + str(av) +";"+ str(ac) +";"+ str(au) +";"+ str(confid) +";"+ str(integ) +";"+ str(avail) + ";" + vectorString + ";" + str(accessVector) + ";" + str(accessComplexity) + ";" + str(authentication) + ";" + str(confidentialityImpact) + ";" + str(integrityImpact) + ";" + str(availabilityImpact) + ";" + str(obtainAllPrivilege) + ";" + str(obtainUserPrivilege) + ";" + str(obtainOtherPrivilege) + ";" + str(cwe_id) + ";" + str(baseScore_v3) + ";" + str(severity_v3)
        # with open('./cvss2-3-cwe-withNullV3-R2.csv', "a") as of:
        #     of.write(out + '\n')

    # else:
    #     f = open(direct + file)
    #     data = json.load(f)
    #     cve_items = data['CVE_Items']
    #
    #     for i in range(len(cve_items)):
    #         print(cve_items[i]['impact'].keys())
    #
    #         cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']
    #         publishedDate = cve_items[i]['publishedDate']
    #         problemtype_desc = cve_items[i]['cve']['problemtype']['problemtype_data'][0]['description']
    #         exit()

print(c,d)
print(len(rejectedVulns), len(v2Nulls), x)
print(x1,x2)
print("Non Null CWEs: ", len(distinctCWEs), "and corresponding CVEs: ", len(cwe_idCVEs))
print("Total CVEs: ", len(OverallCves))
# for itm in v2_cve:
#     print(itm, len(v2_cve[itm]))
# for itm in v3_cve:
#     print(itm, len(v3_cve[itm]))