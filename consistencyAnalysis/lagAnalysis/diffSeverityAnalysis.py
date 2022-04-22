import pickle
# f = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

v2 = open('../severityByYear/cve2018s_v2_pdd_date_diff_v3_predV3-V2.csv', 'r')

lag_severity = {}
severity_lag = {}
severity_count = {}
for line in v2:
    line = line.replace('\n', '').rsplit(';')
    # print(line)
    cve = line[0]
    v2 = line[1]
    lag = int(line[4])
    if lag == 0:
        continue
    v3 = line[-2]
    if v3 == "":
        v3 = line[-1]
        # print(v3)
    if lag not in lag_severity:
        lag_severity[lag] = {}
        if v3 not in lag_severity[lag]:
            lag_severity[lag][v3] = 1
        else:
            lag_severity[lag][v3] += 1
    else:
        if v3 not in lag_severity[lag]:
            lag_severity[lag][v3] = 1
        else:
            lag_severity[lag][v3] += 1

    if v3 not in severity_lag:
        severity_lag[v3] = lag
    else:
        severity_lag[v3]+=lag

    if v3 not in severity_count:
        severity_count[v3] = 1
    else:
        severity_count[v3]+=1




# with open('lag_severity.pickle', 'wb') as handle:
#     pickle.dump(lag_severity, handle, protocol=pickle.HIGHEST_PROTOCOL)
# out = str(cve)+';'+str(v2)+";"+str(pdd)+";"+str(date)+";"+str(diff)+';'+str(v3)+';'+str(predV3)

for itm in lag_severity:
    print(itm, lag_severity[itm])

for itm in severity_count:
    print(itm, severity_count[itm], severity_lag[itm], float(severity_lag[itm]/severity_count[itm]))

