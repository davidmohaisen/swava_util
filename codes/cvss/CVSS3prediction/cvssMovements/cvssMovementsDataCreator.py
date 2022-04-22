import os, re
import json

direct = '/media/seal06/HDD/Projects/Vulnerabilities/SWAVA/json_and_csv/NVD_JSON/'

header = "cve_id;severity_v2;baseScore_v2;exploit_v2;impact_v2;av;ac;au;confid;integ;avail;obtainAllPrivilege;obtainUserPrivilege;obtainOtherPrivilege;cwe_id;severity_v3;baseScore_v3;exploit_v3;impact_v3;av3;ac3;pr3;ui3;scope3;confid3;integ3;avail3"
with open('./cvssV2_V3_ForMovementsAnalysis-R2.csv', "a") as of:
    of.write(header + '\n')

c = 0
for file in os.listdir(direct):
    if 'recent' in file:
        continue
    f = open(direct+file)
    data = json.load(f)

    cve_items = data['CVE_Items']
    for i in range(len(cve_items)):
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']
        description_data = cve_items[i]['cve']['description']['description_data']
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
        vectorString3 = ""
        vectorStringTokenized = ""
        for k1 in range(len(description_data)):
            cve_desc = description_data[k1]['value']
            if not cve_desc.lstrip().rstrip().startswith('** REJECT **'):
                desc = desc + ' ' + cve_desc

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
            # print(cve_items[i]['impact']['baseMetricV2'].keys())
            try:
                userInteractionRequired = cve_items[i]['impact']['baseMetricV2']['userInteractionRequired']
            except:
                pass
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
            vectorString3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['vectorString']
            # print(cve_items[i]['impact']['baseMetricV3'])#.keys())
            # # print(cve_items[i]['impact']['baseMetricV3']['cvssV3'].keys())
            # print(cve_items[i]['impact']['baseMetricV2'])#.keys())
            # # print(cve_items[i]['impact']['baseMetricV2']['cvssV2'].keys())
            # # print(cve_items[i]['impact']['baseMetricV3']['cvssV3']['vectorString'])
            # # print(vectorString)
            # print("--------------------------")



            vects = re.sub(r'\(|\)', '', vectorString).rsplit("/")
            av = vects[0].rsplit(':')[-1]
            ac = vects[1].rsplit(':')[-1]
            au = vects[2].rsplit(':')[-1]
            confid = vects[3].rsplit(':')[-1]
            integ = vects[4].rsplit(':')[-1]
            avail = vects[5].rsplit(':')[-1]

            vect3tkn = re.sub(r'\(|\)', '', vectorString3).rsplit("/")
            av3 = vect3tkn[0].rsplit(':')[-1]
            ac3 = vect3tkn[1].rsplit(':')[-1]
            pr3 = vect3tkn[2].rsplit(':')[-1]
            ui3 = vect3tkn[3].rsplit(':')[-1]
            scope3 = vect3tkn[4].rsplit(':')[-1]
            confid3 = vect3tkn[5].rsplit(':')[-1]
            integ3 = vect3tkn[6].rsplit(':')[-1]
            avail3 = vect3tkn[7].rsplit(':')[-1]

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


            # print(cve_id, severity_v2, baseScore_v2, exploit_v2, impact_v2, vectorString, exploit_v3, impact_v3, baseScore_v3, cwe_id)

            out = str(cve_id) + ";" + str(severity_v2) + ";" + str(baseScore_v2) + ";" + str(exploit_v2) + ";" + str(impact_v2) + ";" + str(av) +";"+ str(ac) +";"+ str(au) +";"+ str(confid) +";"+ str(integ) +";"+ str(avail) + ";" + str(obtainAllPrivilege) + ";" + str(obtainUserPrivilege) + ";" + str(obtainOtherPrivilege) + ";" + str(cwe_id) + ";" + str(severity_v3) + ";" + str(baseScore_v3) + ";" + str(exploit_v3) + ";" + str(impact_v3) + ";" + str(av3) +";"+ str(ac3) +";"+ str(pr3) +";"+ str(ui3) +";"+ str(scope3) +";"+ str(confid3) + ";" + str(integ3) + ";" + str(avail3)
            print(out)
            c+=1
            with open('./cvssV2_V3_ForMovementsAnalysis-R2.csv', "a") as of:
                of.write(out + '\n')



print(c)