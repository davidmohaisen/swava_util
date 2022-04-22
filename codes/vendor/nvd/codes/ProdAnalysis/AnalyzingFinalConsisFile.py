f = open('./cve_vendProd_ConsIncons_pdd_date.csv', 'rb')

inconsVendorSet, inconsProdSet, consVendorSet, consProdSet, preConsVendorSet, preConsProdSet = set(), set(), set(), set(), set(), set()
vendorsImpactedByProductSet = set()
for line in f:
    line = line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    inconVendor = line[1]
    inconProd = inconVendor+"-"+line[2]
    consVendor = line[3]
    consProd = line[4]
    if consVendor != "":
        preConsVendorSet.add(inconVendor)
    if consProd != "":
        preConsProdSet.add(inconVendor+"-"+inconProd)
        vendorsImpactedByProductSet.add(inconVendor)

    if consVendor == "":
        consVendor = inconVendor
    if consProd == "":
        consProd = inconProd
    else:
        consProd = consVendor + "-" + consProd
    pdd = line[5]
    inconsVendorSet.add(inconVendor)
    inconsProdSet.add(inconProd)
    consVendorSet.add(consVendor)
    consProdSet.add(consProd)

print("# Inconsistent Vendor Count: ", len(inconsVendorSet))
print("# Inconsistent Product Count: ", len(inconsProdSet))
print("# Pre Consistent Vendor Count: ", len(preConsVendorSet))
print("# Pre Consistent Product Count: ", len(preConsProdSet))
print("# Overall Consistent Vendor Count: ", len(consVendorSet))
print("# Overall Consistent Product Count: ", len(consProdSet))
print("# Vendors Impacted by Product consistencies: ", len(vendorsImpactedByProductSet))
# print(line)
print(vendorsImpactedByProductSet)