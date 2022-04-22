import json, re
posed = open('../productPosingAsVendor.xlsx', 'rb')
substringed = open('../output/Final/vendorSubstringMatching.xlsx', 'rb')
posedUnposed = open('../output/vendorAsprod-prodAsvendor.xlsx', 'rb')
newAdditions = open('../output2.0/probableInconsistencies-newAdditions.xlsx', 'rb')
venChain = open('../output2.0/vendorChains-Final.xlsx', 'rb')
# looseVenChain = open('../Relaxed/outputRel/vendorChains-Final.json', 'rb')


c, d, prodAsVendorCount = 0, 0, 0
prodAsVendorAffectedVendors = set()

noIntersection = set()
intersectionbw1and4 = set()
morethan4match = set()

searchInThese = []
# skipThese = ['vba32', 'fourtwosevenbb', 'onlinefantasyfootballleague']
for line in posed:
    line = line.decode().replace('\n', '')
    # c+=1
    if c >= 180:
        break
        morethan4match.add(line.rsplit(":")[0])
        morethan4match.add(line.rsplit(":")[1])
    else:
        if line not in searchInThese:
            searchInThese.append(line)

    tknx = line.rsplit(':')[-1]
    if len(tknx.rsplit(',')) > 1:
        print(tknx)
        c+=1
print(c)
exit()
        # print(line)

for i in range(len(searchInThese)):
    vendorLine = searchInThese[i]
    tkn = vendorLine.rsplit(':')
    # print(tkn)
    #vendor as product
    if tkn[1] in tkn[2].rsplit(',') or tkn[0] in tkn[3].rsplit(','):
        # print(tkn)
        prodAsVendorAffectedVendors.add(tkn[0])
        prodAsVendorAffectedVendors.add(tkn[1])
        prodAsVendorCount+=1
    # else:
    #     # only two are here
    #     print(tkn)
    d+=1

print(c, d, prodAsVendorCount)
print("-------- Vendors impacted by products posing as vendors: ", len(prodAsVendorAffectedVendors))

for ln in venChain:
    ln = ln.decode().replace('\n', '')
    venChain = json.loads(ln)
    # print(venChain)

print(venChain)
n2, n=0, 0
for itm in venChain:
    n+=len(venChain[itm])

print(n)

for itm in prodAsVendorAffectedVendors:
    if itm in venChain:
        n2+=len(venChain[itm])
print(n2)

n3 = 0
for itm in morethan4match:
    if itm in venChain:
        # print(itm, venChain[itm])
        n3+=len(venChain[itm])

print(n3)
print(morethan4match)
print(len(morethan4match))

# tokenizer finding

toknzdvendsinChain = {}
for itm in venChain:
    print(itm, len(venChain[itm]))
    for itm1 in range(len(venChain[itm])):
        # print(venChain[itm], venChain[itm][itm1])
        venx = re.sub(r'\_|\-|\.', '', venChain[itm][itm1]).strip().lower()
        if venx in toknzdvendsinChain:
            toknzdvendsinChain[venx].append(venChain[itm][itm1])
        else:
            toknzdvendsinChain[venx] = []
            toknzdvendsinChain[venx].append(venChain[itm][itm1])

print(toknzdvendsinChain)
n4 = 0
for itm in toknzdvendsinChain:
    if len(toknzdvendsinChain[itm]) <= 1:
        continue
    n4+=len(toknzdvendsinChain[itm])

print(n4)
print(len(toknzdvendsinChain))

# for line in looseVenChain:
#     looseVenChain = json.loads(line.decode().replace('\n', ''))
# # for itm in looseVenChain:
# #     print(itm, len(looseVenChain[itm]))