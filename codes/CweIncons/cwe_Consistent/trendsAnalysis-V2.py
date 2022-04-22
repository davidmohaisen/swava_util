import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# f = open('./yearCweVulnCounts_ForTrendAnalysis.csv', 'rb')
f = open('./yearCweVulnCounts_ForTrendAnalysis-Inconsis.csv', 'rb')
# next(f)
heatmapInput = []
cwes = []
year = []
headerCnt = 0
for line in f:
    line = line.decode().replace('\n', '').rsplit(',')#[1:]
    if headerCnt == 0:
        year = line[1:10]
        headerCnt += 1
        continue

    cwe = line[0]
    if "noinfo" in cwe:
        cwe = "CWE-noinf"
    cwes.append(cwe)
    heatmapInput.append(list(map(int, line[1:10])))
    # print(len(line))

print(heatmapInput)
# exit()
percentageRepresentation = np.zeros((20,9))
heatmapInput = np.asarray(heatmapInput)
print(heatmapInput)
# exit()
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
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.savefig("cweTrendCons-V2-Incons.pdf")
plt.clf()
plt.close()