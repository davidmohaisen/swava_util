import pickle

f = open('./impactedVendorsByProdIncons.pkl', 'rb')
impactedVendorsByProdIncons = pickle.load(f)
vendor_prodIncons = pickle.load(open('./vendor_prodIncons.pkl', 'rb'))
maxVendor_vendorSet = pickle.load(open('./maxVendor_vendorSet.pkl', 'rb'))

# print(impactedVendorsByProdIncons)
vendset = set()
f2 = open('../../../../ConsistentVendor_prod_info-V2.csv', 'rb')
vendor_productCveCounts = {}
for line in f2:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    vend = line[1]

    if vend == "":
        vend = line[2]
    vendset.add(vend.replace('_', '').replace('-', ''))
    product = line[3]
    date = line[4]
    venP = vend+":"+product
    if venP not in vendor_productCveCounts:
        vendor_productCveCounts[venP] = set()
        vendor_productCveCounts[venP].add(cve)
    else:
        vendor_productCveCounts[venP].add(cve)

print(impactedVendorsByProdIncons - vendset)
print(len(impactedVendorsByProdIncons - vendset))

# set(maxVendor_vendorSet.keys()) -
# set(maxVendor_vendorSet.keys()) -