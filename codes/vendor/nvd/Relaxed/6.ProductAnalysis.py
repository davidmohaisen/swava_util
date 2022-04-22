import re

vendorChainsOnlyRedundantVendors = open('./outputRel/vendorChainsProds-Final.xlsx', 'rb')
vendorChainsProdFile = open('./outputRel/vendorChains_OtherNVDvendors.xlsx', 'rb')

vendList = set()
for line in vendorChainsOnlyRedundantVendors:
    vend = line.decode().replace('\n', '').rsplit(":")[0]
    vendList.add(vend)
    # print(line)

cnt = 0
vendorProdRedundancy, vendorProdWoRedundancy = {}, {}
for vendorLine in vendorChainsProdFile:
    vendorLine = vendorLine.decode().replace('\n', '')
    vendor = vendorLine.rsplit(":")[0]

    prodTkn = vendorLine.rsplit(":")[-1].rsplit(',')
    prodCntSet, prodAbbrSet, prodCntSetWoRedundancy = {}, {}, {}
    for i in range(len(prodTkn)):
        prodWoDash = re.sub(r'\_|\-', '', prodTkn[i])

        if prodWoDash in prodCntSet:
            prodCntSet[prodWoDash].append(prodTkn[i])
        else:
            prodCntSet[prodWoDash] = []
            prodCntSet[prodWoDash].append(prodTkn[i])

        for i3 in range(len(prodTkn)):
            abbreviatedProd = ""
            prodSpaceTkn = re.sub(r'\_|\-|\.', ' ', prodTkn[i3]).rsplit(' ')

            if len(prodSpaceTkn) > 1:
                for i2 in range(len(prodSpaceTkn)):
                    if prodSpaceTkn[i2] == "":
                        continue
                    if abbreviatedProd == "":
                        abbreviatedProd = prodSpaceTkn[i2][0]
                    else:
                        abbreviatedProd = str(abbreviatedProd) + str(prodSpaceTkn[i2][0])

            if abbreviatedProd == "":
                continue
            if abbreviatedProd == prodTkn[i]:
                if abbreviatedProd in prodAbbrSet:
                    prodAbbrSet[abbreviatedProd].append(prodTkn[i3])
                else:
                    prodAbbrSet[abbreviatedProd] = []
                    prodAbbrSet[abbreviatedProd].append(prodTkn[i3])


    for kItm in prodCntSet.copy():
        if len(prodCntSet[kItm]) < 2:
            # print(prodCntSet[kItm])
            prodCntSet.pop(kItm)
        if kItm in prodCntSet:
            prodCntSetWoRedundancy[kItm] = set(prodCntSet[kItm])

    # print(prodCntSet)
    # print("Set Wala: ", prodCntSetWoRedundancy)
    if len(prodCntSet) > 0:
        vendorProdRedundancy[vendor] = (prodCntSet)
        if vendor not in vendList:
            # print(vendor)
            cnt += 1
    if len(prodCntSetWoRedundancy) > 0:
        vendorProdWoRedundancy[vendor] = prodCntSetWoRedundancy
        if vendor not in vendList:
            # print(vendor)
            cnt += 1

    # if len(prodAbbrSet) > 0:
    #     print(vendor, prodAbbrSet)
    #     cnt+=1

# print(cnt)
# print(len(vendorProdRedundancy), vendorProdRedundancy)
print("-------------- Quantifying product inconsistencies including duplication due to inconsistent vendors -------------")
productIncoonsCountIncludingDuplication = 0
for itm in vendorProdRedundancy:
    for itmP in vendorProdRedundancy[itm]:
        productIncoonsCountIncludingDuplication += len(vendorProdRedundancy[itm][itmP])

print("There are ", productIncoonsCountIncludingDuplication, " inconsistent products (including duplicates) impacting ", len(vendorProdRedundancy), " vendors.")

# print(len(vendorProdWoRedundancy), vendorProdWoRedundancy)
print("-------------- Analyzing products that are considered inconsistent because they were present in both instances of inconsistent vendors --------------")
nonduplicationProducts = 0
for itm in vendorProdWoRedundancy.copy():
    for itmP in vendorProdWoRedundancy[itm].copy():
        if len(vendorProdWoRedundancy[itm][itmP]) == 1:
            vendorProdWoRedundancy[itm].pop(itmP)
        if itmP in vendorProdWoRedundancy[itm]:
            nonduplicationProducts += len(vendorProdWoRedundancy[itm][itmP])
    if len(vendorProdWoRedundancy[itm]) == 0:
        vendorProdWoRedundancy.pop(itm)
# print(len(vendorProdWoRedundancy), nonduplicationProducts, vendorProdWoRedundancy)

print("There are ", nonduplicationProducts, " inconsistent products (excluding duplicates) impacting ", len(vendorProdWoRedundancy), " vendors.")

print("There are ", len(vendorProdRedundancy.keys() - vendList), " vendors that are inconsistent because of inconsistencies in their products. ")
# print(len(vendorProdRedundancy.keys() - onlyRedundantVendors))