import urllib.request
from bs4 import BeautifulSoup
import socket
import time, re
import urllib.error
import ssl
from datetime import datetime
import ssl, re

alreadyAnalyzed = set()
f1 = open('./cweNullsCurrentStatusFromWeb.csv', 'rb')
for l in f1:
    l = l.decode().replace('\n', '').rsplit(';')
    alreadyAnalyzed.add(l[0])


f = open('./cweIdNullsCurrentStatus.csv', 'rb')
for line in f:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    date  =line[1]
    modifiedDate  = line[2]

    if cve in alreadyAnalyzed:
        continue
    elif modifiedDate == "":
        out1 = ";".join(line)+";"
        with open('./cweNullsCurrentStatusFromWeb.csv', 'a') as foo1:
            foo1.write(out1 + '\n')
        continue
    elif modifiedDate < '2018-05-17':
        out1 = ";".join(line)+";"+"Silent Update"
        with open('./cweNullsCurrentStatusFromWeb.csv', 'a') as foo1:
            foo1.write(out1 + '\n')
        continue

    url = 'https://nvd.nist.gov/vuln/detail/'+cve+'#VulnChangeHistorySection'
    req = urllib.request.Request(url, headers={'User-Agent': 'Chrome/77.0.3865.90'})
    context = ssl._create_unverified_context()
    html = urllib.request.urlopen(req, context=context)
    soup = BeautifulSoup(html, "lxml")
    changeHistory = soup.findAll('div', {'class':'vuln-change-history-container'})

    foundin = []
    for i in range(len(changeHistory)):
        if "CWE-" in changeHistory[i].text:
            dates = re.findall(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}', changeHistory[i].text)#[0]
            # print(changeHistory[i].text)
            foundin.append(dates)
            # print(i, date)
    try:
        actualModifiedDate = foundin[len(foundin)-1]
    except:
        if len(foundin) == 0:
            actualModifiedDate = ""
    out = cve+";"+date+";"+modifiedDate+";"+re.sub(r'\[|\]|\'', '', str(actualModifiedDate)).replace(', ', ',')
    with open('./cweNullsCurrentStatusFromWeb.csv', 'a') as foo:
        foo.write(out+'\n')
    print(out)