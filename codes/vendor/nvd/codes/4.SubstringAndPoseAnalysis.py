import json
import re

substringed = open('../output/Final/vendorSubstringMatching.xlsx', 'rb')
posed = open('../output/Final/productPosingAsVendor.xlsx', 'rb')
posedUnposed = open('../output/vendorAsprod-prodAsvendor.xlsx', 'rb')
newAdditions = open('../output2.0/probableInconsistencies-newAdditions.xlsx', 'rb')
vendProds = open('../output2.0/vendorProdWithout_-Space.xlsx', 'rb')

c = 0
repeatingVendorSets, repeatingVendorsChainSet = set(), {}
inconsistencyRemovedVendors, inconsistencyRemovedVendProducts, singularInconsistentVendorMap = {}, {}, {}

vendProdSet, inconsitentVendorSet = {}, {}

for lin in vendProds:
    lin = lin.decode().replace('\n', '')
    venproTkn = lin.rsplit(':')
    vend = venproTkn[0]
    # if "zakon" not in vend:
    #     continue
    prods = venproTkn[-1].replace(', ', ',')
    vendNVD = venproTkn[2].replace(", ", ",")
    # print(vend, vendNVD, prods)

    if vend in vendProdSet:
        vendProdSet[vend] = vendProdSet[vend] + "," + prods
    else:
        # vendProdSet[vend] = set()
        vendProdSet[vend] = prods

    if vend in singularInconsistentVendorMap:
        singularInconsistentVendorMap[vend] = singularInconsistentVendorMap[vend] + vendNVD
    else:
        singularInconsistentVendorMap[vend] = vendNVD

n=0
x=0
uniqueProducts = set()
for itm in vendProdSet:
    prods = vendProdSet[itm].rsplit(',')
    for itmi in range(len(prods)):
        uniqueProducts.add(itm+"_"+prods[itmi])
print(uniqueProducts)
print("Total no. of Products", len(uniqueProducts))
print("Total no. of Vendors", len(vendProdSet))

for itm in singularInconsistentVendorMap:
    inc = singularInconsistentVendorMap[itm]
    if "," in singularInconsistentVendorMap[itm]:
        inct = inc.rsplit(',')
        n+=len(inct)
        x+=1
        print(itm, singularInconsistentVendorMap[itm])
print(n)
print(x)
print(singularInconsistentVendorMap)
exit()

for line1 in substringed:
    line1 = line1.decode().replace('\n', '')
    # print(line1)
    v1, v2 = line1.rsplit(':')[0], line1.rsplit(':')[1]
    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1).strip().lower()
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2).strip().lower()

    # # ------ Starts:  Stats for table collection -------
    # if len(line1.rsplit(':')[-1].rsplit(',')) > 1:# and "set()" not in line2.rsplit(':')[-1]:
    # # if "set()" in line1.rsplit(':')[-1]:  #
    #     uniqueVendors.add(v1)
    #     uniqueVendors.add(v2)
    #     n += 1
    #     # continue
    #     print(line2.rsplit(':')[-1])
    # # ------ Ends:  Stats for table collection -------

    if len(v1) <= len(v2):
        repeatingVends1 = v1+":"+v2
        repeatingVendorSets.add(repeatingVends1)
    else:
        repeatingVends1 = v2+":"+v1
        repeatingVendorSets.add(repeatingVends1)
    # print(repeatingVends1)
    c+=1
print("Substring: ", len(repeatingVendorSets))


for line1 in newAdditions:
    line1 = line1.decode().replace('\n', '')
    # print(line1)
    v1, v2 = line1.rsplit(':')[0], line1.rsplit(':')[1]

    # # ------ Starts:  Stats for table collection -------
    # if len(line1.rsplit(':')[-1].rsplit(',')) > 1:# and "set()" not in line2.rsplit(':')[-1]:
    # # if "set()" in line1.rsplit(':')[-1]:  #
    #     uniqueVendors.add(v1)
    #     uniqueVendors.add(v2)
    #     n += 1
    #     # continue
    #     print(line2.rsplit(':')[-1])
    # # ------ Ends:  Stats for table collection -------

    if len(v1) <= len(v2):
        repeatingVends1 = v1+":"+v2
        repeatingVendorSets.add(repeatingVends1)
    else:
        repeatingVends1 = v2+":"+v1
        repeatingVendorSets.add(repeatingVends1)
    # print(repeatingVends1)
    c+=1
print("New Additions: ", len(repeatingVendorSets))

lcn = 0
for line2 in posed:
    line2 = line2.decode().replace('\n', '')
    v1, v2 = line2.rsplit(':')[0], line2.rsplit(':')[1]
    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1).strip().lower()
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2).strip().lower()

    # # ------ Starts:  Stats for table collection -------
    # lcn += 1
    # if lcn < 180:
    #     continue
    # if len(line2.rsplit(':')[-1].rsplit(',')) > 1:# and "set()" not in line2.rsplit(':')[-1]:
    # # if "set()" in line2.rsplit(':')[-1]:  #
    #     uniqueVendors.add(v1)
    #     uniqueVendors.add(v2)
    #     n += 1
    #     # continue
    #     print(line2.rsplit(':')[-1])
    # # ------ Ends:  Stats for table collection -------

    if len(v1) <= len(v2):
        repeatingVends2 = v1+":"+v2
        repeatingVendorSets.add(repeatingVends2)
    else:
        repeatingVends2 = v2+":"+v1
        repeatingVendorSets.add(repeatingVends2)
    # print(repeatingVends2)
    c+=1

print("Product Matching: ", len(repeatingVendorSets))

for line2 in posedUnposed:
    line2 = line2.decode().replace('\n', '')

    v1, v2 = line2.rsplit(':')[0], line2.rsplit(':')[1]
    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1).strip().lower()
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2).strip().lower()

    # # ------ Starts:  Stats for table collection -------
    # if len(line2.rsplit(':')[-1].rsplit(',')) > 1:# and "set()" not in line2.rsplit(':')[-1]:
    # # if "set()" in line2.rsplit(':')[-1]:  #
    #     uniqueVendors.add(v1)
    #     uniqueVendors.add(v2)
    #     n += 1
    #     # continue
    #     print(line2.rsplit(':')[-1])
    # # ------ Ends:  Stats for table collection -------

    if len(v1) <= len(v2):
        repeatingVends2 = v1+":"+v2
        repeatingVendorSets.add(repeatingVends2)
    else:
        repeatingVends2 = v2+":"+v1
        repeatingVendorSets.add(repeatingVends2)
    # print(repeatingVends2)
    c+=1

# # ------ Starts:  Stats for table collection -------
# print(n, len(uniqueVendors))
# print(uniqueVendors)
# # for itm in uniqueVendors:
# exit()
# #     print(itm, )
# # ------ Ends:  Stats for table collection -------

print("Prod As Vendor and Vendor in Products: ", c, len(repeatingVendorSets))

d = 0
for probRepVendor in repeatingVendorSets:
    d = 0

    v1 = probRepVendor.rsplit(":")[0]
    v2 = probRepVendor.rsplit(":")[1]


    if len(repeatingVendorsChainSet) == 0:
        repeatingVendorsChainSet[v1] = set()
        repeatingVendorsChainSet[v1].add(v2)
    else:
        for itm in repeatingVendorsChainSet.copy():
            if v1 == itm or v2 == itm or v1 in repeatingVendorsChainSet[itm] or v2 in repeatingVendorsChainSet[itm]:
                if v1 == itm:
                    repeatingVendorsChainSet[itm].add(v2)
                elif v2 == itm:
                    repeatingVendorsChainSet[itm].add(v1)
                else:
                    repeatingVendorsChainSet[itm].add(v1)
                    repeatingVendorsChainSet[itm].add(v2)
            else:
                repeatingVendorsChainSet[v1] = set()
                repeatingVendorsChainSet[v1].add(v2)

print("---------------- Yha tk hua ----------------")

print(repeatingVendorsChainSet)
print(len(repeatingVendorsChainSet))

print("---------------- countering the instances that depend on the order in which elements are entered into the set ----------------")

tmprepeatingVendorsChainSet = repeatingVendorsChainSet.copy()
# repeatingVendorsChainSet = {}

for itm in tmprepeatingVendorsChainSet:
    for itm1 in tmprepeatingVendorsChainSet:
        try:
            if itm in repeatingVendorsChainSet[itm1]:
                repeatingVendorsChainSet.pop(itm)
                # print("Popped item: ", itm)
        except:
            continue

print(tmprepeatingVendorsChainSet)
print(repeatingVendorsChainSet)
print(len(repeatingVendorsChainSet))
# print(tmprepeatingVendorsChainSet.keys()-repeatingVendorsChainSet.keys())
print(len(tmprepeatingVendorsChainSet.keys()-repeatingVendorsChainSet.keys()))
# exit()



# for itmk in inconsistencyRemovedVendProducts:
#     print(itmk, inconsistencyRemovedVendProducts[itmk])

# print(inconsistencyRemovedVendProducts['dinkumsoft'])
# print(repeatingVendorsChainSet['dinkumsoft'])
# print(vendProdSet['dinkumsoft'])
# print(vendProdSet['dinkumsoft.com'])


print(inconsistencyRemovedVendors, "Kali hai?")

notInNewDataset = set()
for itmV in repeatingVendorsChainSet:
    # print(itmV, singularInconsistentVendorMap[itmV])
    if itmV not in inconsistencyRemovedVendors:
        if itmV not in singularInconsistentVendorMap:
            notInNewDataset.add(itmV)
            continue
        inconsistencyRemovedVendors[itmV] = set()
        tokenizerVendor = singularInconsistentVendorMap[itmV].rsplit(',')
        for tk in range(len(tokenizerVendor)):
            inconsistencyRemovedVendors[itmV].add(tokenizerVendor[tk])

        otherformsSet = repeatingVendorsChainSet[itmV]
        for ven in otherformsSet:
            try:
                tokenizerVendor = singularInconsistentVendorMap[ven].rsplit(',')
            except:
                notInNewDataset.add(ven)
                continue

            for tk in range(len(tokenizerVendor)):
                inconsistencyRemovedVendors[itmV].add(tokenizerVendor[tk])
    else:
        print(" Nahi Hai!!!")

print(inconsistencyRemovedVendors)
print(len(inconsistencyRemovedVendors))
print("Count of vendors present in old dataset and not in new dataset", len(notInNewDataset), "They are: ", notInNewDataset)
# exit()

overallImpactedVendors = 0
for itm in inconsistencyRemovedVendors:
    overallImpactedVendors += len(inconsistencyRemovedVendors[itm])

print("Without Dashed inconsistencies, the number of inconsistent vendors is: ", overallImpactedVendors, ". These vendors can be replaced by ", len(inconsistencyRemovedVendors), " vendros")

# # ------ Starts:  Stats for table collection -------
# for itm in singularInconsistentVendorMap:
#     if "," in singularInconsistentVendorMap[itm]:
#         print(itm, singularInconsistentVendorMap[itm])
#         tmp = singularInconsistentVendorMap[itm].rsplit(',')
#         for i in range(len(tmp)):
#             uniqueVendors.add(tmp[i])
#         n+=1
# print(n, len(uniqueVendors))
# print(uniqueVendors)
# exit()
# # ------ Ends:  Stats for table collection -------

for itmF in singularInconsistentVendorMap:
    if itmF not in inconsistencyRemovedVendors and "," in singularInconsistentVendorMap[itmF]:
        # for keyF in inconsistencyRemovedVendors:
        #     if itmF in inconsistencyRemovedVendors[itmF]:
        #         continue
        inconsistencyRemovedVendors[itmF] = set()                                                   # Mapping inconsistencies with original vendor names in the NVD
        tknVendors = singularInconsistentVendorMap[itmF].rsplit(',')
        for xF in range(len(tknVendors)):
            inconsistencyRemovedVendors[itmF].add(tknVendors[xF])                                   # added inconsistent vendors as individual elements in the set (those with underscores and hyphens)

print("----------------- After Adding the Dashed related Inconsistencies ----------------")
print(inconsistencyRemovedVendors)
print(len(inconsistencyRemovedVendors))

overallImpactedVendorsWithDashed = 0
for itm in inconsistencyRemovedVendors:
    overallImpactedVendorsWithDashed += len(inconsistencyRemovedVendors[itm])
print("With Dashed inconsistencies, the number of inconsistent vendors is: ", overallImpactedVendorsWithDashed, ". These vendors can be replaced by ", len(inconsistencyRemovedVendors), " vendros")

inconsistencyRemovedVendorsJsonOut = {}
for lol in inconsistencyRemovedVendors:
    # print(lol, ":", list(inconsistencyRemovedVendors[lol]))
    inconsistencyRemovedVendorsJsonOut[lol] = list(inconsistencyRemovedVendors[lol])

print(inconsistencyRemovedVendorsJsonOut)
print(len(inconsistencyRemovedVendorsJsonOut))

with open('../output2.0/vendorChains-Final.xlsx', 'w') as f:
    json.dump(inconsistencyRemovedVendorsJsonOut, f)


# for itmVen in inconsistencyRemovedVendors:
#     inconsistencyRemovedVendProducts[itmVen] = vendProdSet[itmVen]

print("-------------- Vendor Product Mapping ----------------------")
# print(vendProdSet)
ignoredDuringProductMapping = set()
for itm in inconsistencyRemovedVendors:
    if itm not in inconsistencyRemovedVendProducts:
        inconsistencyRemovedVendProducts[itm] = set()
        inconsistencyRemovedVendProducts[itm] = vendProdSet[itm]

        otherformsSet = inconsistencyRemovedVendors[itm]

        for ven in otherformsSet:
            ven = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', ven).strip().lower()
            if ven not in inconsistencyRemovedVendProducts:
                try:
                    inconsistencyRemovedVendProducts[itm] = inconsistencyRemovedVendProducts[itm] + "," + vendProdSet[ven]
                except:
                    ignoredDuringProductMapping.add(ven)
                    print(itm, "irgnored for ", ven)
                    continue

    else:
        inconsistencyRemovedVendProducts[itm] = inconsistencyRemovedVendProducts[itm] + "," + vendProdSet[itm]
        otherformsSet = inconsistencyRemovedVendors[itm]

        for ven in otherformsSet:
            ven = re.sub(r'\-|\_', '', ven)
            if ven not in inconsistencyRemovedVendProducts:
                inconsistencyRemovedVendProducts[itm] = inconsistencyRemovedVendProducts[itm] + "," + vendProdSet[ven]

print(inconsistencyRemovedVendProducts)
print(len(inconsistencyRemovedVendProducts))


for itmVp in inconsistencyRemovedVendProducts:
    with open('../output2.0/vendorChainsProds-Final.xlsx', 'a') as f:
        f.write(str(itmVp)+":"+inconsistencyRemovedVendProducts[itmVp]+'\n')
    # print(itmVp, inconsistencyRemovedVendProducts[itmVp])

print("-------------------- Testing for correctness of vendor chain --------------------")
for itm in repeatingVendorsChainSet:
    for itm1 in repeatingVendorsChainSet:
        if itm in repeatingVendorsChainSet[itm1]:
            print(itm, itm1, repeatingVendorsChainSet[itm], repeatingVendorsChainSet[itm1])