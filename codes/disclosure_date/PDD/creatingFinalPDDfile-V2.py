from datetime import datetime
import numpy as np

f1 = open('./part1/public_distribution_date_overall-V2.csv', 'rb')
f2 = open('./part2/public_distribution_date_overall-V2.csv', 'rb')
f3 = open('./part3/public_distribution_date_overall-V2.csv', 'rb')
f4 = open('./part4/public_distribution_date_overall-V2.csv', 'rb')
f5 = open('./part5/public_distribution_date_overall-V2.csv', 'rb')

cve_pdd = {}
cve_dt = {}
for line in f1:
    line = line.decode().replace('\n', '').rsplit(',')
    cve = line[0]
    pdd = line[1]
    dt = line[-1]
    if cve not in cve_pdd:
        cve_pdd[cve] = []
        if pdd != "":
            cve_pdd[cve].append(pdd)
    else:
        if pdd not in cve_pdd[cve] and pdd != "":
            cve_pdd[cve].append(pdd)

    if cve not in cve_dt:
        cve_dt[cve] = []
        if dt != "":
            cve_dt[cve].append(dt)
    else:
        if dt not in cve_dt[cve] and dt != "":
            cve_dt[cve].append(dt)
    # print(line)
    # exit()

for line in f2:
    line = line.decode().replace('\n', '').rsplit(',')
    cve = line[0]
    pdd = line[1]
    dt = line[-1]
    if cve not in cve_pdd:
        cve_pdd[cve] = []
        if pdd != "":
            cve_pdd[cve].append(pdd)
    else:
        if pdd not in cve_pdd[cve] and pdd != "":
            cve_pdd[cve].append(pdd)

    if cve not in cve_dt:
        cve_dt[cve] = []
        if dt != "":
            cve_dt[cve].append(dt)
    else:
        if dt not in cve_dt[cve] and dt != "":
            cve_dt[cve].append(dt)

for line in f3:
    line = line.decode().replace('\n', '').rsplit(',')
    cve = line[0]
    pdd = line[1]
    dt = line[-1]
    if cve not in cve_pdd:
        cve_pdd[cve] = []
        if pdd != "":
            cve_pdd[cve].append(pdd)
    else:
        if pdd not in cve_pdd[cve] and pdd != "":
            cve_pdd[cve].append(pdd)

    if cve not in cve_dt:
        cve_dt[cve] = []
        if dt != "":
            cve_dt[cve].append(dt)
    else:
        if dt not in cve_dt[cve] and dt != "":
            cve_dt[cve].append(dt)


for line in f4:
    line = line.decode().replace('\n', '').rsplit(',')
    cve = line[0]
    pdd = line[1]
    dt = line[-1]
    if cve not in cve_pdd:
        cve_pdd[cve] = []
        if pdd != "":
            cve_pdd[cve].append(pdd)
    else:
        if pdd not in cve_pdd[cve] and pdd != "":
            cve_pdd[cve].append(pdd)

    if cve not in cve_dt:
        cve_dt[cve] = []
        if dt != "":
            cve_dt[cve].append(dt)
    else:
        if dt not in cve_dt[cve] and dt != "":
            cve_dt[cve].append(dt)

for line in f5:
    line = line.decode().replace('\n', '').rsplit(',')
    cve = line[0]
    pdd = line[1]
    dt = line[-1]
    if cve not in cve_pdd:
        cve_pdd[cve] = []
        if pdd != "":
            cve_pdd[cve].append(pdd)
    else:
        if pdd not in cve_pdd[cve] and pdd != "":
            cve_pdd[cve].append(pdd)

    if cve not in cve_dt:
        cve_dt[cve] = []
        if dt != "":
            cve_dt[cve].append(dt)
    else:
        if dt not in cve_dt[cve] and dt != "":
            cve_dt[cve].append(dt)

f_1 = open('../../Re-cvss_analysis/CVSS3prediction/cvss2-3-cwe-withNullV3.csv', 'rb')
cve_cvss = {}
x1, x2, x3 = 0, 0, 0
for line in f_1:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    v2v3 = line[1]+":"+line[-1]
    if v2v3 == ":":
        continue
    cve_cvss[cve] = v2v3
    x1+=1
    # print(cve, v2v3)
# exit()
f0 = open('../../cve_publishedDate.csv', 'rb')
cve_publishedDate = {}
cve_diff = [[], [], []]
for line in f0:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    date = line[-1]
    if date > "2018-12-31":
        continue
    x2+=1
    if cve not in cve_publishedDate:
        cve_publishedDate[cve] = date

year_lag = {}
for cve in cve_publishedDate:
    date = cve_publishedDate[cve]
    year = date.rsplit("-")[0]
    date = datetime.strptime(date, "%Y-%m-%d")
    try:
        v2v3 = cve_cvss[cve].rsplit(":")
        v2, v3 = v2v3[0], v2v3[1]
    except:
        v2, v3 = "", ""

    try:
        pdd = cve_pdd[cve][0]
        if " " in pdd:
            pdd = pdd.rsplit(" ")[-2]
        pdd = datetime.strptime(pdd, "%Y-%m-%d")
    except KeyError:
        pdd = date
    except IndexError:
        pdd = date
    except:
        print("Exited ", cve_pdd[cve][0])
        exit()

    if date < pdd:
        pdd = date

    diff = (date - pdd).days
    pdd = str(pdd).rsplit(' ')[0]
    date = str(date).rsplit(' ')[0]


    out = str(cve) + ";" + str(pdd) + ";" + str(date) + ";" + str(diff)
    with open('./cve_pdd_diff-V2.csv', 'a') as foo:
        foo.write(out+'\n')
    cve_diff[0].append(cve)
    cve_diff[1].append(diff)
    cve_diff[2].append(v2)
    if year not in year_lag:
        year_lag[year] = []
        year_lag[year].append(abs(diff))
    else:
        year_lag[year].append(abs(diff))
    x3+=1


print(min(cve_diff[1]))
print(x1, x2, x3, len(cve_diff[0]))
print(len(cve_cvss), len(cve_publishedDate))
print(cve_cvss.keys() - cve_publishedDate.keys())
print(len(cve_cvss.keys() - cve_publishedDate.keys()))

lagTable = np.zeros((11, 4), dtype=np.int32)
print(lagTable)
print(lagTable.shape)
print(lagTable[0,2])
tkl=0
for i in range(len(cve_diff[1])):
    if cve_diff[1][i] < 0:
        tkl+=1
print("No. of CVEs with negative lag: ", tkl)
# exit()
diffs = cve_diff[1]
cve = cve_diff[0]
v2 = cve_diff[2]
for i in range(len(cve)):
    if diffs[i] <= 0:
        lagTable[0, 3] += 1
        if v2[i].lower() == "low":
            lagTable[0,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[0,1] += 1
        elif v2[i].lower() == "high":
            lagTable[0,2] += 1

    elif diffs[i] > 0 and diffs[i] <= 5:
        lagTable[1, 3] += 1
        if v2[i].lower() == "low":
            lagTable[1,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[1,1] += 1
        elif v2[i].lower() == "high":
            lagTable[1,2] += 1

    elif diffs[i] > 5 and diffs[i] <= 10:
        lagTable[2, 3] += 1
        if v2[i].lower() == "low":
            lagTable[2,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[2,1] += 1
        elif v2[i].lower() == "high":
            lagTable[2,2] += 1

    elif diffs[i] > 10 and diffs[i] <= 20:
        lagTable[3, 3] += 1
        if v2[i].lower() == "low":
            lagTable[3,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[3,1] += 1
        elif v2[i].lower() == "high":
            lagTable[3,2] += 1

    elif diffs[i] > 20 and diffs[i] <= 40:
        lagTable[4, 3] += 1
        if v2[i].lower() == "low":
            lagTable[4,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[4,1] += 1
        elif v2[i].lower() == "high":
            lagTable[4,2] += 1

    elif diffs[i] > 40 and diffs[i] <= 80:
        lagTable[5, 3] += 1
        if v2[i].lower() == "low":
            lagTable[5,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[5,1] += 1
        elif v2[i].lower() == "high":
            lagTable[5,2] += 1

    elif diffs[i] > 80 and diffs[i] <= 160:
        lagTable[6, 3] += 1
        if v2[i].lower() == "low":
            lagTable[6,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[6,1] += 1
        elif v2[i].lower() == "high":
            lagTable[6,2] += 1

    elif diffs[i] > 160 and diffs[i] <= 320:
        lagTable[7, 3] += 1
        if v2[i].lower() == "low":
            lagTable[7,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[7,1] += 1
        elif v2[i].lower() == "high":
            lagTable[7,2] += 1


    elif diffs[i] > 320 and diffs[i] <= 640:
        lagTable[8, 3] += 1
        if v2[i].lower() == "low":
            lagTable[8,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[8,1] += 1
        elif v2[i].lower() == "high":
            lagTable[8,2] += 1

    elif diffs[i] > 640 and diffs[i] <= 1280:
        lagTable[9, 3] += 1
        if v2[i].lower() == "low":
            lagTable[9,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[9,1] += 1
        elif v2[i].lower() == "high":
            lagTable[9,2] += 1


    elif diffs[i] > 1280:
        lagTable[10, 3] += 1
        if v2[i].lower() == "low":
            lagTable[10,0] += 1
        elif v2[i].lower() == "medium":
            lagTable[10,1] += 1
        elif v2[i].lower() == "high":
            lagTable[10,2] += 1
print(lagTable)

for itm in year_lag:
    print(itm, sum(year_lag[itm]), len(year_lag[itm]), np.median(np.array(year_lag[itm])), round(np.mean(np.array(year_lag[itm])), 2))
# for i in range(len(cve_diff[0])):