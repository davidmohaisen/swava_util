f = open('../../../ConsistentVendor_prod_info.csv', 'rb')

yearIncons = {}
yearInconsOverall = {}
dateS = set()
for line in f:
    line = line.decode().replace("\n", '').rsplit(";")
    cve = line[0]
    vendor = line[1]
    consisVend = line[2]
    product = line[3]
    date = line[4]
    # year = cve.rsplit("-")[1]
    year = date.rsplit("-")[0]
    # print(year, type(year))
    # exit()
    if year == "2019":
        continue
    if consisVend != "":
        if year not in yearInconsOverall:
            yearInconsOverall[year] = set()
            yearInconsOverall[year].add(cve)
        else:
            yearInconsOverall[year].add(cve)

    if consisVend != vendor and consisVend != "":
        if year not in yearIncons:
            yearIncons[year] = set()
            yearIncons[year].add(cve)
        else:
            yearIncons[year].add(cve)
    if "2019" in date:
        dateS.add(date)
    # print(year)
print(dateS)
print(len(dateS))
# exit()
for itm in yearIncons:
    print(itm, len(yearIncons[itm]), len(yearInconsOverall[itm]))