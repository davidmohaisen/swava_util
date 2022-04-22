import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import linregress
import matplotlib.pyplot as plt

f = open('./VendorProdCveCountAvg.csv', "rb")

cves, vulnPerProd, prods = [], [], []
for line in f:
    line = line.decode().replace('\n','')
    # print(line)

    tkn = line.rsplit(',')
    cveCnt = tkn[1]
    cves.append(cveCnt)
    prodCnt = tkn[2]
    prods.append(prodCnt)
    avg = tkn[3]
    vulnPerProd.append(avg)


print(len(cves), len(vulnPerProd))

# df = pd.DataFrame(cves, vulnPerProd)
cves = np.array(cves).astype(np.float)
vulnPerProd = np.array(vulnPerProd).astype(np.float)
prods = np.array(prods).astype(np.float)

print(cves)
print(vulnPerProd)

# linregress(cves, vulnPerProd)


# pearson_coef, p_value = stats.pearsonr(cves, vulnPerProd)
# print("Pearson Correlation Coefficient: ", pearson_coef, "and a P-value of:", p_value) # Results
#
#
# cves = np.array(cves)
# vulnPerProd = np.array(vulnPerProd)
print(np.corrcoef(cves, vulnPerProd)[0, 1])
plt.plot(vulnPerProd, cves)
plt.show()