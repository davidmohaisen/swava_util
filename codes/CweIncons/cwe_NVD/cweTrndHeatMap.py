import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

f = open('./cweTrand.csv', 'rb')
next(f)
heatmapInput = []
cwes = ['CWE-79','CWE-119','CWE-20','CWE-200','CWE-190','CWE-125','CWE-89','CWE-352','CWE-284','CWE-22','CWE-264','CWE-416','CWE-476','CWE-78','CWE-787','CWE-287','CWE-611','CWE-400','CWE-434','CWE-399']
year = [2018,2017,2016,2015,2014,2013,2012,2011,2010]
for line in f:
    line = line.decode().replace('\n', '').rsplit(',')[1:]
    tkn = []
    for i in range(len(line)):
        tkn.append(int(line[i]))
    heatmapInput.append(tkn)
    # print(len(line))

print(heatmapInput)
percentageRepresentation = np.zeros((20,9))
heatmapInput = np.asarray(heatmapInput)
print(heatmapInput)
df = pd.DataFrame(heatmapInput, columns=year,index=cwes)
dfMax = df.max(axis=1)
print(dfMax)
# exit()
df = df.divide(dfMax, axis=0)
df = df.round(2)
print(df)
# exit()

sns.set(font_scale=1)

plt.figure(figsize=(7,6))
ax = sns.heatmap(df,annot=True,cmap="Blues",fmt='g', cbar=False)#
# plt.xlabel('Year', fontsize=12)
# plt.ylabel('CWE-ID', fontsize=12)
plt.savefig("cweTrendV2.pdf")
plt.clf()
plt.close()