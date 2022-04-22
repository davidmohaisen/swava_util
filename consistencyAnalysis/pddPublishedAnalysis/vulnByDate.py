f = open('../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

cve_PDD = {}
cve_date = {}
yearPDD_cnt = {}
yearPublished_cnt = {}
pddYear_cve, dateYear_cve = {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]

    pdd = line[1].rsplit(" ")[0]
    yearPDD = pdd.rsplit("-")[0]
    publishedDate = line[2].rsplit(" ")[0]
    yearPublished = publishedDate.rsplit("-")[0]
    if yearPDD not in pddYear_cve:
        pddYear_cve[yearPDD] = set()
        pddYear_cve[yearPDD].add(cve)
    else:
        pddYear_cve[yearPDD].add(cve)

    if yearPublished not in dateYear_cve:
        dateYear_cve[yearPublished] = set()
        dateYear_cve[yearPublished].add(cve)
    else:
        dateYear_cve[yearPublished].add(cve)

    if yearPDD not in yearPDD_cnt:
        yearPDD_cnt[yearPDD] = set()
        yearPDD_cnt[yearPDD].add(pdd)
    else:
        yearPDD_cnt[yearPDD].add(pdd)

    if yearPublished not in yearPublished_cnt:
        yearPublished_cnt[yearPublished] = set()
        yearPublished_cnt[yearPublished].add(publishedDate)
    else:
        yearPublished_cnt[yearPublished].add(publishedDate)

    if pdd not in cve_PDD:
        cve_PDD[pdd] = set()
        cve_PDD[pdd].add(cve)
    else:
        cve_PDD[pdd].add(cve)

    if publishedDate not in cve_date:
        cve_date[publishedDate] = set()
        cve_date[publishedDate].add(cve)
    else:
        cve_date[publishedDate].add(cve)

# for itm in cve_date:
#     with open('./cvePerPublishedDate-V2.csv', 'a') as foo:
#         foo.write(str(itm)+";"+str(len(cve_date[itm]))+"\n")
# #
# for itm in cve_PDD:
#     with open('./cvePerPDD-V2.csv', 'a') as foo:
#         foo.write(str(itm)+";"+str(len(cve_PDD[itm]))+"\n")

# for itm in yearPublished_cnt:
#     with open('./year_pddCount_dateCount-V2.csv', 'a') as foo:
#         foo.write(str(itm)+";"+str(len(yearPDD_cnt[itm]))+";"+str(len(yearPublished_cnt[itm]))+"\n")
#     print(itm, len(yearPDD_cnt[itm]), len(yearPublished_cnt[itm]))

# pddYear_cve, dateYear_cve
for itm in pddYear_cve:
    with open('./year_pddCveCount_dateCveCount-V2.csv', 'a') as foo:
        foo.write(str(itm)+";"+str(len(pddYear_cve[itm]))+";"+str(len(dateYear_cve[itm]))+"\n")
    print(itm, len(pddYear_cve[itm]), len(dateYear_cve[itm]))