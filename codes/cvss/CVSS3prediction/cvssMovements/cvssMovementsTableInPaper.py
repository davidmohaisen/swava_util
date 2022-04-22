import numpy as np

f = open('../cvss2-3-cwe.csv', 'rb')

lh, lm, lc, ml, mh, mc, hl, hm, hc, ll, mm, hh = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

mat = [[ll, lm, lh, lc], [ml, mm, mh, mc], [hl, hm, hh, hc]]
print(mat)
cveSet = set()
for line in f:
    line = line.decode().replace('\n', '')
    # print(line)
    tkn = line.rsplit(';')
    # if len(tkn) != 24:
    #     print(line)
    # print(tkn[1])
    v3 = tkn[-1].rstrip().lstrip()
    v2 = tkn[1]
    cve = tkn[0]

    if v3 == "":
        continue
    if cve in cveSet:
        continue

    if v2 == "LOW" and v3 == "MEDIUM":
        lm += 1
    elif v2 == "LOW" and v3 == "LOW":
        ll += 1
    elif v2 == "LOW" and v3 == "HIGH":
        lh += 1
    elif v2 == "LOW" and v3 == "CRITICAL":
        lc += 1
    elif v2 == "MEDIUM" and v3 == "LOW":
        ml += 1
    elif v2 == "MEDIUM" and v3 == "MEDIUM":
        mm += 1
    elif v2 == "MEDIUM" and v3 == "HIGH":
        mh += 1
    elif v2 == "MEDIUM" and v3 == "CRITICAL":
        mc += 1
    elif v2 == "HIGH" and v3 == "LOW":
        hl += 1
    elif v2 == "HIGH" and v3 == "MEDIUM":
        hm += 1
    elif v2 == "HIGH" and v3 == "HIGH":
        hh += 1
    elif v2 == "HIGH" and v3 == "CRITICAL":
        hc += 1

    cveSet.add(cve)

mat = [[ll, lm, lh, lc], [ml, mm, mh, mc], [hl, hm, hh, hc]]
mat = np.matrix(mat)
print(mat)
print(np.matrix.sum(mat))