import pickle

vendor_prod_maxProd = pickle.load(open('./vendor_prod_maxProd.pkl', 'rb'))
print(vendor_prod_maxProd)

fileForPdd = open('../../../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')
cve_pdd = {}
for line in fileForPdd:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    pdd = line[1]
    if cve not in cve_pdd:
        cve_pdd[cve] = pdd

f2 = open('../../../../ConsistentVendor_prod_info-V2.csv', 'rb')
for line in f2:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    vend = line[1]
    consVend = line[2]
    # print(line)
    product = line[3]
    date = line[4]
    pdd = cve_pdd[cve]
    consProd = ""
    if vend in vendor_prod_maxProd:
        prods = vendor_prod_maxProd[vend]
        if product in prods:
            consProd = prods[product]
            # if product != consProd:
            #     print(vend, product, consProd)
    out = str(cve)+";"+str(vend)+";"+str(product)+";"+str(consVend)+";"+str(consProd)+";"+str(pdd)+";"+str(date)
    with open('./cve_vendProd_ConsIncons_pdd_date.csv', 'a')as foo:
        foo.write(out+'\n')