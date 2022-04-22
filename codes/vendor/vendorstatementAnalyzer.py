from xml.dom import minidom
import xml.etree.ElementTree as ET


f = open('./vendorstatements.xml', 'rb')
f1 = open('./vendorstatements.xml', 'rb').read().decode()
print(type(f), type(f1))

# # tree = ET.parse(f)
# # root = tree.getroot()
# root = ET.fromstring(f)
#
# # print(root.iter("statement"))
# for t in root.iter("statement"):
#     print(t.attrib)
# # for neighbor in tree.iter("statement"):
# #     print(neighbor.attrib)
#
# # print(root.tag)
# # # print(tree.findall('statement'))
# # print(root.findall('./statement'))
# # print(root.children)
# # for form in root.findall("./statement"):
# #     x = (form.attrib)
# #     print(x)
# #     z = list(x)
# #     print(z)


xmldoc = minidom.parse(f)
statements = xmldoc.getElementsByTagName('statement')

# print(statements)
# for statement in statements:
#     print(statement.attributes)

root1 = ET.XML(f1)

for sub in root1:
    print(sub.attrib, sub.text)
    # print(sub.text, sub.tag)
    # b=(sub.attrib.get('statement'))
    # print(b)