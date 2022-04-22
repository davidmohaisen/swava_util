import os, pickle

descNulls = set(pickle.load(open("./descNulls.pkl", 'rb')))
cvssNulls = set(pickle.load(open("./cvssNulls.pkl", 'rb')))
vendorNulls = set(pickle.load(open("./vendorNulls.pkl", 'rb')))
cweNulls = set(pickle.load(open("./cweNulls.pkl", 'rb')))
rejectedVulns = set(pickle.load(open("./rejectedVulns.pkl", 'rb')))
referenceNulls = set(pickle.load(open("./referenceNulls.pkl", 'rb')))

print(len(descNulls))
print(len(cvssNulls))
print(len(vendorNulls))
print(len(cweNulls))
print(len(rejectedVulns))
print(len(referenceNulls))

print(cweNulls - cvssNulls)
print(len(vendorNulls - cvssNulls))
print(cvssNulls)

print(len(referenceNulls-cvssNulls))
# vendorNulls.pkl
# cvssNulls.pkl
# cweNulls.pkl
# rejectedVulns.pkl
# referenceNulls.pkl

# Check their published date