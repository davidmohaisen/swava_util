import re
f = open('./Cons-cve_cweId_CweDb_PDD_Date-V3.xlsx', 'rb')
# next(f)

cwe_yearMin = {}
cwe_yearMax = {}
cwe_yearMinNvd, cwe_yearMaxNvd = {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    # print(line)

    cve = line[0]
    cweNVD = line[1]
    cweDesc = line[2]
    year = line[-1].rsplit('-')[0]
    # if year not in cwe_yearMin:
    #     cwe_yearMin[cweDesc] = set()
    #     cwe_yearMin[cweDesc] = int(year)
    # else:
    #     if cwe_yearMin[cweDesc] < int(year):
    #         cwe_yearMin[cweDesc] = int(year)

    if year not in cwe_yearMax:
        cwe_yearMax[year] = set()
        if cweDesc != "":
           cwe_yearMax[year].add(cweDesc)#int(year)
    else:
        if cweDesc != "":
            cwe_yearMax[year].add(cweDesc)

    if year not in cwe_yearMinNvd:
        cwe_yearMinNvd[year] = set()
        if cweDesc != "":
            cwe_yearMinNvd[year].add(cweNVD)
    else:
        if cweDesc != "":
            cwe_yearMinNvd[year].add(cweNVD)

    # if year not in cwe_yearMaxNvd:
    #     cwe_yearMaxNvd[year] = set()
    #     cwe_yearMaxNvd[year].add(cweNVD)
    # else:
    #     # if cwe_yearMaxNvd[year] > int(year):
    #     cwe_yearMaxNvd[year].add(cweNVD)


for itm in cwe_yearMax:
    # print(itm, re.sub(r'\{|\}|\'| ', '', str(cwe_yearMax[itm]-cwe_yearMinNvd[itm])))
    print(itm, len(cwe_yearMax[itm]-cwe_yearMinNvd[itm]))
    # try:
    #     out = (itm, cwe_yearMax[itm], cwe_yearMinNvd[itm])
    # except:
    #     print(itm)

# print("***********")
# for itm in cwe_yearMaxNvd:
#     print(itm, cwe_yearMaxNvd[itm], cwe_yearMinNvd[itm])

# 1999 {'NVD-CWE-Other'}
# 1998 {'NVD-CWE-Other'}
# 1997 {'NVD-CWE-Other'}
# 1996 set()
# 1995 set()
# 1988 set()
# 1990 set()
# 1994 set()
# 1992 set()
# 1993 set()
# 1991 set()
# 2000 {'NVD-CWE-Other'}
# 2001 {'NVD-CWE-Other'}
# 2002 {'NVD-CWE-Other'}
# 1989 set()
# 2003 {'NVD-CWE-Other'}
# 2005 {'NVD-CWE-Other'}
# 2009 {'NVD-CWE-Other'}
# 2010 {'NVD-CWE-Other'}
# 2011 {'NVD-CWE-Other'}
# 2016 {'NVD-CWE-Other,CWE-189', 'CWE-119,NVD-CWE-Other', 'NVD-CWE-Other,CWE-255', 'CWE-362,NVD-CWE-Other', 'NVD-CWE-Other,CWE-310', 'CWE-362,NVD-CWE-Other,CWE-200', 'NVD-CWE-Other', 'NVD-CWE-Other,CWE-200', 'NVD-CWE-Other,CWE-264'}
# 2004 {'NVD-CWE-Other'}
# 2014 {'NVD-CWE-Other'}
# 2015 {'CWE-362,NVD-CWE-Other', 'NVD-CWE-Other', 'NVD-CWE-Other,CWE-254'}
# 2013 {'NVD-CWE-Other'}
# 2017 {'CWE-665', 'NVD-CWE-Other', 'CWE-79,CWE-352', 'CWE-943'}
# 2018 {'', 'CWE-125,CWE-129'}
# 2012 {'NVD-CWE-Other'}
# 2006 {'NVD-CWE-Other'}
# 2007 {'NVD-CWE-Other'}
# 2008 {'CWE-89,CWE-352', 'NVD-CWE-Other'}
# 2019 {'CWE-943'}