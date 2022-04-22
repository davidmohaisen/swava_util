import pandas as pd

f = open('../cweDb/cve_cwe_cwedb_cwedesc_ConsistentCwe.csv', 'rb')

year_cwe_VulnCount, inconYear_cwe_VulnCount = {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(";")
    # print(line)
    # exit()
    cve = line[0]
    consCwe = line[4]
    year = int(line[-2])

    inconCwe = line[1]
    inconYear = int(line[-1])
    # print(year)

    if inconYear not in inconYear_cwe_VulnCount:
        inconYear_cwe_VulnCount[inconYear] = {}
        if inconCwe not in inconYear_cwe_VulnCount[inconYear]:
            inconYear_cwe_VulnCount[inconYear][inconCwe] = set()
            inconYear_cwe_VulnCount[inconYear][inconCwe].add(cve)
        else:
            inconYear_cwe_VulnCount[inconYear][inconCwe].add(cve)
    else:
        if inconCwe not in inconYear_cwe_VulnCount[inconYear]:
            inconYear_cwe_VulnCount[inconYear][inconCwe] = set()
            inconYear_cwe_VulnCount[inconYear][inconCwe].add(cve)
        else:
            inconYear_cwe_VulnCount[inconYear][inconCwe].add(cve)

    if year not in year_cwe_VulnCount:
        year_cwe_VulnCount[year] = {}
        if consCwe not in year_cwe_VulnCount[year]:
            year_cwe_VulnCount[year][consCwe] = set()
            year_cwe_VulnCount[year][consCwe].add(cve)
        else:
            year_cwe_VulnCount[year][consCwe].add(cve)
    else:
        if consCwe not in year_cwe_VulnCount[year]:
            year_cwe_VulnCount[year][consCwe] = set()
            year_cwe_VulnCount[year][consCwe].add(cve)
        else:
            year_cwe_VulnCount[year][consCwe].add(cve)

cweset = set()
for year in year_cwe_VulnCount:
    cweset = cweset.union(set(year_cwe_VulnCount[year].keys()))
    # print(year, len(set(year_cwe_VulnCount[year].keys())))

inconcweset = set()
for year in inconYear_cwe_VulnCount:
    inconcweset = inconcweset.union(set(inconYear_cwe_VulnCount[year].keys()))

for itm in inconYear_cwe_VulnCount[2018]:
    print(itm, len(inconYear_cwe_VulnCount[2018][itm]))
# exit()
# inconYear_cwe_VulnCount
cweList = list(cweset)
cwes2018Top20 = ['CWE-79', 'CWE-119', 'CWE-20', 'CWE-200', 'NVD-CWE-noinfo', 'CWE-190', 'CWE-125', 'CWE-89', 'CWE-352', 'CWE-284', 'CWE-22', 'CWE-416', 'CWE-476', 'CWE-264', 'CWE-78', 'CWE-787', 'CWE-287', 'CWE-611', 'CWE-400', 'CWE-434']
years = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988]
cwesInconTop20 = ['CWE-79', 'CWE-119', 'CWE-20', 'CWE-200', 'NVD-CWE-noinfo', 'CWE-190', 'CWE-125', 'CWE-89', 'CWE-352', 'CWE-284', 'CWE-22', 'CWE-264', 'CWE-416', 'CWE-476', 'CWE-78', 'CWE-787', 'CWE-287', 'CWE-611', 'CWE-400', 'CWE-434']

year_cwe_Counts = []
cweForHeader = []
cweForHeader.append("CWE-ID")
for i in range(len(cwes2018Top20)):
    cweForHeader.append(cwes2018Top20[i])

# year_cwe_Counts.append(cweForHeader)

inconyear_cwe_Counts = []
inconcweForHeader = []
inconcweForHeader.append("CWE-ID")
for i in range(len(cwesInconTop20)):
    inconcweForHeader.append(cwesInconTop20[i])
inconyear_cwe_Counts.append(inconcweForHeader)

for j in range(len(years)):
    year = years[j]
    year_counts = []
    year_counts.append(year)
    for i in range(len(cwes2018Top20)):
        cwe = cwes2018Top20[i]
        try:
            count = len(year_cwe_VulnCount[year][cwe])
        except:
            count = 0
        year_counts.append(count)
    year_cwe_Counts.append(year_counts)
    # For inconsis >>

    inconyear = years[j]
    inconyear_counts = []
    inconyear_counts.append(inconyear)
    for i in range(len(cwesInconTop20)):
        inconcwe = cwesInconTop20[i]
        try:
            inconcount = len(inconYear_cwe_VulnCount[inconyear][inconcwe])
        except:
            inconcount = 0
        inconyear_counts.append(inconcount)

    year_cwe_Counts.append(year_counts)
    inconyear_cwe_Counts.append(inconyear_counts)

print(year_cwe_Counts)
print(inconyear_cwe_Counts)

df = pd.DataFrame(year_cwe_Counts)
# df.to_csv('./yearCweVulnCounts_ForTrendAnalysis.csv', index=False)
print(df)

dfIncon = pd.DataFrame(inconyear_cwe_Counts)
# dfIncon.to_csv('./yearCweVulnCounts_ForTrendAnalysis-Inconsis.csv', index=False)
print(dfIncon)
dfIncon = dfIncon.T
dfIncon.to_csv('./yearCweVulnCounts_ForTrendAnalysis-Inconsis.csv', index=False)
print(dfIncon)
# for i in range(len(year_cwe_Counts)):
#     print()
# print(dfIncon.subtract(df))