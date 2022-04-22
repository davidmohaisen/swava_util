import numpy as np

# f = open('./Actual-Predicted_cnn_all.csv', 'r')
f = open('./Actual-Predicted_cnn-TestData.csv', 'r')

lh, lm, lc, ml, mh, mc, hl, hm, hc, ll, mm, hh = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

mat = [[ll, lm, lh, lc], [ml, mm, mh, mc], [hl, hm, hh, hc]]

n=0
for line in f:
    line = line.replace('\n', '')
    # print(line)
    # exit()
    tkn = line.rsplit(';')
    v2 = float(tkn[0])
    pv3 = float(tkn[2])
    v2Lbl = ""
    pv3Lbl = ""
    n+=1

    if v2 < 4:
        v2Lbl = "LOW"
    elif v2 < 7:
        v2Lbl = "MEDIUM"
    elif v2 >= 7:
        v2Lbl = "HIGH"

    if pv3 < 4:
        pv3Lbl = "LOW"
    elif pv3 < 7:
        pv3Lbl = "MEDIUM"
    elif pv3 < 9:
        pv3Lbl = "HIGH"
    elif pv3 >= 9:
        pv3Lbl = "CRITICAL"


    if v2Lbl == "LOW" and pv3Lbl == "MEDIUM":
        lm += 1
    elif v2Lbl == "LOW" and pv3Lbl == "LOW":
        ll += 1
    elif v2Lbl == "LOW" and pv3Lbl == "HIGH":
        lh += 1
    elif v2Lbl == "LOW" and pv3Lbl == "CRITICAL":
        lc += 1
    elif v2Lbl == "MEDIUM" and pv3Lbl == "LOW":
        ml += 1
    elif v2Lbl == "MEDIUM" and pv3Lbl == "MEDIUM":
        mm += 1
    elif v2Lbl == "MEDIUM" and pv3Lbl == "HIGH":
        mh += 1
    elif v2Lbl == "MEDIUM" and pv3Lbl == "CRITICAL":
        mc += 1
    elif v2Lbl == "HIGH" and pv3Lbl == "LOW":
        hl += 1
    elif v2Lbl == "HIGH" and pv3Lbl == "MEDIUM":
        hm += 1
    elif v2Lbl == "HIGH" and pv3Lbl == "HIGH":
        hh += 1
    elif v2Lbl == "HIGH" and pv3Lbl == "CRITICAL":
        hc += 1
    # print(line)

mat = [[ll, lm, lh, lc], [ml, mm, mh, mc], [hl, hm, hh, hc]]
mat = np.matrix(mat)
print(mat)
# print(mat*(100/73556))
print(np.matrix.sum(mat))
print(n)
# print(len(cveSet), len(movesCves))
# print(len(cveSet-movesCves))
# print(cveSet-movesCves)