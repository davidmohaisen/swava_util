f = open('../../disclosure_date/Re-PDD/cve_pdd_diff-V2.csv', 'rb')

diff_cve = {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    diff = line[-1]
    if diff not in diff_cve:
        diff_cve[diff] = set()
        diff_cve[diff].add(cve)
    else:
        diff_cve[diff].add(cve)
    # print(line)

for diff in diff_cve:
    out = str(diff)+";"+str(len(diff_cve[diff]))
    with open('./diff_VulnCount-V2.csv', 'a') as foo:
        foo.write(out+'\n')
    print(diff, len(diff_cve[diff]))

# print(diff_cve[-599])