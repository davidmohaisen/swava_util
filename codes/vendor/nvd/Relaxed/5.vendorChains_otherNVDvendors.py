import json, re
vendorProdWoTkn = open('../output2.0/vendorProdWithout_-Space.xlsx', 'rb')
vendorChain = open('./outputRel/vendorChains-Final.xlsx', 'rb')
vendorChainsProdFile = open('./outputRel/vendorChainsProds-Final.xlsx', 'rb')

c, d, e, f = 0, 0, 0, 0
vendorProds = {}
for line1 in vendorChainsProdFile:
    line1 = line1.decode().replace('\n', '')
    tkn1 = line1.rsplit(':')
    inconsVend = tkn1[0]
    prods = tkn1[1]

    # print(tkn1[1])
    if inconsVend not in vendorProds:
        vendorProds[inconsVend] = prods

vendorsAlreadyInTheProdFile = []
for line2 in vendorChain:
    line2 = line2.decode()
    lineJson = json.loads(line2)
    # print(lineJson)
    for itm in lineJson:
        for i in range(len(lineJson[itm])):
            d+=1
            # print(lineJson[itm][i]) #re.sub(r'\_|\-', '', lineJson[itm][i])
            if lineJson[itm][i] not in vendorsAlreadyInTheProdFile:
                vendorsAlreadyInTheProdFile.append(re.sub(r'\_|\-', '', lineJson[itm][i]))
            # print(lineJson[itm])


xvends = []
for line3 in vendorProdWoTkn:
    line3 = line3.decode().replace('\n', '')
    tkn3 = line3.rsplit(":")
    vend = tkn3[0]
    # vend = re.sub(r'\_|\-', '', tkn3[0])
    prod = tkn3[-1].replace(', ', ',')
    xvends.append(vend)

    # print(prod)
    if vend in vendorsAlreadyInTheProdFile:
        c+=1
        continue
        # print(vend, vendorProds[vend.replace()])
    f+=1
    print(vend, prod)
    with open('./outputRel/vendorChains_OtherNVDvendors.xlsx', 'a') as fw:
        fw.write(str(vend) + ":" +str(prod) + '\n')


for itmv in vendorProds:
    with open('./outputRel/vendorChains_OtherNVDvendors.xlsx', 'a') as fw:
        fw.write(str(itmv) + ":" +str(vendorProds[itmv]) + '\n')

print(c, d, len(vendorsAlreadyInTheProdFile), len(set(vendorsAlreadyInTheProdFile)), e, len(vendorProds), f)

print(set(vendorsAlreadyInTheProdFile) - set(xvends))


# 1334 1366 1249 1108