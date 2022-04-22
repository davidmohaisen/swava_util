import pickle
f = open('./699.csv', 'rb')
f1 = open('./1000.csv', 'rb')
f2 = open('./1008.csv', 'rb')
next(f)
next(f1)
next(f2)
name_id={}
AhmedTaughtMe = []
a, b, c = 0,0,0
cweadded = set()
for line in f:
    line = line.decode().replace("\n", '').rsplit(',')
    print(line)
    # exit()

    cwe_id = line[0]
    name = line[1]
    cweDesc = line[4]
    if cweDesc == "":
        cweDesc = line[5]
        a+=1
    if cweDesc == "":
        cweDesc = line[1]
        b+=1
    if cweDesc == "":
        c+=1
    cweadded.add(cwe_id)
    AhmedTaughtMe.append(["CWE-"+str(cwe_id), name, str(cweDesc)])
    related=line[6]
    if cwe_id == "109":
        print(line[6])
    if name not in name_id:
        name_id[name] = []
        name_id[name].append(cwe_id)
    else:
        if cwe_id not in name_id[name]:
            name_id[name].append(cwe_id)
        # print(cwe_id, name, related)
        # print(name_id[name])
        # exit()
    # exit()
# with open('./CWEDb.pkl', 'wb') as foot:
#     pickle.dump(AhmedTaughtMe, foot)
for line in f1:
    line = line.decode().replace("\n", '').rsplit(',')
    print(line)
    # exit()

    cwe_id = line[0]
    name = line[1]
    cweDesc = line[4]
    if cweDesc == "":
        cweDesc = line[5]
        a+=1
    if cweDesc == "":
        cweDesc = line[1]
        b+=1
    if cweDesc == "":
        c+=1
    if cwe_id not in cweadded:
        cweadded.add(cwe_id)
        AhmedTaughtMe.append(["CWE-"+str(cwe_id), name, str(cweDesc)])

for line in f2:
    line = line.decode().replace("\n", '').rsplit(',')
    print(line)
    # exit()

    cwe_id = line[0]
    name = line[1]
    cweDesc = line[4]
    if cweDesc == "":
        cweDesc = line[5]
        a+=1
    if cweDesc == "":
        cweDesc = line[1]
        b+=1
    if cweDesc == "":
        c+=1
    if cwe_id not in cweadded:
        cweadded.add(cwe_id)
        AhmedTaughtMe.append(["CWE-"+str(cwe_id), name, str(cweDesc)])

AhmedTaughtMe.append(['CWE-19', "Data Processing Errors", "Weaknesses in this category are typically found in functionality that processes data."])
AhmedTaughtMe.append(['CWE-371', "State Issues", "Weaknesses in this category are related to improper management of system state."])
AhmedTaughtMe.append(['CWE-388', "7PK - Errors", "This category represents one of the phyla in the Seven Pernicious Kingdoms vulnerability classification. It includes weaknesses that occur when an application does not properly handle errors that occur during processing."])
AhmedTaughtMe.append(['CWE-320', "Key Management Errors", "Weaknesses in this category are related to errors in the management of cryptographic keys."])
AhmedTaughtMe.append(['CWE-417', "Channel and Path Errors", "Weaknesses in this category are related to improper handling of communication channels and access paths."])
AhmedTaughtMe.append(['CWE-361', "7PK - Time and State", "This category represents one of the phyla in the Seven Pernicious Kingdoms vulnerability classification. It includes weaknesses related to the improper management of time and state in an environment that supports simultaneous or near-simultaneous computation by multiple systems, processes, or threads."])
AhmedTaughtMe.append(['CWE-199', "Information Management Errors", "Weaknesses in this category are related to improper handling of sensitive information."])
AhmedTaughtMe.append(['CWE-21', "Pathname Traversal and Equivalence Errors", "Weaknesses in this category can be used to access files outside of a restricted directory (path traversal) or to perform operations on files that would otherwise be restricted (path equivalence). Files, directories, and folders are so central to information technology that many different weaknesses and variants have been discovered. The manipulations generally involve special characters or sequences in pathnames, or the use of alternate references or channels."])
AhmedTaughtMe.append(['CWE-310', "Cryptographic Issues", "Weaknesses in this category are related to the use of cryptography."])
AhmedTaughtMe.append(['CWE-485', "7PK - Encapsulation", "This category represents one of the phyla in the Seven Pernicious Kingdoms vulnerability classification. It includes weaknesses that occur when the product does not sufficiently encapsulate critical data or functionality."])
AhmedTaughtMe.append(['CWE-275', "Permission Issues", "Weaknesses in this category are related to improper assignment or handling of permissions."])
AhmedTaughtMe.append(['CWE-398', "7PK - Code Quality", "This category represents one of the phyla in the Seven Pernicious Kingdoms vulnerability classification. It includes weaknesses that do not directly introduce a weakness or vulnerability, but indicate that the product has not been carefully developed or maintained."])
AhmedTaughtMe.append(['CWE-16', "Configuration", "Weaknesses in this category are typically introduced during the configuration of the software."])
AhmedTaughtMe.append(['CWE-399', "Resource Management Errors", "Weaknesses in this category are related to improper management of system resources."])
AhmedTaughtMe.append(['CWE-264', "Permissions, Privileges, and Access Controls", "Weaknesses in this category are related to the management of permissions, privileges, and other security features that are used to perform access control."])
AhmedTaughtMe.append(['CWE-254', "7PK - Security Features", "Software security is not security software. Here we're concerned with topics like authentication, access control, confidentiality, cryptography, and privilege management."])
AhmedTaughtMe.append(['CWE-189', "Numeric Errors", "Weaknesses in this category are related to improper calculation or conversion of numbers."])
AhmedTaughtMe.append(['CWE-255', "Credentials Management", "Weaknesses in this category are related to the management of credentials."])
AhmedTaughtMe.append(["CWE-699", "Development Concepts", "This view organizes weaknesses around concepts that are frequently used or encountered in software development. Accordingly, this view can align closely with the perspectives of developers, educators, and assessment vendors. It provides a variety of categories that are intended to simplify navigation, browsing, and mapping."])

print(a,b,c)
with open('./CWEDb.pkl', 'wb') as foot:
    pickle.dump(AhmedTaughtMe, foot)
# ['CWE-ID', 'Name', 'Weakness Abstraction', 'Status', 'Description', 'Extended Description', 'Related Weaknesses', 'Weakness Ordinalities', 'Applicable Platforms', 'Background Details', 'Alternate Terms', 'Modes Of Introduction', 'Exploitation Factors', 'Likelihood of Exploit', 'Common Consequences', 'Detection Methods', 'Potential Mitigations', 'Observed Examples', 'Functional Areas', 'Affected Resources', 'Taxonomy Mappings', 'Related Attack Patterns', 'Notes']
