from datetime import datetime

f = open('./pdd_by_link.csv', 'rb')

kernelOrgChangeCves = set()
cve_pdds = {}
v2cve_pdd = {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(',')
    cve = line[0]
    url = ",".join(line[1:-2])
    pdd = line[-2]

    if "kernel.org" in url and "changelog" in url.lower():
        kernelOrgChangeCves.add(cve)
        continue

    if cve not in cve_pdds:
        cve_pdds[cve] = []
        if pdd != "":
            cve_pdds[cve].append(pdd)
    elif pdd != "":
        cve_pdds[cve].append(pdd)

    # print(line)
    # cve = line[0]
for cve in kernelOrgChangeCves:
    pddList = cve_pdds[cve]
    index1 = sorted(pddList, key=lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%Y-%m-%d"))
    try:
        pdd = index1[0]
    except:
        print("Errored: ", cve)
        pdd = ""
    # print(cve, index1, pdd)
    if cve not in v2cve_pdd:
        v2cve_pdd[cve] = pdd

# out = cve_id + "," + public_date + "," + db_dt1 + "\n"
prePddFile = open('./public_distribution_date_overall.csv', 'rb')
for line in prePddFile:
    line = line.decode().replace('\n', '')
    tkn = line.rsplit(',')
    cve = tkn[0]
    pdd = tkn[1]
    date = tkn[2]
    if cve in v2cve_pdd:
        pdd = v2cve_pdd[cve]

    out = cve + "," + pdd + "," + date + "\n"
    with open('./public_distribution_date_overall-V2.csv', 'a') as foo:
        foo.write(out)