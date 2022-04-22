f0 = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv')
cve_pddYear, cve_pddInconYear = {}, {}
for line in f0:
    line = line.replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[1]
    date = line[2]

    if cve not in cve_pddYear:
        cve_pddYear[cve] = int(pdd.rsplit('-')[0])
    if cve not in cve_pddInconYear:
        cve_pddInconYear[cve] = int(date.rsplit('-')[0])
    # print(line)
    # exit()
# f = open('../../inconsistency/nvd/codes/ProdAnalysis/cve_vendProd_ConsIncons_pdd_date-V2.csv', 'rb')
f=open('../../ConsistentVendor_prod_info-V2.csv', 'rb')

outDir = './kPercUntilYear-Files/After/'
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
year_vend_CveCount = {}
vend_CveCount = {}
vendcount = set()

yearFile = 2010
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    vend = line[1]
    consisVend = line[2]
    if consisVend == "":
        consisVend = vend

    # consisVend = vend

    year = int(cve_pddYear[cve])
    # year = int(line[-1].rsplit('-')[0])
    if year <= yearFile:
        vendcount.add(consisVend)
        pddYear = yearFile
        if consisVend not in vend_CveCount:
            vend_CveCount[consisVend] = set()
            vend_CveCount[consisVend].add(cve)
        else:
            vend_CveCount[consisVend].add(cve)

        # if pddYear not in year_vend_CveCount:
        #     year_vend_CveCount[pddYear] = {}
        #     if vend not in year_vend_CveCount[pddYear]:
        #         year_vend_CveCount[pddYear][vend] = set()
        #         year_vend_CveCount[pddYear][vend].add(cve)
        #     else:
        #         year_vend_CveCount[pddYear][vend].add(cve)
        # else:
        #     if vend not in year_vend_CveCount[pddYear]:
        #         year_vend_CveCount[pddYear][vend] = set()
        #         year_vend_CveCount[pddYear][vend].add(cve)
        #     else:
        #         year_vend_CveCount[pddYear][vend].add(cve)

print(len(vend_CveCount))
print(len(vendcount))
for itm in vend_CveCount:
    out = str(itm)+";"+str(len(vend_CveCount[itm]))
    with open(outDir+str(yearFile)+".csv", 'a') as foo:
        foo.write(out+"\n")

# for year in year_vend_CveCount:
#     x, y = 0, 0
#     for vend in year_vend_CveCount[year]:
#         # print(vend, len(year_vend_CveCount[year][vend]))
#         out = str(vend)+";"+str(len(year_vend_CveCount[year][vend]))
#         x+=len(year_vend_CveCount[year][vend])
#         # with open(outDir+str(year)+".csv", 'a') as foo:
#         #     foo.write(out+'\n')
#     # exit()
#     y+=len(year_vend_CveCount[year])
#     print(year, y, x)
#
# print(len(year_vend_CveCount[2018]))
# print(len(vendcount))