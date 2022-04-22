import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# import scikits.statsmodels as sm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import scipy
#
def plotLineGraph(data, labe):
    fig = plt.figure(figsize=(8,4))
    # labels = np.arange(len(data["labels"]))

    # sns.set()
    plt.plot(data["labels"], data["low"], linewidth=1.5, color = 'gray', label="Low", linestyle=":")            #marker='o',
    plt.plot(data["labels"], data["medium"], linewidth=1.5, color = 'k', label="Medium", linestyle="--")        #marker='^',
    plt.plot(data["labels"], data["high"], linewidth=1.5, color = 'b', label="High", linestyle="-.")              #marker='D',
    plt.plot(data["labels"], data["total"], linewidth=1.5, color = 'lightseagreen', label="Total", linestyle=('-'))  #marker='X',
    plt.gca().yaxis.grid(True)

    # set the basic properties
    plt.xlabel('Lag days', fontsize=14)
    plt.ylabel('CDF', fontsize=14)
    plt.style.use('fivethirtyeight')
    # plt.xticks(rotation = 35, ha="right")
    plt.legend(loc=7)
    xlab, xtck = [], []
    next = 0
    for j in range(len(labels)):
        if j == next:
            next+=240
            xtck.append(str(labels[j]))
        else:
            xtck.append(" ")


    print(len(data["labels"]), len(xtck))

    plt.xticks(data["labels"], xtck, fontsize=12)#, rotation=90)
    plt.yticks(fontsize=12, rotation = 35)
    # plt.ylim(ymin=0, ymax = 1.005)
    # plt.xlim(xmin=-3, xmax = len(labels)-0.9)

    fig.savefig('./lagtimePlot-V5.pdf', bbox_inches='tight')
    plt.close(fig)





def plot_cdf_xy(y, a):
    y2=y
    y2 = sorted(y, reverse=True)		# For reverse CDF: reverse = true
    # print y
    z = [0] * len(y2)
    z[0] = y2[0]
    z2 = z

    for i in range(1, len(y2)):
        z2[i] = y2[i] + z2[i-1]

    print(a, max(z2))

    for i in range(len(z)):
        # if a == 1:
        z[i] = float(z2[i]) / float(z2[len(z2)-1])
        #     # print("yaha")
        # else:
        #     z[i] = float(z2[i]) / float(59289)
        #     # if z[i] > 1:
        #     #     print(z[i], z2[i])
        #         # print(y)
        #     # print("yaha bhi")

    return z
#
# # labels = ['(-∞, 0]', '(0, 5]', '(5, 10]', '(10, 20]', '(20, 40]', '(40, 80]', '(80, 160]', '(160, 320]', '(320, 640]', '(640, 1280]', '(1280, ∞]']
# # print(labels)
# # labels = ['0', '5', '10', '20', '40', '80', '160', '320', '640', '1280', '']
# # low = [3534, 2292, 774, 485, 423, 536, 447, 325, 197, 120, 27]
# # medium = [24904, 15494, 5158, 3127, 2642, 2627, 2672, 2267, 1132, 720, 135]
# # high = [14262, 13588, 3564, 2156, 1701, 1653, 1669, 1338, 705, 273, 79]
#
# data = [[],[],[],[],[]]
# f = open('./lagTimeByv2ClassAbsoluteNumbers.csv', 'rb')
# next(f)
# for line in f:
#     line = line.decode().replace('\n', '').rsplit(',')
#     # print(line)
#     data[0].append(int(line[0]))
#     data[1].append(int(line[1]))
#     data[2].append(int(line[2]))
#     data[3].append(int(line[3]))
#     data[4].append(int(line[4]))
#
#
# # print(max([max(data[1]), max(data[2]), max(data[3])]))
# # print(max(data[1]))
# # print(max(data[2]))
# # print(max(data[3]))
# # print(max(data[4]))
# # exit()
#
# labels = data[0]
# low = plot_cdf_xy(data[1], 0)
# medium = plot_cdf_xy(data[2], 0)
# high = plot_cdf_xy(data[3], 0)
# total = plot_cdf_xy(data[4], 1)
# # labe = []
# # for i in range(len(labels)):
# #     labe.append(str(labels[i]))
# # print(labels)
# # exit()
# # print(max(low))
# # print(max(medium))
# # print(max(high))
# # print(max(total))
# # exit()
# data = pd.DataFrame({'labels':labels,'low':low,'medium':medium,'high':high,'total':total})
# # data.to_csv('./CDFlagbyv2class-Final', index=False)
# plotLineGraph(data, labels)
#
#
# exit()
cve_v2 = {}
diff_vuln = {}
f = open('./cve_v2_pdd_date_diff.csv', 'rb')
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    diff = line[-1]
    v2 = line[1]
    cve = line[0]
    if diff not in diff_vuln:
        diff_vuln[diff] = set()
        diff_vuln[diff].add(cve)
    else:
        diff_vuln[diff].add(cve)

    if v2 not in cve_v2:
        cve_v2[cve] = v2

data = [[], [], [], [], []]
for diff in diff_vuln:
    cvess = diff_vuln[diff]
    data[0].append(diff)
    lows, mediums, highs = 0, 0, 0
    for cve in cvess:
        v2 = cve_v2[cve]
        # print(v2)
        if v2 == "LOW":
            lows+=1
        if v2 == "MEDIUM":
            mediums+=1
        if v2 == "HIGH": 
            highs+=1
    # print(diff, len(cvess))
    # print(lows, mediums, highs, lows+mediums+highs)
    data[1].append(lows)
    data[2].append(mediums)
    data[3].append(highs)
    data[4].append(lows+mediums+highs)
    # print(line)
# exit()
# total = []
labels = data[0]
low = data[1]
medium = data[2]
high = data[3]
total = data[4]
data = pd.DataFrame({'labels':labels,'low':low,'medium':medium,'high':high,'total':total})
data.to_csv('./lagTimeByv2ClassAbsoluteNumbers-V2.csv', index=False)
print("aaya")
print(max([max(low), max(medium), max(high)]))
exit()
low = plot_cdf_xy(low)
medium = plot_cdf_xy(medium)
high = plot_cdf_xy(high)
total = plot_cdf_xy(total, 1)
print(low)
print(medium)
print(high)
print(total)

data = pd.DataFrame({'labels':labels,'low':low,'medium':medium,'high':high,'total':total})
data.to_csv('./lagTimeByv2ClassCDFWithoutSort-V2.csv', index=False)

# f, (ax) = plt.subplots(1, 1, sharex=True)
# ax2.spines['top'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.xaxis.tick_top()
# ax.tick_params(labeltop=False)
# ax2.xaxis.tick_bottom()


# plt.plot(data["labels"], data["low"], linewidth=2.5, marker='o', color = 'red', label="Low")
# plt.plot(data["labels"], data["medium"], linewidth=2.5, marker='^', color = 'g', label="Medium")
# plt.plot(data["labels"], data["high"], linewidth=2.5, marker='D', color = 'b', label="High")

# ax2.plot(data["labels"], data["low"], linewidth=2.5, marker='o', color = 'red')
# ax2.plot(data["labels"], data["medium"], linewidth=2.5, marker='^', color = 'g')
# ax2.plot(data["labels"], data["high"], linewidth=2.5, marker='D', color = 'b')

# ax.set_ylim(2000, 25500)  # outliers only
# # ax.set_yticks([20000, 22250, 25000])
# ax2.set_ylim(0, 2000)  # most of the data
# # ax2.set_yticks([0, 50, 500, 5000])
