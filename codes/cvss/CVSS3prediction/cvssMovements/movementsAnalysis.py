import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

f = open('./cvssV2_V3_ForMovementsAnalysis.csv', 'rb')
next(f)

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

df = df.convert_objects(convert_numeric=True)
df = df[df[0]==0]
X = df[df.columns[0:10]]
Y = df[df.columns[13]]
print(X)

# # standardize the features
# sc = StandardScaler()
# X_train_std = sc.fit_transform(X)
#
# cov_mat = np.cov(X_train_std.T)
# eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
#
# # calculate cumulative sum of explained variances
# tot = sum(eigen_vals)
# var_exp = [(i / tot) for i in sorted(eigen_vals, reverse=True)]
# cum_var_exp = np.cumsum(var_exp)
#
# # # plot explained variances
# # plt.bar(range(1,14), var_exp, alpha=0.5,
# #         align='center', label='individual explained variance')
# # plt.step(range(1,14), cum_var_exp, where='mid',
# #          label='cumulative explained variance')
# # plt.ylabel('Explained variance ratio')
# # plt.xlabel('Principal component index')
# # plt.legend(loc='best')
# # plt.show()
#
#
# # Make a list of (eigenvalue, eigenvector) tuples
# eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i]) for i in range(len(eigen_vals))]
#
# # Sort the (eigenvalue, eigenvector) tuples from high to low
# eigen_pairs.sort(key=lambda k: k[0], reverse=True)
#
# w = np.hstack((eigen_pairs[0][1][:, np.newaxis], eigen_pairs[1][1][:, np.newaxis]))
# print('Matrix W:\n', w)
#
# X_train_std[0].dot(w)
#
# X_train_pca = X_train_std.dot(w)
#
# markers = ('s', 'x', 'o', 'v')#, '^')
# colors = ('red', 'blue', 'lightgreen', 'magenta')#, 'gray')
#
# fig = plt.figure()
#
# for l, c, m in zip(np.unique(Y), colors, markers):
#     plt.scatter(X_train_pca[Y == l, 0], X_train_pca[Y == l, 1], c=c, label=l, marker=m)
#
# plt.xlabel('PC 1')
# plt.ylabel('PC 2')
# plt.legend(loc='lower left')
# plt.show()
# # fig.savefig("v2low.pdf", bbox_inches='tight')

# **************************** Using pca from sklearn ************************* #

pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(X)
markers = ('s', 'x', 'o', 'v')
colors = ('red', 'blue', 'lightgreen', 'magenta')
fig = plt.figure()

for l, c, m in zip(np.unique(Y), colors, markers):
    plt.scatter(X_train_pca[Y == l, 0], X_train_pca[Y == l, 1], c=c, label=l, marker=m)

print(np.unique(Y))
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.show()
# fig.savefig("v2low.pdf", bbox_inches='tight')