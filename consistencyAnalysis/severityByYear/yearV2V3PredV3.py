import pandas as pd

f = open('./cve2018s_v2_pdd_date_diff_v3_predV3-V2.csv', 'rb')

year_cve = {}
cve_v2, cve_v3, cve_predV3 = {}, {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    print(line)
    cve = line[0]
    v2 = line[1]
    discYear = line[2].rsplit('-')[0]
    v3 = line[-2]
    predV3 = line[-1]

    if discYear not in year_cve:
        year_cve[discYear] = set()
        year_cve[discYear].add(cve)
    else:
        year_cve[discYear].add(cve)

    if cve not in cve_v2:
        cve_v2[cve] = v2
    if cve not in cve_v3:
        cve_v3[cve] = v3
    if cve not in cve_predV3:
        cve_predV3[cve] = predV3

data = [[], [], [], [], [], [], [], [], [], [], [], []]

for year in year_cve:
    v2l, v2m, v2h, v3l, v3m, v3h, v3c, pv3l, pv3m, pv3h, pv3c = 0,0,0,0,0,0,0,0,0,0,0
    for cve in year_cve[year]:
        v2 = cve_v2[cve]
        if v2 == "LOW":
            v2l+=1
        elif v2 == "MEDIUM":
            v2m+=1
        elif v2 == "HIGH":
            v2h+=1

        v3 = cve_v3[cve]
        if v3 == "LOW":
            v3l+=1
        elif v3 == "MEDIUM":
            v3m+=1
        elif v3 == "HIGH":
            v3h+=1
        elif v3 == "CRITICAL":
            v3c+=1


        predV3 = cve_predV3[cve]
        if predV3 == "LOW":
            pv3l+=1
        elif predV3 == "MEDIUM":
            pv3m+=1
        elif predV3 == "HIGH":
            pv3h+=1
        elif predV3 == "CRITICAL":
            pv3c+=1
    data[0].append(year)
    data[1].append(v2l)
    data[2].append(v2m)
    data[3].append(v2h)
    data[4].append(v3l)
    data[5].append(v3m)
    data[6].append(v3h)
    data[7].append(v3c)
    data[8].append(pv3l)
    data[9].append(pv3m)
    data[10].append(pv3h)
    data[11].append(pv3c)

    # print(line)
# headers = ['year', 'v2l', 'v2m', 'v2h', 'v3l', 'v3m', 'v3h', 'v3c', 'pv3l', 'pv3m', 'pv3h', 'pv3c']
df = pd.DataFrame(data)#, columns=headers)
# print(df)
# df.to_csv('./v2v3predv3ByYear.csv', index=False)
# for i in range(len(data)):
#     print((data[i]))
