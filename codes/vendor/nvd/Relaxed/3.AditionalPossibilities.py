substringed = open('../output/Final/vendorSubstringMatching.xlsx', 'rb')
posed = open('../output/Final/productPosingAsVendor.xlsx', 'rb')
posedUnposed = open('../output/vendorAsprod-prodAsvendor.xlsx', 'rb')
vendProds = open('../output/vendorProdWithout_-Space.xlsx', 'rb')

newPossibilities = open('../output2.0/probableInconsistencies.xlsx', 'rb')

alreadyAnalyzed= set()
toAnalyze = set()

for line in substringed:
    line = line.decode().replace('\n', '')
    alreadyAnalyzed.add(line)
    # print(line)
print(len(alreadyAnalyzed))
for line in posed:
    line = line.decode().replace('\n', '')
    alreadyAnalyzed.add(line)
print(len(alreadyAnalyzed))
for line in posedUnposed:
    line = line.decode().replace('\n', '')
    alreadyAnalyzed.add(line)
print(len(alreadyAnalyzed))
for line in vendProds:
    line = line.decode().replace('\n', '')
    alreadyAnalyzed.add(line)
print(len(alreadyAnalyzed))

for line in newPossibilities:
    line = line.decode().replace('\n', '')
    toAnalyze.add(line)

print(len(toAnalyze - alreadyAnalyzed))
step2Set = toAnalyze - alreadyAnalyzed
print(len(step2Set))
for itm in (toAnalyze - alreadyAnalyzed):
    # print(itm)
    ven1 = itm.rsplit(":")[0]
    ven2 = itm.rsplit(":")[1]

    for itm1 in alreadyAnalyzed:
        if ven1+":"+ven2 in itm1 or ven2+":"+ven1 in itm1:
            step2Set.remove(itm)
            break

print(len(step2Set))
print("From Here ***************")
for itm in step2Set:
    print(itm)