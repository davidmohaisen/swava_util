import re
from datetime import datetime

f = open('./cve_pdd_date_pddYear_nvdYear_cweId_cweDb_cweDesc-V2.csv', 'rb')
cwe_year = {}
cweBefore_Year = {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[1]
    date = line[2]
    pddYear = int(line[3])
    dateYear = int(line[4])
    cwe_id = line[5]
    cweDb = line[6]
    cweDesc = line[7]
    cweList = set()
    if pddYear == "":
        print(line)
        # pddYear = dateYear

    beforeCwes = cwe_id.rsplit(",")
    for j2 in range(len(beforeCwes)):
        befcwe = beforeCwes[j2]
        if befcwe not in cweBefore_Year:
            cweBefore_Year[befcwe] = set()
            cweBefore_Year[befcwe].add(dateYear)
        else:
            cweBefore_Year[befcwe].add(dateYear)

    cweids = cwe_id.replace(', ', ',').rsplit(',')
    for i in range(len(cweids)):
        found = 0
        if cweids[i] == "NVD-CWE-Other" or cwe_id == "NVD-CWE-noinfo":
            if cweDb != "":
                found = 1
                cweList.add(cweDb)
                if cweDb not in cwe_year:
                    cwe_year[cweDb] = set()
                    cwe_year[cweDb].add(pddYear)
                else:
                    cwe_year[cweDb].add(pddYear)
            if cweDesc != "":
                found = 1
                cweList.add(cweDesc)
                if cweDesc not in cwe_year:
                    cwe_year[cweDesc] = set()
                    cwe_year[cweDesc].add(pddYear)
                else:
                    cwe_year[cweDesc].add(pddYear)
            if found == 0:
                cweList.add(cweids[i])
                if cweids[i] not in cwe_year:
                    cwe_year[cweids[i]] = set()
                    cwe_year[cweids[i]].add(pddYear)
                else:
                    cwe_year[cweids[i]].add(pddYear)
        else:
            if cweDb != "":
                cweList.add(cweDb)
                if cweDb not in cwe_year:
                    cwe_year[cweDb] = set()
                    cwe_year[cweDb].add(pddYear)
                else:
                    cwe_year[cweDb].add(pddYear)
            if cweDesc != "":
                cweList.add(cweDesc)
                if cweDesc not in cwe_year:
                    cwe_year[cweDesc] = set()
                    cwe_year[cweDesc].add(pddYear)
                else:
                    cwe_year[cweDesc].add(pddYear)
            if cweids[i] != "":
                cw = ""
                if cweids[i] == "CWE-769":
                    cw = "CWE-774"
                    cweList.add(cw)
                elif cweids[i] == "CWE-534":
                    cw = "CWE-532"
                    cweList.add(cw)
                elif cweids[i] == "CWE-18":
                    cw = "CWE-699"
                    cweList.add(cw)
                elif cweids[i] == "CWE-17":
                    cw = "CWE-699"
                    cweList.add(cw)
                elif cweids[i] == "CWE-1":
                    cw = "CWE-699"
                    cweList.add(cw)
                cweList.add(cweids[i])

                if cw not in cwe_year:
                    cwe_year[cw] = set()
                    cwe_year[cw].add(pddYear)
                else:
                    cwe_year[cw].add(pddYear)

                if cweids[i] not in cwe_year:
                    cwe_year[cweids[i]] = set()
                    cwe_year[cweids[i]].add(pddYear)
                else:
                    cwe_year[cweids[i]].add(pddYear)

    # if cweDb != "" or cweDesc != "":
    cwes = re.sub(r'\{|\}|\'|\"', '', str(cweList)).replace(', ', ',')
    out = cve+";"+cwe_id+";"+cweDb+";"+cweDesc+";"+cwes+";"+pdd+";"+date+";"+str(pddYear)+";"+str(dateYear)
    # with open('./cve_cwe_cwedb_cwedesc_ConsistentCwe.csv', 'a') as foo:
    #     foo.write(out+'\n')
    # print(cwe_id, cweDb, cweDesc, cweList)
# print(cwe_year["CWE-190"])
# exit()
cweafter_year = {}
for cwePre in cwe_year:
    yearSet = cwe_year[cwePre]
    cweTkn = cwePre.rsplit(',')
    for i in range(len(cweTkn)):
        if cweTkn[i] not in cweafter_year:
            cweafter_year[cweTkn[i]] = set()
            cweafter_year[cweTkn[i]] = yearSet
        else:
            cweafter_year[cweTkn[i]].union(yearSet)
for cwe in cweafter_year:
    yearList = list(cweafter_year[cwe])
    index1 = sorted(yearList, reverse=True)
    lastSeen = index1[0]
    firstSeen = index1[-1]
    # if lastSeen or firstSeen == "":
    #     continue
    out = str(cwe)+";"+str(firstSeen)+";"+str(lastSeen)
    # print(out)
    # with open('./cweFirstLastYear-After.csv', 'a') as foo:
    #     foo.write(out+'\n')

for cwe in cweBefore_Year:
    beforeYearList = list(cweBefore_Year[cwe])
    index1 = sorted(beforeYearList, reverse=True)
    lastSeen = index1[0]
    firstSeen = index1[-1]
    # if lastSeen or firstSeen == "":
    #     continue
    out = str(cwe) + ";" + str(firstSeen) + ";" + str(lastSeen)
    # with open('./cweFirstLastYear-before.csv', 'a') as foo:
    #     foo.write(out+'\n')
    print(out)