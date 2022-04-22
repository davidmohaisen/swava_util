from bs4 import BeautifulSoup
# import openpyxl
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.securitytracker.com/topics/topics.html#vendor'
html = urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text().rsplit('\n')
print(text)
# print("Vendors as extracted from SecurityTracker: ", text)
# print("Vendor Count as extracted from SecurityFocus: ", len(text))
#
# vendorList = []
# start, end = 0, 0
# for i in range(len(text)):
#     string = text[i].strip()
#     if string == "":
#         continue
#
#     if string == "Select Vendor" and start == 0:
#         start = 1
#         continue
#
#     if string == "Title:":
#         end = 1
#         continue
#
#     if start == 1 and end == 0:
#         vendorList.append(string)
#
# print("----------------- SecurityFocus vendors acquired ----------------------")
# print(vendorList)
# print(len(vendorList))
