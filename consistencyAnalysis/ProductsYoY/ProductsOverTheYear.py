f = open('./cve_vendProd_ConsIncons_pdd_date.csv', 'rb')

pddyear_consven, pddyear_incvend, pddyear_consprod, pddyear_incprod = {}, {}, {}, {}
for line in f:
    line = line.decode().replace('\n', '').rsplit(";")
    cve = line[0]
    incvend = line[1]
    incprod = line[2]
    consvend = line[3]
    consprod = line[4]

    if consvend == "":
        consvend = incvend
    if consprod == "":
        consprod = incprod

    pdd = line[5]
    pddyear = pdd.rsplit("-")[0]

    if pddyear not in pddyear_consven:
        pddyear_consven[pddyear] = set()
        pddyear_consven[pddyear].add(consvend)
    else:
        pddyear_consven[pddyear].add(consvend)

    if pddyear not in pddyear_incvend:
        pddyear_incvend[pddyear] = set()
        pddyear_incvend[pddyear].add(incvend)
    else:
        pddyear_incvend[pddyear].add(incvend)


    if pddyear not in pddyear_consprod:
        pddyear_consprod[pddyear] = set()
        pddyear_consprod[pddyear].add(consvend+":"+consprod)
    else:
        pddyear_consprod[pddyear].add(consvend+":"+consprod)

    if pddyear not in pddyear_incprod:
        pddyear_incprod[pddyear] = set()
        pddyear_incprod[pddyear].add(incvend+":"+incprod)
    else:
        pddyear_incprod[pddyear].add(incvend+":"+incprod)
    # print(line)

print(len(pddyear_incprod), len(pddyear_consprod), len(pddyear_incvend), len(pddyear_consven))

for itm in pddyear_consven:
    out = str(itm)+";"+str(len(pddyear_consven[itm]))+";"+str(len(pddyear_incvend[itm]))+";"+str(len(pddyear_consprod[itm]))+";"+str(len(pddyear_incprod[itm]))
    with open('./pddyear_consIncons_Vend_Prod.csv', 'a') as foo:
        foo.write(out+'\n')
    # print(out)