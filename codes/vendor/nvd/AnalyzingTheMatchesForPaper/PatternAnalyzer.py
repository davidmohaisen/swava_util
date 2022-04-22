import re
from difflib import SequenceMatcher

substringed = open('../output/Final/vendorSubstringMatching.xlsx', 'rb')
posed = open('../output/Final/productPosingAsVendor.xlsx', 'rb')
posedUnposed = open('../output/vendorAsprod-prodAsvendor.xlsx', 'rb')
newAdditions = open('../output2.0/probableInconsistencies-newAdditions.xlsx', 'rb')
alpossibilities = open('/media/seal06/HDD/Projects/Vulnerabilities/SWAVA2.0/inconsistency/nvd/output2.0/probableInconsistencies.xlsx', 'rb')

universalSet = set()
allPossibilitySet = set()
uniques = set()

ignorableProds = {'client', 'server', 'host', 'directory', 'cms', 'os', 'httpserver', 'ftpserver', 'ecommerce', 'antivirus', 'forum', 'news', 'emailserver', 'php', 'linux', 'tftpserver', 'gui', 'contactus', 'webhelpdesk', 'webcalendar', 'webgui', 'admin', 'webadmin', 'mobile', 'whois', 'blogcms', 'downloadmanager', 'expressionengine', 'backupmanager', 'links', 'postfix', 'phpnews', 'minibill', 'calendarscript', 'gallery', 'siteman', 'phplinks', 'web', 'rubyonrails', 'easyscript'}

for line in alpossibilities:
    line = line.decode().replace('\n', '')

    v1 = line.rsplit(":")[0]
    v2 = line.rsplit(":")[1]
    if str(v1) + ":" + str(v2) not in allPossibilitySet and str(v2) + ":" + str(v1) not in allPossibilitySet:
        allPossibilitySet.add(str(v1) + ":" + str(v2))

    # allPossibilitySet.add(line)

for line in substringed:
    line = line.decode().replace('\n', '')

    v1 = line.rsplit(":")[0]
    v2 = line.rsplit(":")[1]

    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1)
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2)
    if str(v1) + ":" + str(v2) in allPossibilitySet or str(v2) + ":" + str(v1) in allPossibilitySet:
        if str(v1) + ":" + str(v2) not in universalSet and str(v2) + ":" + str(v1) not in universalSet:
            universalSet.add(str(v1) + ":" + str(v2))

for line in posed:
    line = line.decode().replace('\n', '')

    v1 = line.rsplit(":")[0]
    v2 = line.rsplit(":")[1]
    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1)
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2)
    if str(v1) + ":" + str(v2) in allPossibilitySet or str(v2) + ":" + str(v1) in allPossibilitySet:
        if str(v1) + ":" + str(v2) not in universalSet and str(v2) + ":" + str(v1) not in universalSet:
            universalSet.add(str(v1) + ":" + str(v2))

for line in posedUnposed:
    line = line.decode().replace('\n', '')
    v1 = line.rsplit(":")[0]
    v2 = line.rsplit(":")[1]
    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1)
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2)
    if str(v1) + ":" + str(v2) in allPossibilitySet or str(v2) + ":" + str(v1) in allPossibilitySet:
        if str(v1) + ":" + str(v2) not in universalSet and str(v2) + ":" + str(v1) not in universalSet:
            universalSet.add(str(v1) + ":" + str(v2))

for line in newAdditions:
    line = line.decode().replace('\n', '')
    v1 = line.rsplit(":")[0]
    v2 = line.rsplit(":")[1]
    v1 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v1)
    v2 = re.sub(r'\_|\-|\(|\)|\.|\ |\\|\/|\'|\"|\!|\#|\$|\%|\^|\&|\*|\+|\=|\{|\}|\[|\]|\;|\:|\<|\>|\,|\.|\?', '', v2)
    if str(v1) + ":" + str(v2) in allPossibilitySet or str(v2) + ":" + str(v1) in allPossibilitySet:
        if str(v1) + ":" + str(v2) not in universalSet and str(v2) + ":" + str(v1) not in universalSet:
            universalSet.add(str(v1) + ":" + str(v2))


files = {'./partwiseData/gt3_IS_eq0.txt', './partwiseData/gt3_IS_eq1.txt', './partwiseData/gt3_IS_gt1.txt', './partwiseData/gt3_vendor_prod_vendor.txt', './partwiseData/gt3_vendor_xyz.txt', './partwiseData/lt3_IS_eq0.txt', './partwiseData/lt3_IS_eq1.txt', './partwiseData/lt3_IS_gt1.txt', './partwiseData/lt3_vendor_prod_vendor.txt', './partwiseData/lt3_vendor_xyz.txt'}
for file in files:
    fo = open(file, 'rb')
    fileName = file.rsplit('/')[-1].rsplit('.')[0]
    uniques = set()
    x1vends = set()
    x2vends = set()
    x1, x2 = 0,0
    for line in fo:
        line = line.decode().replace('\n', '')
        # print(line)
        v1 = line.rsplit(':')[0]
        v2 = line.rsplit(':')[1]
        x1 += 1
        x1vends.add(v1)
        x1vends.add(v2)
        if str(v1) + ":" + str(v2) not in universalSet and str(v2) + ":" + str(v1) not in universalSet:
            x2 += 1
            x2vends.add(v1)
            x2vends.add(v2)

    print(fileName, x1, x2)
    print("vends", len(x1vends), len(x2vends))
# for itm in universalSet:
#     print(itm)
#
#     tkn = itm.rsplit(":")
#
#     if len(tkn) != 5:
#         # print(itm)
#         continue
# # exit()
#     vendor1 = tkn[0]
#     vendor2 = tkn[1]