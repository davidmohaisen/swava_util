import datetime

f = open('./cve2018s_v2_pdd_date_diff_v3_predV3.csv', 'rb')

for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    # print(line)
    cve = line[0]
    v2 = line[1]
    pdd = line[2]
    date = line[3]
    diff = line[4]
    v3 = line[5]
    pv3 = line[6]
    if pdd > date:
        print(line)
    discYear, discMon, discDay = pdd.rsplit('-')[0], pdd.rsplit('-')[1], pdd.rsplit('-')[2]
    discDay = datetime.date(int(discYear), int(discMon), int(discDay)).strftime("%A")
    NvdYear, NvdMon, NvdDay = date.rsplit('-')[0], date.rsplit('-')[1], date.rsplit('-')[2]
    NvdDay = datetime.date(int(NvdYear), int(NvdMon), int(NvdDay)).strftime("%A")

    out = cve+";"+discDay+";"+NvdDay+";"+pdd+";"+date
    with open('./cve2018_discDay_NvdDay_pdd_date.csv', 'a') as foo:
        foo.write(out+'\n')
    # print(out)