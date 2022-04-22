import math
import numpy as np

f = open('./predicted.csv', 'rb')
f2 = open('../cvss2-3-cwe-R3.csv', 'rb')

cveV2, cveV3 = {}, {}
movementMatPred, movementMatActual = np.zeros((3,4)), np.zeros((3,4))
print(movementMatPred[2][3])
# exit()

def determine_label(baseScore, version):
    if version == 3:
        if baseScore <= 3.9:
            label = 0
        elif baseScore <= 6.9:
            label = 1
        elif baseScore <= 8.9:
            label = 2
        elif baseScore <= 10:
            label = 3
        return label

    elif version == 2:
        if baseScore <= 3.9:
            label = 0
        elif baseScore <= 6.9:
            label = 1
        elif baseScore <= 10:
            label = 2
        return label

uniquev3s = set()
for line in f2:
    line = line.decode().replace('\n', '')
    # print(line)
    tkn = line.rsplit(';')
    print(tkn)

    cve = tkn[0]
    v2label = tkn[1]
    if v2label == "LOW":
        v2label = 0
    if v2label == "MEDIUM":
        v2label = 1
    if v2label == "HIGH":
        v2label = 2
    if cve not in cveV2:
        cveV2[cve] = v2label

    v3label = tkn[-1]

    if v3label != "":
        uniquev3s.add(v3label)
        if v3label == "LOW":
            v3label = 0
        if v3label == "MEDIUM":
            v3label = 1
        if v3label == "HIGH":
            v3label = 2
        if v3label == "CRITICAL":
            v3label = 3
        cveV3[cve] = v3label
print(cveV3)
exit()
for line in f:
    line = line.decode().replace('\n', '')
    # print(line.rsplit(';'))
    # exit()
    cve = line.rsplit(';')[0]
    predScore = float(line.rsplit(';')[1])
    ceiledPredScore = math.ceil(predScore*10)/float(10)
    if ceiledPredScore > 10:
        ceiledPredScore = 10
    predLabel = determine_label(ceiledPredScore, 3)

    v2severity = cveV2[cve]
    # print(predScore, ceiledPredScore, predLabel, v2severity)
    movementMatPred[v2severity][predLabel] += 1

    # try:
    actualv3 = cveV3[cve]
    # except:
    #     print(cve, v3label)
    #     exit()
    movementMatActual[v2severity][actualv3] += 1

print(movementMatPred[0][0])
print(np.matrix.sum(np.asmatrix(movementMatPred)))

print(movementMatActual[0][0])
print(np.matrix.sum(np.asmatrix(movementMatActual)))