import re
f = open('../../../vendor_prod_info.csv', 'rb')

vend_prod = {}
vendor_vendorWoTkn = {}
for line in f:
    line = line.decode().replace('\n', '')
    print(line)

    tkn = line.rsplit(";")
    vendor = tkn[1]
    product = tkn[2]
    vendorWoTkn = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', vendor).strip().lower()

    if vendorWoTkn not in vend_prod:
        vend_prod[vendorWoTkn] = set()
        vend_prod[vendorWoTkn].add(product)
    else:
        vend_prod[vendorWoTkn].add(product)

    if vendorWoTkn not in vendor_vendorWoTkn:
        vendor_vendorWoTkn[vendorWoTkn] = set()
        vendor_vendorWoTkn[vendorWoTkn].add(vendor)
    else:
        vendor_vendorWoTkn[vendorWoTkn].add(vendor)


    # print(vendor, prodList)
    # out = vendor+':'+str(prodList).replace('[','').replace(']','').replace("'","")
    # print(out)
    # with open('../output/inconsistencyInput.xlsx', "a") as of:
    #     of.write(out + '\n')
    # vendorProdWithout_ - Space.xlsx
for itm in vend_prod:

    with open('../output2.0/vendorProdWithout_-Space.xlsx', "a") as of:
        of.write(str(itm) +":"+ str(len(vendor_vendorWoTkn[itm])) + ":" + re.sub(r'\}|\{|\ |\'', '', str(vendor_vendorWoTkn[itm])) +":"+ re.sub(r'\}|\{|\ |\'', '', str(vend_prod[itm])) + '\n')

    if len(vendor_vendorWoTkn[itm]) > 1:
        with open('../output2.0/vendor_vendorWoTkn.xlsx', "a") as of:
            of.write(str(itm) + ":" + re.sub(r'\}|\{|\ |\'', '', str(vendor_vendorWoTkn[itm])) + '\n')