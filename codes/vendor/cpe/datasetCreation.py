import os, re
import json

direct = '/media/seal06/HDD/Projects/Vulnerabilities/SWAVA/json_and_csv/NVD_JSON/'
cpe22Set, cpe23Set = set(), set()
for file in os.listdir(direct):
    if 'recent' in file:
        continue
    f = open(direct+file)
    data = json.load(f)

    cve_items = data['CVE_Items']
    for i in range(len(cve_items)):
        # cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']
        cpeNodes = cve_items[i]['configurations']['nodes']

        for cpeDet in cpeNodes:
            try:
                cpe = cpeDet['cpe']
                # print(cpe)
                for j in range(len(cpe)):
                    cpe22 = cpe[j]['cpeMatchString']
                    cpe23 = cpe[j]['cpe23Uri']
                    cpe22Set.add(cpe22)
                    cpe23Set.add(cpe23)
                    # print(cpe22, cpe23)
            except:
                try:
                    cpeChildren = cpeDet['children']
                    for j in range(len(cpeChildren)):
                        try:
                            cpe = cpeChildren[j]['cpe']
                            for k in range(len(cpe)):
                                cpe22 = cpe[k]['cpeMatchString']
                                cpe23 = cpe[k]['cpe23Uri']
                                cpe22Set.add(cpe22)
                                cpe23Set.add(cpe23)
                                # print(cpe22, cpe23)
                        except:
                            if 'cpe' not in cpeChildren[j]:
                                # print("no cpe in children", cpeChildren[j])
                                continue
                except:
                    if 'cpe' not in cpeDet:
                        continue
                        # print(cpeDet)
                    # exit()

for cpe23 in cpe23Set:
    vendor = cpe23.rsplit(':')[2]
    product = cpe23.rsplit(':')[3]

print(cpe23Set)


        # print(cve_id, desc, severity_v3, exploit_v3, impact_v3, baseScore_v3)
        # out1 = str(cve_id) + ";" + str(desc).replace(';', '') + ";" + str(severity_v3) + ";" + str(baseScore_v3)
        # with open('./desc-cvss3-R2.csv', "a") as of:
        #     of.write(out1 + '\n')