cnn = open('./Actual-Predicted_cnn.csv', 'r')
dnn = open('./Actual-Predicted_dnn.csv', 'r')
lr = open('./Actual-Predicted_lr.csv', 'r')
svr = open('./Actual-Predicted_svr.csv', 'r')


print("******************** CNN - Results ********************")
actualV3s, correctV3s = {}, {}
for line in cnn:
    line = line.replace('\n', '').rsplit(';')
    actualV3 = float(line[1])
    predV3 = float(line[2])

    actualV3Label, predV3Label = "", ""
    if actualV3 > 0 and actualV3 < 4.0:
        actualV3Label = "L"
    elif actualV3 < 7.0:
        actualV3Label = "M"
    elif actualV3 < 9.0:
        actualV3Label = "H"
    elif actualV3 <= 10.0:
        actualV3Label = "C"


    if predV3 > 0 and predV3 < 4.0:
        predV3Label = "L"
    elif predV3 < 7.0:
        predV3Label = "M"
    elif predV3 < 9.0:
        predV3Label = "H"
    elif predV3 <= 10.0:
        predV3Label = "C"

    if actualV3Label not in actualV3s:
        actualV3s[actualV3Label] = 1
    else:
        actualV3s[actualV3Label] += 1

    if actualV3Label not in correctV3s:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] = 1
    else:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] += 1

print(actualV3s)
print(correctV3s)

print("******************** DNN - Results ********************")
actualV3s, correctV3s = {}, {}
for line in dnn:
    line = line.replace('\n', '').rsplit(';')
    actualV3 = float(line[0])
    predV3 = float(line[1])

    actualV3Label, predV3Label = "", ""
    if actualV3 > 0 and actualV3 < 4.0:
        actualV3Label = "L"
    elif actualV3 < 7.0:
        actualV3Label = "M"
    elif actualV3 < 9.0:
        actualV3Label = "H"
    elif actualV3 <= 10.0:
        actualV3Label = "C"


    if predV3 > 0 and predV3 < 4.0:
        predV3Label = "L"
    elif predV3 < 7.0:
        predV3Label = "M"
    elif predV3 < 9.0:
        predV3Label = "H"
    elif predV3 <= 10.0:
        predV3Label = "C"

    if actualV3Label not in actualV3s:
        actualV3s[actualV3Label] = 1
    else:
        actualV3s[actualV3Label] += 1

    if actualV3Label not in correctV3s:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] = 1
    else:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] += 1

print(actualV3s)
print(correctV3s)


print("******************** LR - Results ********************")
actualV3s, correctV3s = {}, {}
for line in lr:
    line = line.replace('\n', '').rsplit(';')
    actualV3 = float(line[0])
    predV3 = float(line[1])

    actualV3Label, predV3Label = "", ""
    if actualV3 > 0 and actualV3 < 4.0:
        actualV3Label = "L"
    elif actualV3 < 7.0:
        actualV3Label = "M"
    elif actualV3 < 9.0:
        actualV3Label = "H"
    elif actualV3 <= 10.0:
        actualV3Label = "C"


    if predV3 > 0 and predV3 < 4.0:
        predV3Label = "L"
    elif predV3 < 7.0:
        predV3Label = "M"
    elif predV3 < 9.0:
        predV3Label = "H"
    elif predV3 <= 10.0:
        predV3Label = "C"

    if actualV3Label not in actualV3s:
        actualV3s[actualV3Label] = 1
    else:
        actualV3s[actualV3Label] += 1

    if actualV3Label not in correctV3s:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] = 1
    else:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] += 1

print(actualV3s)
print(correctV3s)


print("******************** SVR - Results ********************")
actualV3s, correctV3s = {}, {}
for line in svr:
    line = line.replace('\n', '').rsplit(';')
    actualV3 = float(line[0])
    predV3 = float(line[1])

    actualV3Label, predV3Label = "", ""
    if actualV3 > 0 and actualV3 < 4.0:
        actualV3Label = "L"
    elif actualV3 < 7.0:
        actualV3Label = "M"
    elif actualV3 < 9.0:
        actualV3Label = "H"
    elif actualV3 <= 10.0:
        actualV3Label = "C"


    if predV3 > 0 and predV3 < 4.0:
        predV3Label = "L"
    elif predV3 < 7.0:
        predV3Label = "M"
    elif predV3 < 9.0:
        predV3Label = "H"
    elif predV3 <= 10.0:
        predV3Label = "C"

    if actualV3Label not in actualV3s:
        actualV3s[actualV3Label] = 1
    else:
        actualV3s[actualV3Label] += 1

    if actualV3Label not in correctV3s:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] = 1
    else:
        if actualV3Label == predV3Label:
            correctV3s[actualV3Label] += 1

print(actualV3s)
print(correctV3s)