import re
import numpy as np

def minEditDistance(s1, s2):
    matrix = np.zeros((len(s1) + 1, len(s2) + 1), dtype="int64")

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i-1][j], matrix[i-1][j-1])  # (Insert, Remove, Replace)

    return matrix[len(s1)][len(s2)]

vendorChainsOnlyRedundantVendors = open('../output2.0/vendorChainsProds-Final.xlsx', 'rb')
vendorChainsProdFile = open('../output2.0/vendorChains_OtherNVDvendors.xlsx', 'rb')

vendList = set()
for line in vendorChainsOnlyRedundantVendors:
    vend = line.decode().replace('\n', '').rsplit(":")[0]
    vendList.add(vend)
    # print(line)

cnt = 0
vendorProdRedundancy, vendorProdWoRedundancy = {}, {}
editDist_Count = {}
for vendorLine in vendorChainsProdFile:
    vendorLine = vendorLine.decode().replace('\n', '')
    vendor = vendorLine.rsplit(":")[0]

    prodTkn = vendorLine.rsplit(":")[-1].rsplit(',')
    prodCntSet, prodAbbrSet, prodCntSetWoRedundancy = {}, {}, {}
    prodAlreadyEditDistanced = set()
    editDistancedPairs = set()
    analyzedCombination = {}
    for i in range(len(prodTkn)):
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

        if prodTkn[i] not in prodAlreadyEditDistanced:
            prodAlreadyEditDistanced.add(prodTkn[i])
            prod1 = prodTkn[i]
            prodTknExceptCurrProd = set(prodTkn) - {prod1}
            for prod2 in prodTknExceptCurrProd:
                if prod1+":"+prod2 in editDistancedPairs or prod2+":"+prod1 in editDistancedPairs:
                    continue
                cnt+=1
                p1 = re.sub(r'\.|\_|\-|\\|\/|\+|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\{|\}|\[|\]|\;|\:|\'|\"|\<|\,|\.|\>', '', prod1)
                p2 = re.sub(r'\.|\_|\-|\\|\/|\+|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\{|\}|\[|\]|\;|\:|\'|\"|\<|\,|\.|\>', '', prod2)

                if p1 in analyzedCombination and analyzedCombination[p1] == p2:
                    continue
                elif p2 in analyzedCombination and analyzedCombination[p2] == p1:
                    continue

                analyzedCombination[p1] = p2
                analyzedCombination[p2] = p1

                editDist = minEditDistance(p1, p2)
                editDistancedPairs.add(prod1+":"+prod2)

                if editDist not in editDist_Count:
                    editDist_Count[editDist] = 1
                else:
                    editDist_Count[editDist] += 1
                if editDist in {0, 1, 2, 3}:
                    out = str(vendor)+":"+str(editDist)+":"+str(prod1)+":"+str(prod2)#+":"+str(re.sub(r'\.|\_|\-|\\|\/', '', prod1))+":"+str(re.sub(r'\.|\_|\-|\\|\/', '', prod2))
                    # print(vendor, editDist, prod1, prod2, re.sub(r'\d', '', p1), re.sub(r'\d', '', p2))
                    with open('../editDistanceVendorProd1Prod2-V3.csv', 'a') as foo:
                        foo.write(out+'\n')
                    # if len(prod1) == len(prod2):
                    #     print(vendor, editDist, prod1, prod2, re.sub(r'\d', '', p1), re.sub(r'\d', '', p2))
                    #     with open('./editDistanceVendorProd1Prod2-EqualLengths-V2.csv', 'a') as foo:
                    #         foo.write(out + '\n')


for itm in editDist_Count:
    print(itm, editDist_Count[itm])
    # with open('./editDistCount-V2.csv', 'a') as foos:
    #     foos.write(str(itm)+":"+str(editDist_Count[itm])+'\n')
print("Total: ", cnt)


# -------------- Quantifying product inconsistencies including duplication due to inconsistent vendors -------------
# There are  3104  inconsistent products (including duplicates) impacting  699  vendors.
# -------------- Analyzing products that are considered inconsistent because they were present in both instances of inconsistent vendors --------------
# There are  642  inconsistent products (excluding duplicates) impacting  185  vendors.
# There are  109  vendors that are inconsistent because of inconsistencies in their products.
#
# Process finished with exit code 0