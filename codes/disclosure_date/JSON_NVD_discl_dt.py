# coding=utf-8
import json
from pprint import pprint
import csv
import urllib2
from bs4 import BeautifulSoup
import socket
import time
import ssl
# from BeautifulSoup import BeautifulSoup

socket.setdefaulttimeout(7)

# ind = 0
# cout[][]
# r = 1
def output_array_creater(out,b):
    csv_out = '/Users/afsahanwar/tmp/disclosure_date/pddate/public_distribution_date'+b+'.csv'
    with open(csv_out, "a") as output:

        output.write(out)


        # writer.writerows(cout) 
              

    return;
# def codes_gen:
def create_date(year,mon,day):
    day = day.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    mon = mon.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    year = year.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    # print day,mon,year

    try:
        t = day[2]
        d = day
        day = mon
        mon = d
    except IndexError:
        day = day
        mon = mon

    if day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7" or day == "8" or day == "9":
        day = str(0)+day


    if mon[:3].lower() == "jan":
        mon = "01"
    elif mon[:3].lower() == "feb":
        mon = "02"
    elif mon[:3].lower() == "mar":
        mon = "03"
    elif mon[:3].lower() == "apr":
        mon = "04"
    elif mon[:3].lower() == "may":
        mon = "05"
    elif mon[:3].lower() == "jun":
        mon = "06"
    elif mon[:3].lower() == "jul":
        mon = "07"
    elif mon[:3].lower() == "aug":
        mon = "08"
    elif mon[:3].lower() == "sep":
        mon = "09"
    elif mon[:3].lower() == "oct":
        mon = "10"
    elif mon[:3].lower() == "nov":
        mon = "11"
    elif mon[:3].lower() == "dec":
        mon = "12"

    date = str(year)+"-"+str(mon)+"-"+str(day)
    if date == "--":
        return ""
    else:
        return date

def hpe_date(url1):
    response = ''
    html = ''
    print(url1)
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # print tokens[i]
            if tokens[i] == "Release Date:":
                a = tokens[i+1]
                try:
                    day = a.split('-')[2]
                    return a
                except IndexError:
                    return url

# def hp_date(url1):
#     response = ''
# html = ''
# #     try:
# #         response = urllib2.urlopen(url1)
# html = response.read()
# response.close()
# #     except urllib2.HTTPError, ev:
# #         return ""
# #     except urllib2.URLError, uu:
# #         return ""

# #     html = response.read()
# response.close()

#     soup = BeautifulSoup(html, "lxml")
#     a = ''
#     for script in soup(["script", "style"]):
#         script.extract()

#     text = soup.get_text()
#     lines = (line.strip() for line in text.splitlines())
#     chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#     text = '\n'.join(chunk for chunk in chunks if chunk)

#     tokens = text.rsplit('\n')

#     mon, day, year = "","",""

#     if len(tokens) > 1:
#         return url1

def avaya_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i][:22] == "Original Release Date:":
            a = tokens[i]
            try:
                day = a.split(' ')[4]
                mon = a.split(' ')[3]
                year = a.split(' ')[5]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                try:
                    a = tokens[i+1]
                    day = a.split(' ')[1]
                    mon = a.split(' ')[0]
                    year = a.split(' ')[2]
                    date = create_date(year,mon,day)
                    return date
                except IndexError:
                    return ""

def vm_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i] == "Issue date:":
            a = tokens[i+1]
            try:
                day = a.split('-')[2]
                return a
            except IndexError:
                a = tokens[i+2]
                try:
                    day = a.split('-')[2]
                    return a
                except IndexError:
                    return ""

def packetstormorg_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i][:6] == "Posted":
            a = tokens[i]
            try:
                day = a.split(' ')[2]
                mon = a.split(' ')[1]
                year = a.split(' ')[3]
            except IndexError:
                a = tokens[i]
                b = tokens[i+1]
                mon = a.split(' ')[1]
                day = b.split(' ')[0]
                year = b.split(' ')[1]
            date = create_date(year,mon,day)
            return date
            break
def wireshark_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i][:6] == "author":
            a = tokens[i+1]
            try:
                day = a.split(' ')[1]
                mon = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Reported:":
            a = tokens[i+1]
            try:
                date = a.split(' ')[0]
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i][:5] == "Date:":
            a = tokens[i]
            try:
                mon = a.split(' ')[1]
                day = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                pass
        elif a=="":
            return ""
def apache_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Created:":
            a = tokens[i+1]
            try:
                mon = a.split(' ')[0].split('/')[1]
                day = a.split(' ')[0].split('/')[0]
                year = a.split(' ')[0].split('/')[2]
                year = int(year)
                if year >90:
                    year = str(19)+str(year)
                elif year <=17:
                    year = str(20)+str(year)
                date = create_date(year,mon,day)
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Date":
            a = tokens[i+1]
            try:
                day = a.split(' ')[1]
                mon = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Main":
            a = tokens[i+2]
            try:
                mon = a.split(' ')[1]
                day = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                pass
        elif a == "":
            if i == 0:
                try:
                    a = tokens[0]
                    year = a.split(' ')[1].split('\t')[1].split('/')[0]
                    mon = a.split(' ')[1].split('\t')[1].split('/')[1]
                    day = a.split(' ')[1].split('\t')[1].split('/')[2]
                    date = create_date(year,mon,day)
                    return date
                except:
                    return ""       #check this again

def android_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i][:9] == "Published":
            try:
                mon = tokens[i].split('|')[0].split(' ')[1]
                day = tokens[i].split('|')[0].split(' ')[2]
                year = tokens[i].split('|')[0].split(' ')[3]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                return ""
def zdi_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Disclosure Timeline":
            try:
                a = tokens[i+2].split(' - ')[0]
                return a
            except IndexError:
                return ""

def drupal_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    if len(tokens) > 1:
        print url1
    return ""
def sun_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""

    if len(tokens) > 1:
        print url1
    return ""
def kernel_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    date_x = []
    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Date:":
            mon = tokens[i+1].split(' ')[1]
            day = tokens[i+1].split(' ')[2]
            year = tokens[i+1].split(' ')[4]
            date = create_date(year,mon,day)
            date_x.append(date)
        elif a == "":   
            try:
                if tokens[i][:6] == "author":
                    a = tokens[i].split('>')[1].split(' ')[0]
                    return a
            except IndexError:
                pass

    index = sorted(date_x, key=lambda d: map(int, d.split('-')))
    if len(index)>=1:
        return index[0]
    else:
        return ""
def sourceforge_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):
        # return tokens[i]
        if a == "":
            try:
                if tokens[i][:5] == "From:":
                    try:
                        a = tokens[i].split(' - ')[1].split(' ')[0]
                        return a
                    except IndexError:
                        pass
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Created:":
            try:
                a = tokens[i+1]
                return a
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Authored by:":
            try:
                a = tokens[i+2]
                return a
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Posted by":
            try:
                a = tokens[i+1]
                return a
            except IndexError:
                pass
def novell_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):
        

        if tokens[i] == "Reported:":
            try:
                a = tokens[i+1][:10]
                return a
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Release:":
            
            try:
                a = tokens[i+1]
                year = a[:4]
                mon = a[4:6]
                day = a[6:10]
            except IndexError:
                pass
        elif a == "" and tokens[i][:12] == "Document ID:":
            try:
                creation_date = tokens[i].split(' ')[2][5:14]
                ya = creation_date.split('-')[2]
                ya = int(ya)
                last_modified = tokens[i].split(' ')[3][5:14]
                yb = last_modified.split('-')[2]
                yb = int(yb)
                if yb - ya <= 2:
                    if ya <= 17:
                        year = str(20)+str(ya)
                    if ya >= 90:
                        year = str(19)+str(ya)
                    mon = creation_date.split('-')[1]
                    day = creation_date.split('-')[0]
                else:
                    return ""
            except IndexError:
                pass
        

def adobe_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i][:13] == "Release date:":
            a = tokens[i]
            try:
                mon = a.split(' ')[2]
                day = a.split(' ')[3]
                year = a.split(' ')[4]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                try:
                    mon = a.split(' ')[1].split(':')[1][1:]
                    day = a.split(' ')[2]
                    year = a.split(' ')[3]
                    date = create_date(year,mon,day)
                    return date
                except IndexError:
                    pass
        elif a == "" and tokens[i][:7] == "Created":
            try:
                a = tokens[i].split('Created')[1]
                mon = a.split(' ')[1]
                day = a.split(' ')[0]
                year = a.split(' ')[2]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                a= tokens[i+1]
                mon = a.split(' ')[0]
                day = a.split(' ')[1]
                year = a.split(' ')[2]
                date = create_date(year,mon,day)
                return date
def packetss_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):

        if tokens[i][:6] == "Posted":
            a = tokens[i]
            try:
                mon = a.split(' ')[1]
                day = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                a = tokens[i]
                b = tokens[i+1]
                try:
                    mon = a.split(' ')[1]
                    day = b.split(' ')[0]
                    year = b.split(' ')[1]
                    date = create_date(year,mon,day)
                    return date
                except IndexError:
                    return ""
def jvnjp_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""    
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):
        if tokens[i][:3].encode('utf-8') == "公表日":
            a = tokens[i].encode('utf-8')[9:]
            mon = a.split('/')[1]
            day = a.split('/')[2]
            year = a.split('/')[0]
            date = create_date(year,mon,day)
            return date
            # return mon,day,year
        elif a == "" and tokens[i][:10] == "Published:":
            a = tokens[i]
            try:
                a = a.split(':')[1].encode("ascii", "replace").split('??')[0]
                mon = a.split('/')[1]
                day = a.split('/')[2]
                year = a.split('/')[0]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                return ""

        elif tokens[i][:3].encode('utf-8') == "公開日":
            try:
                a= tokens[i].encode('utf-8')[12:22]
                mon = a.split('/')[1]
                day = a.split('/')[2]
                year = a.split('/')[0]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                return ""

def blogspot_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):
        if tokens[i].split(' ')[0] == "Monday," or tokens[i].split(' ')[0] == "Tuesday," or tokens[i].split(' ')[0] == "Wednesday," or tokens[i].split(' ')[0] == "Thursday," or tokens[i].split(' ')[0] == "Friday," or tokens[i].split(' ')[0] == "Saturday," or tokens[i].split(' ')[0] == "Sunday,":
            a = tokens[i]
            mon=a.split(' ')[1]
            day=a.split(' ')[2]
            year=a.split(' ')[3]
            date = create_date(year,mon,day)
            return date
        elif a == "":
            try:
                g = tokens[i].split(' ')[2]
                try:
                    g = int(g)
                except:
                    pass
                if isinstance(g, int) == True:
                    if g>=2000 and g<=2017:
                        a = tokens[i]
                        mon=a.split(' ')[0]
                        day=a.split(' ')[1]
                        year=a.split(' ')[2]
                        date = create_date(year,mon,day)
                        return date
            except IndexError:
                return ""
def seclists_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return "a"
    except urllib2.URLError, uu:
        return "u"
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "","",""
    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Disclosure Timeline:":
            a=tokens[i+2]
            try:
                a = a.split(' ')[0]
                mon=a.split('-')[1]
                day=a.split('-')[0]
                year=a.split('-')[2]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                pass

        elif tokens[i][:5] == "Date:" and a == "":
            a = tokens[i]
            try:
                mon=a.split(' ')[3]
                day=a.split(' ')[2]
                year=a.split(' ')[4]
                date = create_date(year,mon,day)
                return date
            except IndexError:
                a = tokens[i+1]
                try:
                    mon=a.split(' ')[1]
                    day=a.split(' ')[0]
                    year=a.split(' ')[2]
                    date = create_date(year,mon,day)
                    return date
                except IndexError:
                    return ""

def cisco_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""        

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        if tokens[i][:5] == "First":
            a=tokens[i+1]
            

    dt = a

    dt = dt.encode("ascii", "replace")
    dt = dt.replace("?", " ")

    mon, day, year = "","",""

    try:
        mon=dt.split(' ')[1]
        day=dt.split(' ')[2]
        year=dt.split(' ')[0]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def mozilla_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Announced":
            a=tokens[i+1]
            try:
                year=a.split(' ')[2]
            except IndexError:
                a = tokens[i+1]+" "+tokens[i+2]
        elif tokens[i] == "Last updated by:" and a is "":
            a = tokens[i+2]


    dt = a

    mon, day, year = "","",""
    try:
        mon=dt.split(' ')[0]
        day=dt.split(' ')[1]
        year=dt.split(' ')[2]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def fedora_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i] == "Fedora Update Notification":
            a=tokens[i+2]
            date = a.split(' ')[0]
            return date
        if tokens[i][:17] == "Previous message:":
            if tokens[i-1] != "- Upstream release.":
                a=tokens[i-1]

    dt = a
    try:
        mon=dt.split(' ')[1]
        day=dt.split(' ')[2]
        year=dt.split(' ')[5]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""


def google_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Reported by":
            a=tokens[i+2]
        elif tokens[i] == "Comments":
            try:
                a=tokens[i-1].split(',')[1].replace("th", "")[1:]
            except IndexError:
                print ""

    dt = a
    mon, day, year = "","",""
    try:
        mon=dt.split(' ')[0]
        day=dt.split(' ')[1]
        year=dt.split(' ')[2]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def github_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        if tokens[i] == "Copy path":
            a=tokens[i+3]
        elif tokens[i] == "Latest commit":
            a=tokens[i+2]
        elif tokens[i].replace("'", "")[:18] == "DisclosureDate => ":
            a=tokens[i].replace("'", "")[18:29]
        elif tokens[i] == "Unified":
            a=tokens[i-1]
        elif tokens[i] == "opened this Issue":
            a=tokens[i+1]

    #     elif tokens[i].replace("-", "").replace(" ", "")[:7] == "Public:":
    #         a=tokens[i+1]

    dt = a
    mon, day, year = "","",""

    try:
        mon=dt.split(' ')[0]
        day=dt.split(' ')[1]
        year=dt.split(' ')[2]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""

def secreason_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        try:
            if tokens[i].replace("-", "").replace(" ", "")[:5] == "Dis.:":
                a=tokens[i].replace("-", "").replace(" ", "").split(':')[1]
            elif tokens[i].replace("-", "").replace(" ", "")[:7] == "Public:":
                a=tokens[i+1]
        except IndexError:
            pass

    dt = a
    mon, day, year = "","",""

    if dt is not "":
        try:
            mon=dt.split('.')[0]
            day=dt.split('.')[1]
            year=dt.split('.')[2]
            date = str(year)+"-"+str(mon)+"-"+str(day)
            return date
        except IndexError:
            pass
    else:
        for i in range(len(tokens)):
            if tokens[i][:20] == "Vendor Notification:":
                a = tokens[i]
                try:
                    mon=a.split(' ')[3]
                    day=a.split(' ')[2]
                    year=a.split(' ')[4]
                except IndexError:
                    pass

    dt = a
    # Release Date:  04/25/2011

    if a is "":
        for i in range(len(tokens)):
            if tokens[i][:13] == "Release Date:":
                a = tokens[i+1]
                if a == "unknown":
                    return ""
                else:
                    try:
                        mon=a.split('/')[0]
                        day=a.split('/')[1]
                        year=a.split('/')[2]
                    # return mon,day,year
                    except IndexError:
                        pass

    if a is "":
        for i in range(len(tokens)):
            if tokens[i][1:15] == "DisclosureDate":
                try:
                    a = tokens[i][21:32]
                    # return a[21:32]
                    mon=a.split(' ')[0]
                    day=a.split(' ')[1]
                    year=a.split(' ')[2]
                except IndexError:
                    pass


    if a is "":
        for i in range(len(tokens)):
            # return tokens[i]
            if tokens[i][:7] == "# Date:":
                a = tokens[i]
                try:
                    mon=a.split(' ')[2]
                    day=a.split(' ')[3]
                    year=a.split(' ')[4]
                except IndexError:
                    try:
                        x = a.split(' ')[2]
                        mon=x.split('/')[1]
                        day=x.split('/')[2]
                        year=x.split('/')[0]
                    except IndexError:
                        pass
                

    if a is "":
        a = ""
        for i in range(len(tokens)):
            # return tokens[i]
            try:
                if tokens[i][:15] == "Date published:":
                    a = tokens[i].replace(" ", "").split(':')[1]
                elif tokens[i][:11] == "Issue date:":
                    a = tokens[i+1].replace(" ", "")
                elif tokens[i][:17] == "Original release:":
                    a = tokens[i].replace(" ", "").split(':')[1]
        
                return a
            except IndexError:
                return ""


    day = day.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    mon = mon.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    year = year.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    # # # return day,mon,year

    if day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7" or day == "8" or day == "9":
        day = str(0)+day
    if mon == "1" or mon == "2" or mon == "3" or mon == "4" or mon == "5" or mon == "6" or mon == "7" or mon == "8" or mon == "9":
        mon = str(0)+mon


    # # # # # # # return day,mon,year

    if mon[:3] == "Jan" or mon[:3] == "SEP":
        mon = "01"
    elif mon[:3] == "Feb" or mon[:3] == "FEB":
        mon = "02"
    elif mon[:3] == "Mar" or mon[:3] == "FEB":
        mon = "03"
    elif mon[:3] == "Apr" or mon[:3] == "APR":
        mon = "04"
    elif mon[:3] == "May" or mon[:3] == "MAY":
        mon = "05"
    elif mon[:3] == "Jun" or mon[:3] == "JUN":
        mon = "06"
    elif mon[:3] == "Jul" or mon[:3] == "JUL":
        mon = "07"
    elif mon[:3] == "Aug" or mon[:3] == "AUG":
        mon = "08"
    elif mon[:3] == "Sep" or mon[:3] == "SEP":
        mon = "09"
    elif mon[:3] == "Oct" or mon[:3] == "OCT":
        mon = "10"
    elif mon[:3] == "Nov" or mon[:3] == "NOV":
        mon = "11"
    elif mon[:3] == "Dec" or mon[:3] == "DEC":
        mon = "12"

    date = str(year)+"-"+str(mon)+"-"+str(day)
    if date == "--":
        return ""
    else:
        return date
def cert_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        if tokens[i] == "Date Public:":
            a = tokens[i+1]

    dt = a

   # # print dt
    mon, day, year = "","",""
    try:
        mon=dt.split(' ')[1] #.replace(",", "")
        day=dt.split(' ')[0]
        year = dt.split(' ')[2]
    except:
        for i in range(len(tokens)):
            if tokens[i] == "Date Updated:":
                a = tokens[i+1]
                try:
                    mon=a.split(' ')[1] #.replace(",", "")
                    day=a.split(' ')[0]
                    year = a.split(' ')[2]
                    date = create_date(year,mon,day)
                    return date
                except IndexError:
                    return ""

def orcale_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        if tokens[i][:11] == "Revision 1:":
            a = tokens[i]

    if a is not "":
        try:
            date=a.split(' ')[4]
            return date
        except IndexError:
            pass
    else:
        for i in range(len(tokens)):
            try:
                if tokens[i][:6] == "Rev 1.":
                    a = tokens[i-1]
            except IndexError:
                pass

    dt = a

    mon,day,year = "","",""
    try:
        mon=dt.split('-')[1] #.replace(",", "")
        day=dt.split('-')[2]
        year = dt.split('-')[0]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
   
def ibm_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    for i in range(len(tokens)):
        if tokens[i] == "RELEASE DATE":
            a = tokens[i+5]

        elif tokens[i][:13] == "First Issued:":
            a = tokens[i]
            
            try:
                mon=a.split(' ')[3]
                day=a.split(' ')[4]
                year = a.split(' ')[7]
                a = str(day)+" "+mon+" "+str(year)
            except IndexError:
                return ""

        elif tokens[i][:22] == "(Original publish date":
            a = tokens[i]
            mon=a.split(' ')[3]
            day=a.split(' ')[4].replace(",", "")
            year = a.split(' ')[5].replace(".", "")
            a = str(day)+" "+mon+" "+str(year)

    dt = a

    mon,day,year = "","",""
    try:
        mon=dt.split(' ')[1] 
        day=dt.split(' ')[0]
        year = dt.split(' ')[2]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def ubuntu_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    # print tokens
    # date = ""
    for i in range(len(tokens)):
        if tokens[i][:22] == "Ubuntu Security Notice":
            a = tokens[i+1]

    dt = a

    mon,day,year = "","",""
    try:
        mon=dt.split(' ')[1].replace(",", "")
        day=dt.split(' ')[0][:2]
        year = dt.split(' ')[2]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""


def gentoo_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    # print tokens
    date = ""
    for i in range(len(tokens)):
        if tokens[i] == "Reported:":
            date = tokens[i+1][:10]
            return date

        elif tokens[i] == "Release Date":
            # print tokens[i]
            a = tokens[i+1]

    dt = a
    mon,day,year = "","",""
    try:
        mon=dt.split(' ')[0]
        day=dt.split(' ')[1].replace(",", "")
        year = dt.split(' ')[2]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""  
def debian_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    # print tokens
    for i in range(len(tokens)):
        if tokens[i] == "Date Reported:":
            a= tokens[i+1]

    dt = a

    if dt is "":
        dt_l =[]
        for i in range(len(tokens)):
            if tokens[i][:4] == "Date":
                dt_l.append(tokens[i])
        if len(dt_l) == 0:
            return ""
        elif len(dt_l) == 1:
            for i in range(len(tokens)):
                if tokens[i] == "Date:":
                    x = tokens[i+1][8:10]
                    y = tokens[i+1][4:7]
                    z = tokens[i+1][20:24]
                    dt = str(x)+" "+y+" "+str(z)
        else:
            dt = dt_l[0][11:22]
            if dt == "":
                dt_l2 = []
                for i in range(len(dt_l)):
                    if dt_l[i][11:22] != "":
                        dt_l2.append(dt_l[i])
                dt = dt_l2[0][11:22]


    mon,day,year = "","",""
    try:
        day = dt[:2]
        mon = dt[2:6]
        year = dt[6:11]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def openwall_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    for i in range(len(tokens)):
        if tokens[i] == "Follow us on Twitter":
            a= tokens[i+2]

    try:
        dt = a[11:22]
        day = dt[:2]
        mon = dt[2:6]
        year = dt[6:12]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def opensuse_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    # print tokens
    for i in range(len(tokens)):
        if tokens[i] == "Date:":
            a= tokens[i+1]
            # print a

    try:
        dt = a[5:16]
        day = dt[:2]
        mon = dt[3:6]
        year = dt[7:11]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def redhat_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    # print tokens
    for i in range(len(tokens)):
        if tokens[i] == "Reported:":
            a= tokens[i+1]
            try:
                dt = a[:10]
                a= dt.split('-')[0]
                return dt
            except IndexError:
                return ""

        elif a is "":
            for i in range(len(tokens)):
                if tokens[i] == "Public Date:":
                    a= tokens[i+1]
                    try:
                        dt = a[:10]
                        return dt
                    except IndexError:
                        return ""

def secunia_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    except ssl.CertificateError as sc:
        return ""
    
    

    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    for i in range(len(tokens)):
        if tokens[i] == "5) Time Table":
            a= tokens[i+1]

    dt = a[:10]

    day = dt[8:10]
    mon = dt[5:7]
    year = dt[:4]

    date = str(year)+"-"+str(mon)+"-"+str(day)
    return date
def securityfocus_date(url1):
    response = ''
    html = ''
    try:
        response = urllib2.urlopen(url1)
        html = response.read()
        response.close()
    except urllib2.HTTPError, ev:
        return ""
    except urllib2.URLError, uu:
        return ""
    except socket.error as e:
        return ""
    soup = BeautifulSoup(html, "lxml")
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    for i in range(len(tokens)):
        if tokens[i] == "Published:":
            a= tokens[i+1]

    try:
        dt = a[:11]
        mon = dt[:3]
        day = dt[4:6]
        year = dt[7:11]
        date = create_date(year,mon,day)
        return date
    except IndexError:
        return ""
def map_x(x):
    try:
        x= x.replace('"','')
    except:
        pass
    if x==None:
        return ""
    try:
        a = x[9]
        return x
    except IndexError:
        return ""

def disclosure_dt_csv_creation():

    with open('/Users/afsahanwar/tmp/json_and_csv/nvdcve-1.0-2008.json') as data_file: #change b too
        data = json.load(data_file)
        

    cve_items=data['CVE_Items']
    #parse_json('null',cve_items)

    item_len = len(cve_items)
    #print item_len
    # count = []
    # count1 = []
    url_freq={}
    t = "reference_freq17"
    for i in range(item_len):
        cve_id = cve_items[i]['cve']['CVE_data_meta']['ID']
        b=20081
        # count = count+1
        # print count
        db_dt1 = cve_items[i]['publishedDate']
        year = db_dt1[:4]
        db_dt1 = db_dt1[:10]

        impact = cve_items[i]['impact']
        severity_v2 = ""
        exploit_v2 = ""
        impact_v2 = ""
        baseScore_v2 = ""
        severity_v3 = ""
        exploit_v3 = ""
        impact_v3 = ""
        baseScore_v3 = ""
        cwe_id =""
        sv2 = ""
        sv3 = ""
        public_date = ""
        date_list = []
        reference_data = cve_items[i]['cve']['references']['reference_data']
        k=""
        try:
            k = cve_id.split('-')[2]
            k = int(k)
        except IndexError:
            pass
        if 273 <= k < 2330:
            for j1 in range(len(reference_data)):
                url = reference_data[j1]['url']
                token=url.split('/')[2]#.split('/')[0]
                domain=token.split('.')[-2]+'.'+token.split('.')[-1]
                print cve_id,url

                # if domain in url_freq:
                #     url_freq[domain] = url_freq[domain]+1
                # else:
                #     url_freq[domain] = 1

                if domain == "securityfocus.com":
                    x = securityfocus_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "secunia.com":
                    x = secunia_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "redhat.com":
                    x = redhat_date(url)
                    x = map_x(x)
                    date_list.append(x)

                # if domain == "osvdb.org" or domain == "vupen.com":
                #     continue

                if domain == "opensuse.org":
                    x = opensuse_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "openwall.com":
                    x = openwall_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "debian.org":
                    x = debian_date(url)
                    x = map_x(x)
                    date_list.append(x)


                if domain == "gentoo.org":
                    x = gentoo_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "ubuntu.com":
                    x = ubuntu_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "ibm.com":
                    x = ibm_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "oracle.com":
                    x = orcale_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "cert.org":
                    x = cert_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "securityreason.com":
                    x = secreason_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "github.com":
                    x = github_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "google.com":
                    x = google_date(url)
                    x = map_x(x)
                    date_list.append(x) 

                if domain == "fedoraproject.org":
                    x = fedora_date(url)
                    x = map_x(x)
                    date_list.append(x) 

                if domain == "mozilla.org":
                    x = mozilla_date(url)
                    x = map_x(x)
                    date_list.append(x) 

                if domain == "cisco.com":
                    x = cisco_date(url)
                    x = map_x(x)
                    date_list.append(x) 

                if domain == "seclists.org":
                    x = seclists_date(url)
                    x = map_x(x)
                    date_list.append(x) 
     
                if domain == "blogspot.com":
                    x = blogspot_date(url)
                    x = map_x(x)
                    date_list.append(x)                

                if domain == "jvn.jp":
                    x = jvnjp_date(url)
                    x = map_x(x)
                    date_list.append(x)                

                if domain == "packetstormsecurity.com":
                    x = packetss_date(url)
                    x = map_x(x)
                    date_list.append(x)  

                if domain == "adobe.com":
                    x = adobe_date(url)
                    x = map_x(x)
                    date_list.append(x)                

                if domain == "novell.com":
                    x = novell_date(url)
                    x = map_x(x)
                    date_list.append(x)                

                if domain == "sourceforge.net":
                    x = sourceforge_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "kernel.org":
                    x = kernel_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "sun.com":
                    x = sun_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "drupal.org":
                    x = drupal_date(url)
                    x = map_x(x)
                    date_list.append(x)


                if domain == "zerodayinitiative.com":
                    x = zdi_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "android.com":
                    x = android_date(url)
                    x = map_x(x)
                    date_list.append(x)


                if domain == "apache.org":
                    x = apache_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "wireshark.org":
                    x = wireshark_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "packetstormsecurity.org":
                    x = packetstormorg_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "vmware.com":
                    x = vm_date(url)
                    x = map_x(x)
                    date_list.append(x)

                if domain == "avaya.com":
                    x = avaya_date(url)
                    x = map_x(x)
                    date_list.append(x)

                # if domain == "hp.com":
                #     x = hp_date(url)
                #     x = map_x(x)
                #     date_list.append(x)

                if domain == "hpe.com":
                    x = hpe_date(url)
                    x = map_x(x)
                    date_list.append(x)
                    # if x == None:
                    #     print url
            
            index1 = []        
            try:
                index1 = sorted(date_list, key=lambda d: map(int, d.split('-')))
            except ValueError:
                pass
            if len(index1)>=1:
                public_date = index1[0]

            out = cve_id+","+public_date+","+db_dt1+"\n"
            b = str(b)
            output_array_creater(out,b)
            time.sleep(3)


                    


        # if len(impact)!=0:
        #     severity_v2 =cve_items[i]['impact']['baseMetricV2']['severity']
        #     exploit_v2 = cve_items[i]['impact']['baseMetricV2']['exploitabilityScore']
        #     impact_v2 = cve_items[i]['impact']['baseMetricV2']['impactScore']
        #     baseScore_v2 = cve_items[i]['impact']['baseMetricV2']['cvssV2']['baseScore']
        #     # print baseScore_v2
        #     # print cve_id, severity_v2, exploit_v2, impact_v2, baseScore_v2

        # if 'baseMetricV3' in impact:

        #     severity_v3 =cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseSeverity']
        #     exploit_v3 = cve_items[i]['impact']['baseMetricV3']['exploitabilityScore']
        #     impact_v3 = cve_items[i]['impact']['baseMetricV3']['impactScore']
        #     baseScore_v3 = cve_items[i]['impact']['baseMetricV3']['cvssV3']['baseScore']
        #     # print cve_id,baseScore_v3
        
                 
        # problemtype_desc = cve_items[i]['cve']['problemtype']['problemtype_data'][0]['description']
        # if len(problemtype_desc) > 1:
        #     cwe_pre =[]
            
        #     # print cve_id, len(problemtype_data)        
        #     for i2 in range(len(problemtype_desc)):
        #         cwe_id_p = problemtype_desc[i2]['value']
        #         cwe_pre.append(cwe_id_p)

        #     for x in range(len(cwe_pre)):
        #         s = cwe_pre[x]
        #         # p = s.split("CWE-", 1)[1]
        #         # if s == "Other" or s == "noinfo":
        #         #     cwe_id = cwe_id + ","+'0'
        #         # else:
        #         cwe_id = cwe_id + ","+s   
                

        # elif len(problemtype_desc) == 1:
        #     cwe_str = problemtype_desc[0]['value']
        #     # t = cwe_str.split("CWE-", 1)[1]
        #     # if t == "Other" or t == "noinfo":
        #     #     cwe_id = cwe_id + ","+'0'
        #     # else:
        #     cwe_id = cwe_id + ","+cwe_str
        #     # print cwe_str,cwe_id

        # cwe_id = cwe_id+ ","+'0'+ ","+'0'


        # if (severity_v2 != "" and severity_v3 != ""):
        # # if (severity_v2 == "MEDIUM" and severity_v3 == "HIGH"): 
        #     # out = cve_id+","+year+","+str(sv2)+","+str(exploit_v2)+","+str(impact_v2)+","+str(baseScore_v2)+","+str(sv3)+","+cwe_id+","+str(0)+","+str(0)+"\n"
        #     out = cve_id+","+severity_v2+","+str(baseScore_v2)+","+str(impact_v2)+","+str(exploit_v2)+","+severity_v3+","+str(baseScore_v3)+","+str(impact_v3)+","+str(exploit_v3)+cwe_id+"\n"            
        #     # print out
        #     # output_array_creater(out)
        #     # return out
        # # print year

        
    # for item in url_freq:
    #     print item+";"+str(url_freq[item])

    # ############## csv for domain name and its frequency #################.
    # for item in url_freq:
    #     item, url_freq[item]
    #     out = item+","+str(url_freq[item])+'\n'
    #     output_array_creater(out,t)


def main():
    disclosure_dt_csv_creation()
    print "Done"
  

if __name__ == "__main__":
    main()

            