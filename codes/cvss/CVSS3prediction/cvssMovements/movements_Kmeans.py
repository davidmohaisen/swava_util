import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import colors as mcolors
import math
from mpl_toolkits.mplot3d import Axes3D

f = open('./cvssV2_V3_ForMovementsAnalysis.csv', 'rb')
# next(f)

LoL = []
for line in f:
    line = line.decode().replace('\n', '')
    # line = line.replace('LOW', '0').replace('MEDIUM', '1').replace('HIGH', '2').replace('CRITICAL', '3').replace(";N;", ';0;').replace(";L;", ';1;').replace(";P;", ';2;').replace(";A;", ';3;').replace(";1;", ';1;')
    tkn = line.rsplit(';')[1:15]

    # featureList = tkn[]
    # print(tkn)
    LoL.append(tkn)
    # print(line)
    # exit()

print(LoL)
df = pd.DataFrame(LoL)
df[0] = df[0].replace({"LOW": 0, "MEDIUM": 1, "HIGH": 2})
df[4] = df[4].replace({"N": 0, "L": 1, "A": 2})
df[5] = df[5].replace({"L": 0, "M": 1, "H": 2})
df[6] = df[6].replace({"N": 0, "S": 1, "M": 2})
df[7] = df[7].replace({"N": 0, "P": 1, "C": 2})
df[8] = df[8].replace({"N": 0, "P": 1, "C": 2})
df[9] = df[9].replace({"N": 0, "P": 1, "C": 2})
df[10] = df[10].replace({"False": 0, "True": 1})
df[11] = df[11].replace({"False": 0, "True": 1})
df[12] = df[12].replace({"False": 0, "True": 1})
df[13] = df[13].replace({"LOW": 0, "MEDIUM": 1, "HIGH": 2, "CRITICAL": 3})
#
df = df.convert_objects(convert_numeric=True)
df = df[df[0]==0]
X = df.iloc[:, 0:-1]
Y = df.iloc[:, 13]
# X = df[df.columns[0:10]]
# Y = df[df.columns[11]]
print(Y.shape, X.shape)
#
clusterCount = len(np.unique(Y))
rowCnt, colCnt = df.shape

kmeans = KMeans(n_clusters=clusterCount)#, init='k-means++')#, max_iter=rowCnt, n_init=10, random_state=0)
pred_y = kmeans.fit(X)

labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

print(centroids)
print(kmeans.labels_)
print(kmeans.inertia_)
# print(range(0,14))

# plt.scatter(range(rowCnt), range(rowCnt), c=kmeans.labels_.astype(float), s=50, alpha=0.5)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
#
# plt.show()


pca = PCA(n_components=3)
pca_data = pca.fit_transform(X)

colors = list(zip(*sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name) for name, color in dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS).items())))[1]

# number of steps to taken generate n(clusters) colors
skips = math.floor(len(colors[5: -5]) / clusterCount)
cluster_colors = colors[5: -5: skips]

# Plotting begins

print(colors)
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(pca_data[0], pca_data[1], pca_data[2], c = list(map(lambda label: colors, kmeans.labels_)))

str_labels = list(map(lambda label:'% s' % label, kmeans.labels_))

list(map(lambda data1, data2, data3, str_label: ax.text(data1, data2, data3, s = str_label, size = 16.5, zorder = 20, color = 'k'), pca_data[0], pca_data[1], pca_data[2], str_labels))

plt.show()