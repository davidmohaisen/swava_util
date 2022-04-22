import re
from difflib import SequenceMatcher

f = open('../output2.0/vendorProdWithout_-Space.xlsx', 'rb')

vendorList = []
vendorReplica = {}
vendorProds = {}
for line in f:
    line = line.decode().replace('\n', '')
    tkn = line.rsplit(':')

    vendor = tkn[0]
    replicaCount = tkn[1]
    prods = tkn[3]
    if vendor not in vendorReplica:
        vendorReplica[vendor] = replicaCount
    else:
        vendorReplica[vendor] = vendorReplica[vendor] + replicaCount

    if vendor not in vendorProds:
        vendorProds[vendor] = prods
    else:
        vendorProds[vendor] = vendorProds[vendor] + ", " + prods


vendorSet = set(vendorReplica.keys())
c=0

ignorableProds = {'client', 'server', 'host', 'directory', 'cms', 'os', 'httpserver', 'ftpserver', 'ecommerce', 'antivirus', 'forum', 'news', 'emailserver', 'php', 'linux', 'tftpserver', 'gui', 'contactus', 'webhelpdesk', 'webcalendar', 'webgui', 'admin', 'webadmin', 'mobile', 'whois', 'blogcms', 'downloadmanager', 'expressionengine', 'backupmanager', 'links', 'postfix', 'phpnews', 'minibill', 'calendarscript', 'gallery', 'siteman', 'phplinks', 'web', 'rubyonrails', 'easyscript'}
for vendor1 in vendorSet:
    vendorNotToBeChecked = set()
    vendorNotToBeChecked.add(vendor1)
    checkin = vendorSet - vendorNotToBeChecked
    prodset = vendorProds[vendor1]
    prodset = re.sub(r'\_|\-|\ ', '', prodset).rsplit(',')
    prodset = set(prodset)
    for prod in prodset:
        if prod in ignorableProds or vendor1 in ignorableProds:
            continue
        if prod in checkin:# and prod not in ignorableProds:
            match = SequenceMatcher(None, vendor1, prod).find_longest_match(0, len(vendor1), 0, len(prod))
            matchedstring = vendor1[match.a: match.a + match.size]
            # if len(matchedstring) < 3:
            #     continue
            prodsInPossibleVendor = set(re.sub(r'\_|\-|\ ', '', vendorProds[prod]).rsplit(','))
            # if vendor1 in prodsInPossibleVendor:
            # if prod in prodsInPossibleVendor:

                #
            if prod in vendor1 or vendor1 in prod:
                # print(vendor1, prod, prodset.intersection(prodsInPossibleVendor), prodset)

                out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                c+=1
                print(out)
                # # with open('../output/possibleconflictingvendornamesProdinVendorAndVendorinProd.xlsx', "a") as of:
                # #     of.write(out + '\n')


            elif vendor1 in prodsInPossibleVendor:      # vendor1 -> (p1, p2, p3) Now, vendor p1 and product named "vendor1"
                # print(vendor1, prod, prodset.intersection(prodsInPossibleVendor), prodset)
                out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                c+=1
                print(out)
                # # with open('../output/possibleconflictingvendornamesProdinVendorAndVendorinProd.xlsx', "a") as of:
                # #     of.write(out + '\n')

            elif prodset.intersection(prodsInPossibleVendor):
                # print(vendor1, prod, prodset.intersection(prodsInPossibleVendor), prodset)

                if len(prodset.intersection(prodsInPossibleVendor)) > 1:
                    out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                    c+=1
                    print(out)
                    # # with open('../output/possibleconflictingvendornamesProdinVendorAndVendorinProd.xlsx', "a") as of:
                    # #     of.write(out + '\n')

                elif len(prodset.intersection(prodsInPossibleVendor)) == 1:
                    if list(prodset.intersection(prodsInPossibleVendor))[0] in str(ignorableProds):
                        continue
                    elif vendor1 == re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) or prod == re.sub(r"\'|\ |\{|\}", '', str(prodset)) or re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset))) == re.sub(r"\'|\ |\{|\}", '', str(prodset)) or re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset))) == re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) or re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset))) == vendor1 or re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset))) == prod:
                        out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                        print(out)
                        c += 1
                        # with open('../output/possibleconflictingvendornamesProdinVendorAndVendorinProd.xlsx', "a") as of:
                        #     of.write(out + '\n')
                        #
                    else:
                        out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                        print(out)
                        c+=1
            elif prod not in prodsInPossibleVendor:
                out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                print(out)
                c += 1
                # continue
            # elif prod not in prodsInPossibleVendor:
            #     # print(vendor1, prod, prodset.intersection(prodsInPossibleVendor), prodset)
            #     out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
            #
            #     # print(out)
            #     # # with open('../output/possibleconflictingvendornamesProdinVendorAndVendorinProd.xlsx', "a") as of:
            #     # #     of.write(out + '\n')
            #     # c+=1
            else:
                out = str(prod) + ":" + str(vendor1) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodset)) + ":" + re.sub(r"\'|\ |\{|\}", '', str(prodsInPossibleVendor.intersection(prodset)))
                print(out)
                c+=1
print(c)
