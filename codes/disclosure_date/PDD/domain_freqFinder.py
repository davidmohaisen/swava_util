f = open('../../cve_url_dt.csv', 'rb')

domain_freq = {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    url = line[1]
    domain = ".".join(url.rsplit("/")[2].rsplit(".")[-2:])
    # print(url, domain)

    if domain in domain_freq:
        domain_freq[domain].add(cve)
    else:
        domain_freq[domain] = set()
        domain_freq[domain].add(cve)

for itm in domain_freq:
    print(itm, len(domain_freq[itm]))
    out = str(itm)+":"+str(len(domain_freq[itm]))
    with open('./domain_freq.csv', 'a') as foo:
        foo.write(out+"\n")