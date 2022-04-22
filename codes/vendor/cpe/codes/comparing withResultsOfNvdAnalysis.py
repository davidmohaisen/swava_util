import json, re
cpeDatabase = open('../output/official-cpe-dictionary_v2.3.xml', 'rb')
# vendorInconsistentChainsFromNVD = open('../../nvd/output2.0/vendorChains-Final.xlsx', 'rb')
vendorInconsistentChainsFromNVD_Relaxed = open('../RelaxedvendorChains-Final.xlsx', 'rb')

cpe22Database = open('../output/official-cpe-dictionary_v2.2.xml', 'rb')
# cpe22Database = open('../output/archive-official-cpe-dictionary_v2.2-20181025-000915.xml', 'rb')          #archive data from https://nvd.nist.gov/feeds/xml/cpe/dictionary/

vendProd1 = {}
inconsisVendors = {}
for line1 in vendorInconsistentChainsFromNVD_Relaxed:
    line1 = line1.decode().replace('\n', '')
    line1Json = json.loads(line1)
    inconsisVendors = line1Json
# print(inconsisVendors)

print("------------------------------ CPE 2.3 results ------------------------")
for line in cpeDatabase:
    line = line.decode().replace('\n', '').lstrip().rstrip()
    if line.startswith('<cpe-23:cpe23-item'):
        vendor = line.rsplit(':')[4]
        product = line.rsplit(':')[5]
        # print(vendor, product)
        if vendor in vendProd1:
            if product not in vendProd1[vendor]:
                vendProd1[vendor].append(product)
        else:
            vendProd1[vendor] = []
            vendProd1[vendor].append(product)

dbProductCount = 0
for itm in vendProd1:
    dbProductCount += len(vendProd1[itm])

print("The database has ", dbProductCount, "products corresponding to ", len(vendProd1), " vendors.")
# print("------------------------------ CPE 2.2 results ------------------------")
# for line in cpe22Database:
#     line = line.decode().replace('\n', '').lstrip().rstrip()
#     if line.startswith('<cpe-item'):
#         vendor = line.rsplit(':')[2]
#         product = line.rsplit(':')[3]
#         # print(vendor, product)
#         if vendor in vendProd1:
#             vendProd1[vendor].add(product)
#         else:
#             vendProd1[vendor] = set()
#             vendProd1[vendor].add(product)

print(vendProd1)
print("---------------------------------")
# for itm in vendProd1:
#     print(itm, vendProd1[itm])

x = json.dumps(vendProd1)
with open('./cpeVendProd.json', 'w') as fp:
    fp.write(x)
c=0
presenceCount = {}
vendorProdInconsistency = {}
for itm in inconsisVendors:
    for i in range(len(inconsisVendors[itm])):
        if inconsisVendors[itm][i] in vendProd1:
            # print(inconsisVendors[itm][i], inconsisVendors[itm])
            if itm not in presenceCount:
                presenceCount[itm] = set()
                presenceCount[itm].add(inconsisVendors[itm][i])
            else:
                presenceCount[itm].add(inconsisVendors[itm][i])
                # print(itm, inconsisVendors[itm][i], inconsisVendors[itm], presenceCount[itm])
                # c+=1
            if itm not in vendorProdInconsistency:
                vendorProdInconsistency[itm] = set()
                vendorProdInconsistency[itm] = re.sub(r'\{|\}|\'', '', str(vendProd1[inconsisVendors[itm][i]])).replace(', ', ',')
            else:
                vendorProdInconsistency[itm] = vendorProdInconsistency[itm] + ',' + re.sub(r'\{|\}|\'', '', str(vendProd1[inconsisVendors[itm][i]])).replace(', ', ',')

print("------- Consistent dataset is stored in dictionary 'presenceCount' ---------")
print(presenceCount)

print("------------- Quantifying vendor inconsistency --------------")
vendorinconsistencyCount = 0
replacableVendorCount = 0
onlyRedundantVendors = []
for itmi in presenceCount:
    if len(presenceCount[itmi]) > 1:
        vendorinconsistencyCount += len(presenceCount[itmi])
        # print(itmi, presenceCount[itmi])
        replacableVendorCount+=1
        onlyRedundantVendors.append(itm)

print("Number of vendors impacted by the inconsistency is: ", vendorinconsistencyCount, ". The ", vendorinconsistencyCount, "inconsistent vendors can be replaced by ", replacableVendorCount, "vendors")
print(vendorinconsistencyCount, replacableVendorCount)

print("------------- Vendor inconsistency quantification Done! --------------")

print("------------ Qantifying product inconsistency begins------------------------")
cnt = 0
vendorProdRedundancy, vendorProdWoRedundancy = {}, {}
for itm in vendorProdInconsistency:
    prodTkn = vendorProdInconsistency[itm].rsplit(',')
    # print(prodTkn)
    vendor = itm

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
        if vendor not in onlyRedundantVendors:
            # print(vendor)
            cnt += 1
    if len(prodCntSetWoRedundancy) > 0:
        vendorProdWoRedundancy[vendor] = prodCntSetWoRedundancy
        if vendor not in onlyRedundantVendors:
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

print("There are ", len(vendorProdRedundancy.keys() - onlyRedundantVendors), " vendors that are inconsistent because of inconsistencies in their products. ")
# print(len(vendorProdRedundancy.keys() - onlyRedundantVendors))