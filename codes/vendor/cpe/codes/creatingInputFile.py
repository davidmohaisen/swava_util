import re
from difflib import SequenceMatcher

cpeDatabase = open('../output/official-cpe-dictionary_v2.3.xml', 'rb')

vendProds, vendorReplicates = {}, {}
vendProd1 = {}
for line in cpeDatabase:
    line = line.decode().replace('\n', '').lstrip().rstrip()
    if line.startswith('<cpe-23:cpe23-item'):
        # print(line)
        vendor = line.rsplit(':')[4]
        product = line.rsplit(':')[5]
        # print(vendor, product)
        if vendor in vendProd1:
            vendProd1[vendor] = vendProd1[vendor] + "," + product
        else:
            vendProd1[vendor] = product

        vendorWoDash = re.sub(r'\_|\-', '', vendor)

        if vendorWoDash in vendorReplicates:
            vendorReplicates[vendorWoDash].add(vendor)
        else:
            vendorReplicates[vendorWoDash] = set()
            vendorReplicates[vendorWoDash].add(vendor)

        if vendorWoDash in vendProds:
            vendProds[vendorWoDash] = vendProds[vendorWoDash] + "," + product
        else:
            vendProds[vendorWoDash] = product

        # if "_" in vendor or "-" in vendor:
        #     if vendor == vendor1:
        #         print(vendor, vendor1)
dbProductCount = 0
for itm in vendProd1:
    dbProductCount += len(vendProd1[itm])

print("The database has ", dbProductCount, "products corresponding to ", len(vendProd1), " vendors.")
print("---------------------------------")
print("The actual number of vendors in the database is: ", len(vendProd1), "while the numbers after removing dashes and underscores are: ", len(vendProds))
# print(vendProd1.keys() - vendProds.keys())
# print(len(vendorReplicates))
for itm in vendorReplicates.copy():
    if len(vendorReplicates[itm]) < 2:
        vendorReplicates.pop(itm)
print("The number of vendors in the inconsistency dataset is: ", len(vendorReplicates))
print(vendorReplicates)

print("------------------- Starting substring Matching ------------------------")

vendorSet = set(vendProds.keys())                                           # set of overall vendors
vendorSubstringMatch_Count, vendorInProdasVendor_Count, vendorsWithIntersectionProducts_Count=0, 0, 0

print(vendorSet)
ignorableProds = {'server', 'host', 'directory', 'cms', 'httpserver', 'ftpserver', 'ecommerce', 'forum', 'news', 'emailserver', 'php', 'tftpserver', 'contactus', 'webhelpdesk', 'webcalendar', 'webgui', 'admin', 'webadmin', 'mobile', 'whois', 'blogcms', 'downloadmanager', 'expressionengine', 'backupmanager', 'links', 'postfix', 'phpnews', 'minibill', 'calendarscript', 'gallery', 'siteman', 'phplinks', 'web', 'rubyonrails', 'easyscript'}
for vendor1 in vendorSet:
    vendorNotToBeChecked = set()                # set that stores the current vendor
    vendorNotToBeChecked.add(vendor1)
    checkin = vendorSet - vendorNotToBeChecked  # A set without the current vendor
    prodset = vendProds[vendor1]
    prodset = re.sub(r'\_|\-|\ ', '', prodset).rsplit(',')
    prodset = set(prodset)
    # print(vendor1, prodset)
    for prod in prodset:
        if prod in checkin and prod not in ignorableProds:
            match = SequenceMatcher(None, vendor1, prod).find_longest_match(0, len(vendor1), 0, len(prod))
            matchedstring = vendor1[match.a: match.a + match.size]
            # print("aaya")
            prodsInPossibleVendor = set(re.sub(r'\_|\-|\ ', '', vendProds[prod]).rsplit(','))
            if len(matchedstring) >= 3:
                # if vendor1 in prodsInPossibleVendor:
                # if prod in prodsInPossibleVendor:
                    # print(vendor1, prod, prodset.intersection(prodsInPossibleVendor), prodset)
                if prod in vendor1 or vendor1 in prod:
                    out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                    # print(out)

                    # with open('../output/productsPosingAsVendors.xlsx', "a") as of:
                    #     of.write(out + '\n')
                    vendorSubstringMatch_Count += 1

                elif vendor1 in prodsInPossibleVendor:
                    out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                    # print(out)

                    # with open('../output/productsPosingAsVendors.xlsx', "a") as of:
                    #     of.write(out + '\n')
                    vendorInProdasVendor_Count += 1

                elif len(prodset.intersection(prodsInPossibleVendor)) > 1:
                    out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                    print(out)
                    # with open('../output/checkForThese_VendorsWithIntersectingVendors.xlsx', "a") as of:
                    #     of.write(out + '\n')
                    vendorsWithIntersectionProducts_Count += 1
                else:
                    out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                    # print(out)
print("Count of substring matching between vendor 1 (vendor) and vendor 2 (products of vendor): ", vendorSubstringMatch_Count)
print("Count of vendor as product and product as vendor: ", vendorInProdasVendor_Count)
print("Count of vendor with common products: ", vendorsWithIntersectionProducts_Count)

print("------------------- Substring Matching Ends ------------------------")

# vendProds