import json, re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# vendorInconsistentChainsFromNVD = open('../nvd/output2.0/vendorChains-Final.xlsx', 'rb')
vendorInconsistentChainsFromNVD_Relaxed = open('./RelaxedvendorChains-Final.xlsx', 'rb')

vendProd1 = {}
inconsisVendors = {}
for line1 in vendorInconsistentChainsFromNVD_Relaxed:
    line1 = line1.decode().replace('\n', '')
    line1Json = json.loads(line1)
    inconsisVendors = line1Json
print("Inconssitent Vendors: ", inconsisVendors)

print("------------------------------ security Tracker results ------------------------")
file = open('./securityTrackerVendors.txt', 'rb').read().decode()
text = file.rsplit('\n')

vendorList = []
start, end = 0, 0
for i in range(len(text)):
    string = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', text[i]).strip().lower()
    # print(string, text[i])

    vendorList.append(string)
    if string in vendProd1:
        vendProd1[string].append(text[i])
    else:
        vendProd1[string] = []
        vendProd1[string].append(text[i])

x= json.dumps(vendProd1)
with open('./output/SecurityTrackerVendors.json', 'w') as f0:
    f0.write(x+'\n')
dbProductCount = 0
for itm in vendProd1:
    if len(vendProd1[itm]) > 1:
        dbProductCount +=len( vendProd1[itm])
        # print(itm, vendProd1[itm])

print("The database has ", dbProductCount, "repetitions corresponding to ", len(vendProd1), " vendors.")
print(vendProd1)
print("---------------------------------")
c=0
presenceCount = {}
inconsistencyCounter = {}
totalCount = 0
for itm in inconsisVendors:
    for i in range(len(inconsisVendors[itm])):
        Wotkns = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', inconsisVendors[itm][i]).strip().lower()
        if Wotkns in vendProd1:
            # print(inconsisVendors[itm][i], inconsisVendors[itm])
            if itm not in presenceCount:
                presenceCount[itm] = set()
                presenceCount[itm].add(inconsisVendors[itm][i])
            else:
                presenceCount[itm].add(inconsisVendors[itm][i])
                # print(itm, inconsisVendors[itm][i], inconsisVendors[itm], presenceCount[itm])
                # c+=1
            if len(presenceCount[itm]) > 1:
                if itm not in inconsistencyCounter:
                    inconsistencyCounter[itm] = 2
                    totalCount += 2
                else:
                    inconsistencyCounter[itm] += 1
                    totalCount += 1

print("------- Consistent dataset is stored in dictionary 'presenceCount' ---------")
print(presenceCount)
print(inconsistencyCounter)
print(totalCount)
# exit()
print("------------- Quantifying vendor inconsistency --------------")
vendorinconsistencyCount = 0
replacableVendorCount = 0
onlyRedundantVendors = []
for itmi in vendProd1:
    if len(vendProd1[itmi]) > 1:
        if itmi not in inconsistencyCounter:
            inconsistencyCounter[itmi] = len(vendProd1[itmi])
        else:
            inconsistencyCounter[itmi] = inconsistencyCounter[itmi] + len(vendProd1[itmi])

for itm in inconsistencyCounter:
    vendorinconsistencyCount += inconsistencyCounter[itm]
    # # print(itmi, presenceCount[itmi])
    # replacableVendorCount+=1
    # onlyRedundantVendors.append(itm)

print("Number of vendors impacted by the inconsistency is: ", vendorinconsistencyCount, ". The ", vendorinconsistencyCount, "inconsistent vendors can be replaced by ", len(inconsistencyCounter), "vendors")
print(vendorinconsistencyCount, replacableVendorCount)

print("------------- Vendor inconsistency quantification Done! --------------")
