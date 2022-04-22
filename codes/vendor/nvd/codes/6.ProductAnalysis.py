import re, json

vendorChainsOnlyRedundantVendors = open('../output2.0/vendorChainsProds-Final.xlsx', 'rb')
vendorChainsProdFile = open('../output2.0/vendorChains_OtherNVDvendors.xlsx', 'rb')

vendList = set()
for line in vendorChainsOnlyRedundantVendors:
    vend = line.decode().replace('\n', '').rsplit(":")[0]
    vendList.add(vend)
    # print(line)

cnt = 0
vendorProdWoIncons = {}
overallInconsCount = {}
overallRedundants = {}

for vendorLine in vendorChainsProdFile:
    vendorLine = vendorLine.decode().replace('\n', '')
    vendor = vendorLine.rsplit(":")[0]
    PreRedundantProds, RedundantProds, WoTokenProds, prodAbbrSet, overallProdSet, vendorInconsCount = {}, {}, {}, {}, {}, {"Redundancy": 0, "Abbreviation": 0, "Token": 0}

    tkn = vendorLine.rsplit(":")[-1].rsplit(',')
    # removing redundants
    for i in range(len(tkn)):
        if tkn[i] not in PreRedundantProds:
            PreRedundantProds[tkn[i]] = 1
        else:
            PreRedundantProds[tkn[i]] += 1

    for ktm in PreRedundantProds:
        if PreRedundantProds[ktm] > 2:
            if ktm not in RedundantProds:
                RedundantProds[ktm] = PreRedundantProds[ktm]
                vendorInconsCount["Redundancy"] += PreRedundantProds[ktm]
            # else:
            #     RedundantProds[ktm] += PreRedundantProds[ktm]
            #     vendorInconsCount["Redundancy"] += PreRedundantProds[ktm]

    prodSet = RedundantProds.keys()
    #  redundants removed

    analyzedProdSet = set()        # store the products inserted as non keys (i.e., values)
    prodCntSet, prodCntSetWoRedundancy = {}, {}

    for prd in prodSet:
        tknzdProd = re.sub(r'\.|\_|\-|\\|\/|\+|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\{|\}|\[|\]|\;|\:|\'|\"|\<|\,|\.|\>', '', prd)
        if tknzdProd not in WoTokenProds:
            WoTokenProds[tknzdProd] = set()
            WoTokenProds[tknzdProd].add(prd)
            analyzedProdSet.add(prd)
            vendorInconsCount["Token"] += 1
        else:
            WoTokenProds[tknzdProd].add(prd)
            analyzedProdSet.add(prd)
            vendorInconsCount["Token"] += 1


    for itm in WoTokenProds:
        if len(WoTokenProds[itm]) > 1:
            print(itm, WoTokenProds[itm])
    overallProdSet = WoTokenProds

    for prd in prodSet:
        abbreviatedProd = ""
        tknzdProd = re.sub(r'\.|\_|\-|\\|\/|\+|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\{|\}|\[|\]|\;|\:|\'|\"|\<|\,|\.|\>', '', prd)
        prodSpaceTkn = re.sub(r'\.|\_|\-|\\|\/|\+|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\{|\}|\[|\]|\;|\:|\'|\"|\<|\,|\.|\>', ' ', prd).rsplit(' ')

        if len(prodSpaceTkn) <= 1:
            continue
        elif len(prodSpaceTkn) > 1:
            for i2 in range(len(prodSpaceTkn)):
                if prodSpaceTkn[i2] == "" or prodSpaceTkn[i2] == " ":
                    continue
                if abbreviatedProd == "":
                    abbreviatedProd = prodSpaceTkn[i2][0]
                else:
                    abbreviatedProd = str(abbreviatedProd) + str(prodSpaceTkn[i2][0])

        if abbreviatedProd == "":
            continue
        if abbreviatedProd in prodSet or abbreviatedProd in tknzdProd:
            if prd not in prodAbbrSet:
                prodAbbrSet[prd] = set()
                prodAbbrSet[prd].add(prd)
                prodAbbrSet[prd].add(abbreviatedProd)
                analyzedProdSet.add(prd)
                analyzedProdSet.add(abbreviatedProd)
                vendorInconsCount["Abbreviation"] += 2
                print(prd, abbreviatedProd)

        added = 0
        for itm in overallProdSet:
            if prd in overallProdSet[itm]:
                overallProdSet[itm].add(abbreviatedProd)
                added = 1
            elif abbreviatedProd in overallProdSet[itm]:
                overallProdSet[itm].add(prd)
                added = 1
        if added == 0:
            overallProdSet[prd] = set()
            overallProdSet[prd].add(prd)
            overallProdSet[prd].add(abbreviatedProd)

    allprodSet = prodSet - analyzedProdSet
    for prodkys in allprodSet:
        overallProdSet[prodkys] = set()
        overallProdSet[prodkys].add(prodkys)
    if vendor not in vendorProdWoIncons:
        vendorProdWoIncons[vendor] = overallProdSet
    overallInconsCount[vendor] = vendorInconsCount
    # print(vendor, " : ", vendorInconsCount)

print("Done!!!")

token, abbr, redund, vendorsAffected = 0,0,0, 0
for vendor in overallInconsCount:
    # for type in overallInconsCount[vendor]:
    #     if type == "Token":
    token += overallInconsCount[vendor]["Token"]
    abbr += overallInconsCount[vendor]["Abbreviation"]
    redund += overallInconsCount[vendor]["Redundancy"]
    if overallInconsCount[vendor]["Token"] > 0 or overallInconsCount[vendor]["Abbreviation"] > 0 or overallInconsCount[vendor]["Redundancy"] > 0:
        vendorsAffected += 1

print("Token: ", token, "Abbreviation: ", abbr, "Redundancy: ", redund)
print("Total number of affected Vendors is ", vendorsAffected)

y = json.dumps(overallInconsCount)
with open('../OverallInconsCountByVendor.json', 'w') as foo:
    foo.write(y)

x = json.dumps(vendorProdWoIncons)
with open('../ConsistentProdsInVendor.json', 'w') as foo:
    foo.write(x)


# print("-------------- Quantifying product inconsistencies including duplication due to inconsistent vendors -------------")
# productIncoonsCountIncludingDuplication = 0
# for itm in vendorProdRedundancy:
#     for itmP in vendorProdRedundancy[itm]:
#         productIncoonsCountIncludingDuplication += len(vendorProdRedundancy[itm][itmP])
#
# print("There are ", productIncoonsCountIncludingDuplication, " inconsistent products (including duplicates) impacting ", len(vendorProdRedundancy), " vendors.")
#
# # print(len(vendorProdWoRedundancy), vendorProdWoRedundancy)
# print("-------------- Analyzing products that are considered inconsistent because they were present in both instances of inconsistent vendors --------------")
# nonduplicationProducts = 0
# for itm in vendorProdWoRedundancy.copy():
#     for itmP in vendorProdWoRedundancy[itm].copy():
#         if len(vendorProdWoRedundancy[itm][itmP]) == 1:
#             vendorProdWoRedundancy[itm].pop(itmP)
#         if itmP in vendorProdWoRedundancy[itm]:
#             nonduplicationProducts += len(vendorProdWoRedundancy[itm][itmP])
#     if len(vendorProdWoRedundancy[itm]) == 0:
#         vendorProdWoRedundancy.pop(itm)
# # print(len(vendorProdWoRedundancy), nonduplicationProducts, vendorProdWoRedundancy)
#
# print("There are ", nonduplicationProducts, " inconsistent products (excluding duplicates) impacting ", len(vendorProdWoRedundancy), " vendors.")
#
# print("There are ", len(vendorProdRedundancy.keys() - vendList), " vendors that are inconsistent because of inconsistencies in their products. ")
# # print(len(vendorProdRedundancy.keys() - onlyRedundantVendors))