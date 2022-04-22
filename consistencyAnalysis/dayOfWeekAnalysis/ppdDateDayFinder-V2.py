import datetime

f = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    # print(line)
    # exit()
    cve = line[0]
    pdd = line[1]
    date = line[2]
    diff = line[3]
    if pdd > date:
        print(line)
    discYear, discMon, discDay = pdd.rsplit('-')[0], pdd.rsplit('-')[1], pdd.rsplit('-')[2]
    discDay = datetime.date(int(discYear), int(discMon), int(discDay)).strftime("%A")
    NvdYear, NvdMon, NvdDay = date.rsplit('-')[0], date.rsplit('-')[1], date.rsplit('-')[2]
    NvdDay = datetime.date(int(NvdYear), int(NvdMon), int(NvdDay)).strftime("%A")

    out = cve+";"+discDay+";"+NvdDay+";"+pdd+";"+date
    with open('./cve_discDay_NvdDay_pdd_date-V2.csv', 'a') as foo:
        foo.write(out+'\n')
    # print(out)