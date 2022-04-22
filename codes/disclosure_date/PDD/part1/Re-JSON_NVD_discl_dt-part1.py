# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import socket
import time, re
import urllib.error
import ssl
from datetime import datetime

socket.setdefaulttimeout(7)


def output_array_creater(out, fileName):
    csv_out = './'+ fileName +'.csv'
    with open(csv_out, "a") as output:
        output.write(out)
    return


# def codes_gen:
def create_date(year, mon, day):
    day = day.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    mon = mon.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    year = year.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    # print day,mon,year
    print(year, mon, day)
    try:
        t = day[2]
        d = day
        day = mon
        mon = d
    except IndexError:
        day = day
        mon = mon

    if day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7" or day == "8" or day == "9":
        day = str(0) + day

    if mon.lower().startswith("jan"):
        mon = "01"
    elif mon.lower().startswith("feb"):
        mon = "02"
    elif mon.lower().startswith("mar"):
        mon = "03"
    elif mon.lower().startswith("apr"):
        mon = "04"
    elif mon.lower().startswith("may"):
        mon = "05"
    elif mon.lower().startswith("jun"):
        mon = "06"
    elif mon.lower().startswith("jul"):
        mon = "07"
    elif mon.lower().startswith("aug"):
        mon = "08"
    elif mon.lower().startswith("sep"):
        mon = "09"
    elif mon.lower().startswith("oct"):
        mon = "10"
    elif mon.lower().startswith("nov"):
        mon = "11"
    elif mon.lower().startswith("dec"):
        mon = "12"

    print(year, mon, day)
    date = str(year) + "-" + str(mon) + "-" + str(day)
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print(date, "not in correct date format")
        date = "--"
    if date == "--":
        return ""
    else:
        return date


def hpe_date(url1):
    response = ''
    html = ''
    # print(url1)
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i] == "Release Date:":
            a = tokens[i + 1]
            try:
                day = a.split('-')[2]
                return a
            except IndexError:
                return ""


# def hp_date(url1):
#     response = ''
#     html = ''
#     # print(url1)
#     try:
#         req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
#         html = urllib.request.urlopen(req)
#     except urllib.error.HTTPError:
#         return ""
#     except urllib.error.URLError:
#         return ""
#     except socket.error as e:
#         return ""except ssl.SSLError as err:
#     return ""
# #     try:
# soup = BeautifulSoup(html, "lxml")
# except:
#     with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
#         fp.write()+'\n')
# #     a = ''
#     for script in soup(["script", "style"]):
#         script.extract()
#
#     text = soup.get_text()
#     lines = (line.strip() for line in text.splitlines())
#     chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
#     text = '\n'.join(chunk for chunk in chunks if chunk)
#
#     tokens = text.rsplit('\n')
#
#     mon, day, year = "","",""
#
#     if len(tokens) > 1:
#         return url1

def avaya_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i][:22] == "Original Release Date:":
            a = tokens[i]
            try:
                day = a.split(' ')[4]
                mon = a.split(' ')[3]
                year = a.split(' ')[5]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                try:
                    a = tokens[i + 1]
                    day = a.split(' ')[1]
                    mon = a.split(' ')[0]
                    year = a.split(' ')[2]
                    date = create_date(year, mon, day)
                    return date
                except IndexError:
                    return ""


def vm_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    for i in range(len(tokens)):
        # print tokens[i]
        if tokens[i] == "Issue date:":
            a = tokens[i + 1]
            try:
                day = a.split('-')[2]
                return a
            except IndexError:
                a = tokens[i + 2]
                try:
                    day = a.split('-')[2]
                    return a
                except IndexError:
                    return ""


def packetstormorg_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

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
                b = tokens[i + 1]
                mon = a.split(' ')[1]
                day = b.split(' ')[0]
                year = b.split(' ')[1]
            date = create_date(year, mon, day)
            return date
            break


def wireshark_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i][:6] == "author":
            a = tokens[i + 1]
            try:
                day = a.split(' ')[1]
                mon = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Reported:":
            a = tokens[i + 1]
            try:
                date = a.split(' ')[0]
                date = create_date(date.rsplit("-")[0], date.rsplit("-")[1], date.rsplit("-")[2])
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i][:5] == "Date:":
            a = tokens[i]
            try:
                mon = a.split(' ')[1]
                day = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                pass
        elif a == "":
            return ""


def apache_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Created:":
            a = tokens[i + 1]
            try:
                mon = a.split(' ')[0].split('/')[1]
                day = a.split(' ')[0].split('/')[0]
                year = a.split(' ')[0].split('/')[2]
                year = int(year)
                if year > 90:
                    year = str(19) + str(year)
                elif year <= 17:
                    year = str(20) + str(year)
                date = create_date(year, mon, day)
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Date":
            a = tokens[i + 1]
            try:
                day = a.split(' ')[1]
                mon = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Main":
            a = tokens[i + 2]
            try:
                mon = a.split(' ')[1]
                day = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year, mon, day)
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
                    date = create_date(year, mon, day)
                    return date
                except:
                    return ""  # check this again


def android_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i][:9] == "Published":
            try:
                mon = tokens[i].split('|')[0].split(' ')[1]
                day = tokens[i].split('|')[0].split(' ')[2]
                year = tokens[i].split('|')[0].split(' ')[3]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                return ""


def zdi_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
                a = tokens[i + 2].split(' - ')[0]
                return a
            except IndexError:
                return ""


def drupal_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    if len(tokens) > 1:
        print
        url1
    return ""


def sun_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""

    if len(tokens) > 1:
        print
        url1
    return ""


def kernel_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    date_x = []
    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Date:":
            mon = tokens[i + 1].split(' ')[1]
            day = tokens[i + 1].split(' ')[2]
            year = tokens[i + 1].split(' ')[4]
            date = create_date(year, mon, day)
            date_x.append(date)
        elif a == "":
            try:
                if tokens[i][:6] == "author":
                    a = tokens[i].split('>')[1].split(' ')[0]
                    return a
            except IndexError:
                pass

    index = sorted(date_x, key=lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%Y-%m-%d"))
    if len(index) >= 1:
        return index[0]
    else:
        return ""


def sourceforge_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
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
                a = tokens[i + 1]
                return a
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Authored by:":
            try:
                a = tokens[i + 2]
                return a
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Posted by":
            try:
                a = tokens[i + 1]
                return a
            except IndexError:
                pass


def novell_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    for i in range(len(tokens)):

        if tokens[i] == "Reported:":
            try:
                a = tokens[i + 1][:10]
                return a
            except IndexError:
                pass
        elif a == "" and tokens[i] == "Release:":

            try:
                a = tokens[i + 1]
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
                        year = str(20) + str(ya)
                    if ya >= 90:
                        year = str(19) + str(ya)
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
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i][:13] == "Release date:":
            a = tokens[i]
            try:
                mon = a.split(' ')[2]
                day = a.split(' ')[3]
                year = a.split(' ')[4]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                try:
                    mon = a.split(' ')[1].split(':')[1][1:]
                    day = a.split(' ')[2]
                    year = a.split(' ')[3]
                    date = create_date(year, mon, day)
                    return date
                except IndexError:
                    pass
        elif a == "" and tokens[i][:7] == "Created":
            try:
                a = tokens[i].split('Created')[1]
                mon = a.split(' ')[1]
                day = a.split(' ')[0]
                year = a.split(' ')[2]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                a = tokens[i + 1]
                mon = a.split(' ')[0]
                day = a.split(' ')[1]
                year = a.split(' ')[2]
                date = create_date(year, mon, day)
                return date


def packetss_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    for i in range(len(tokens)):

        if tokens[i][:6] == "Posted":
            a = tokens[i]
            try:
                mon = a.split(' ')[1]
                day = a.split(' ')[2]
                year = a.split(' ')[3]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                a = tokens[i]
                b = tokens[i + 1]
                try:
                    mon = a.split(' ')[1]
                    day = b.split(' ')[0]
                    year = b.split(' ')[1]
                    date = create_date(year, mon, day)
                    return date
                except IndexError:
                    return ""


def jvnjp_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    for i in range(len(tokens)):
        if tokens[i][:3].encode('utf-8') == "公表日":
            a = tokens[i].encode('utf-8')[9:]
            mon = a.split('/')[1]
            day = a.split('/')[2]
            year = a.split('/')[0]
            date = create_date(year, mon, day)
            return date
            # return mon,day,year
        elif a == "" and tokens[i][:10] == "Published:":
            a = tokens[i]
            try:
                a = a.split(':')[1].encode("ascii", "replace").split('??')[0]
                mon = a.split('/')[1]
                day = a.split('/')[2]
                year = a.split('/')[0]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                return ""
            except TypeError:
                try:
                    a = a.split(':')[1].split('??')[0]
                    mon = a.split('/')[1]
                    day = a.split('/')[2]
                    year = a.split('/')[0]
                    date = create_date(year, mon, day)
                    return date
                except:
                    with open('./jvnjpException.txt', 'a') as foout:
                        foout.write(url1+"\n")

        elif tokens[i][:3].encode('utf-8') == "公開日":
            try:
                a = tokens[i].encode('utf-8')[12:22]
                mon = a.split('/')[1]
                day = a.split('/')[2]
                year = a.split('/')[0]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                return ""


def blogspot_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    for i in range(len(tokens)):
        if tokens[i].split(' ')[0] == "Monday," or tokens[i].split(' ')[0] == "Tuesday," or tokens[i].split(' ')[
            0] == "Wednesday," or tokens[i].split(' ')[0] == "Thursday," or tokens[i].split(' ')[0] == "Friday," or \
                tokens[i].split(' ')[0] == "Saturday," or tokens[i].split(' ')[0] == "Sunday,":
            a = tokens[i]
            mon = a.split(' ')[1]
            day = a.split(' ')[2]
            year = a.split(' ')[3]
            date = create_date(year, mon, day)
            return date
        elif a == "":
            try:
                g = tokens[i].split(' ')[2]
                try:
                    g = int(g)
                except:
                    pass
                if isinstance(g, int) == True:
                    if g >= 2000 and g <= 2017:
                        a = tokens[i]
                        mon = a.split(' ')[0]
                        day = a.split(' ')[1]
                        year = a.split(' ')[2]
                        date = create_date(year, mon, day)
                        return date
            except IndexError:
                return ""


def seclists_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return "a"
    except urllib.error.URLError:
        return "u"
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')

    mon, day, year = "", "", ""
    for i in range(len(tokens)):
        # return tokens[i]
        if tokens[i] == "Disclosure Timeline:":
            a = tokens[i + 2]
            try:
                a = a.split(' ')[0]
                mon = a.split('-')[1]
                day = a.split('-')[0]
                year = a.split('-')[2]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                pass

        elif tokens[i][:5] == "Date:" and a == "":
            a = tokens[i]
            try:
                mon = a.split(' ')[3]
                day = a.split(' ')[2]
                year = a.split(' ')[4]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                a = tokens[i + 1]
                try:
                    mon = a.split(' ')[1]
                    day = a.split(' ')[0]
                    year = a.split(' ')[2]
                    date = create_date(year, mon, day)
                    return date
                except IndexError:
                    return ""


def cisco_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]

    dt = a

    try:
        dt = dt.encode("ascii", "replace")
        dt = dt.replace("?", " ")
    except TypeError:
        try:
            dt = dt.encode()
            dt = dt.replace("?", " ")
        except:
            try:
                dt = dt.decode()
                dt = dt.replace("?", " ")
            except:
                with open('./encodingErrorUrls.txt', 'a') as fp:
                    fp.write(url1+":"+str(dt)+":"+str(a)+'\n')

    mon, day, year = "", "", ""

    try:
        mon = dt.split(' ')[1]
        day = dt.split(' ')[2]
        year = dt.split(' ')[0]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def mozilla_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
        return ""
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
            a = tokens[i + 1]
            try:
                year = a.split(' ')[2]
            except IndexError:
                a = tokens[i + 1] + " " + tokens[i + 2]
        elif tokens[i] == "Last updated by:" and a is "":
            a = tokens[i + 2]

    dt = a

    mon, day, year = "", "", ""
    try:
        mon = dt.split(' ')[0]
        day = dt.split(' ')[1]
        year = dt.split(' ')[2]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def fedora_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 2]
            date = a.split(' ')[0]
            return date
        if tokens[i][:17] == "Previous message:":
            if tokens[i - 1] != "- Upstream release.":
                a = tokens[i - 1]

    dt = a
    try:
        mon = dt.split(' ')[1]
        day = dt.split(' ')[2]
        year = dt.split(' ')[5]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def google_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 2]
        elif tokens[i] == "Comments":
            try:
                a = tokens[i - 1].split(',')[1].replace("th", "")[1:]
            except IndexError:
                return ""

    dt = a
    mon, day, year = "", "", ""
    try:
        mon = dt.split(' ')[0]
        day = dt.split(' ')[1]
        year = dt.split(' ')[2]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def github_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 3]
        elif tokens[i] == "Latest commit":
            a = tokens[i + 2]
        elif tokens[i].replace("'", "")[:18] == "DisclosureDate => ":
            a = tokens[i].replace("'", "")[18:29]
        elif tokens[i] == "Unified":
            a = tokens[i - 1]
        elif tokens[i] == "opened this Issue":
            a = tokens[i + 1]

    #     elif tokens[i].replace("-", "").replace(" ", "")[:7] == "Public:":
    #         a=tokens[i+1]

    dt = a
    mon, day, year = "", "", ""

    try:
        mon = dt.split(' ')[0]
        day = dt.split(' ')[1]
        year = dt.split(' ')[2]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def secreason_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
                a = tokens[i].replace("-", "").replace(" ", "").split(':')[1]
            elif tokens[i].replace("-", "").replace(" ", "")[:7] == "Public:":
                a = tokens[i + 1]
        except IndexError:
            pass

    dt = a
    mon, day, year = "", "", ""

    if dt is not "":
        try:
            mon = dt.split('.')[0]
            day = dt.split('.')[1]
            year = dt.split('.')[2]
            date = create_date(year, mon, day)
            if date.startswith("-"):
                date = date[1:]
            if date.endswith("-"):
                date = date[:-1]
            date = re.sub("[^0123456789\-]","",date)
            return date
        except IndexError:
            pass
    else:
        for i in range(len(tokens)):
            if tokens[i][:20] == "Vendor Notification:":
                a = tokens[i]
                try:
                    mon = a.split(' ')[3]
                    day = a.split(' ')[2]
                    year = a.split(' ')[4]
                except IndexError:
                    pass

    dt = a
    # Release Date:  04/25/2011

    if a is "":
        for i in range(len(tokens)):
            if tokens[i][:13] == "Release Date:":
                a = tokens[i + 1]
                if a == "unknown":
                    return ""
                else:
                    try:
                        mon = a.split('/')[0]
                        day = a.split('/')[1]
                        year = a.split('/')[2]
                    # return mon,day,year
                    except IndexError:
                        pass

    if a is "":
        for i in range(len(tokens)):
            if tokens[i][1:15] == "DisclosureDate":
                try:
                    a = tokens[i][21:32]
                    # return a[21:32]
                    mon = a.split(' ')[0]
                    day = a.split(' ')[1]
                    year = a.split(' ')[2]
                except IndexError:
                    pass

    if a is "":
        for i in range(len(tokens)):
            # return tokens[i]
            if tokens[i][:7] == "# Date:":
                a = tokens[i]
                try:
                    mon = a.split(' ')[2]
                    day = a.split(' ')[3]
                    year = a.split(' ')[4]
                except IndexError:
                    try:
                        x = a.split(' ')[2]
                        mon = x.split('/')[1]
                        day = x.split('/')[2]
                        year = x.split('/')[0]
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
                    a = tokens[i + 1].replace(" ", "")
                elif tokens[i][:17] == "Original release:":
                    a = tokens[i].replace(" ", "").split(':')[1]
                if a.startswith("-"):
                    a = a[1:]
                if a.endswith("-"):
                    a = a[:-1]
                date = a.rsplit("-")
                date = create_date(date[0], date[1], date[2])
                date = re.sub("[^0123456789\-]", "", date)
                if date.startswith("-"):
                    date = date[1:]
                if date.endswith("-"):
                    date = date[:-1]
                return date
            except IndexError:
                return ""

    day = day.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    mon = mon.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    # year = year.replace(" ", "").replace(",", "").replace(".", "").replace('"', '')
    year = re.sub("[^0123456789\-]", "", year)
    # # # return day,mon,year

    if day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7" or day == "8" or day == "9":
        day = str(0) + day
    if mon == "1" or mon == "2" or mon == "3" or mon == "4" or mon == "5" or mon == "6" or mon == "7" or mon == "8" or mon == "9":
        mon = str(0) + mon

    # # # # # # # return day,mon,year

    if mon[:3] == "Jan" or mon[:3] == "JAN":
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

    date = str(year) + "-" + str(mon) + "-" + str(day)
    if date.startswith("-"):
        date = date[1:]
    if date.endswith("-"):
        date = date[:-1]
    date = re.sub("[^0123456789\-]", "", date)
    if date == "--":
        return ""
    else:
        return date


def cert_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]

    dt = a

    # # print dt
    mon, day, year = "", "", ""
    try:
        mon = dt.split(' ')[1]  # .replace(",", "")
        day = dt.split(' ')[0]
        year = dt.split(' ')[2]
    except:
        for i in range(len(tokens)):
            if tokens[i] == "Date Updated:":
                a = tokens[i + 1]
                try:
                    mon = a.split(' ')[1]  # .replace(",", "")
                    day = a.split(' ')[0]
                    year = a.split(' ')[2]
                    date = create_date(year, mon, day)
                    return date
                except IndexError:
                    return ""


def orcale_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            date = a.split(' ')[4]
            date = create_date(date.rsplit("-")[0], date.rsplit("-")[1], date.rsplit("-")[2])
            date = re.sub("[^0123456789\-]", "", date)
            return date
        except IndexError:
            pass
    else:
        for i in range(len(tokens)):
            try:
                if tokens[i][:6] == "Rev 1.":
                    a = tokens[i - 1]
            except IndexError:
                pass

    dt = a

    mon, day, year = "", "", ""
    try:
        mon = dt.split('-')[1]  # .replace(",", "")
        day = dt.split('-')[2]
        year = dt.split('-')[0]
        date = create_date(year, mon, day)
        date = re.sub("[^0123456789\-]", "", date)
        return date
    except IndexError:
        return ""


def ibm_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    except ssl.CertificateError:
        with open('./sslCertificateError.txt', 'a') as fp:
            fp.write(url1+'\n')

    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 5]

        elif tokens[i][:13] == "First Issued:":
            a = tokens[i]

            try:
                mon = a.split(' ')[3]
                day = a.split(' ')[4]
                year = a.split(' ')[7]
                a = str(day) + " " + mon + " " + str(year)
            except IndexError:
                return ""

        elif tokens[i][:22] == "(Original publish date":
            a = tokens[i]
            mon = a.split(' ')[3]
            day = a.split(' ')[4].replace(",", "")
            year = a.split(' ')[5].replace(".", "")
            a = str(day) + " " + mon + " " + str(year)

    dt = a

    mon, day, year = "", "", ""
    try:
        mon = dt.split(' ')[1]
        day = dt.split(' ')[0]
        year = dt.split(' ')[2]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def ubuntu_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]

    dt = a

    mon, day, year = "", "", ""
    try:
        mon = dt.split(' ')[1].replace(",", "")
        day = dt.split(' ')[0][:2]
        year = dt.split(' ')[2]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def gentoo_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            date = tokens[i + 1][:10]
            date = create_date(date.rsplit("-")[0], date.rsplit("-")[1], date.rsplit("-")[2])
            return date

        elif tokens[i] == "Release Date":
            # print tokens[i]
            a = tokens[i + 1]

    dt = a
    mon, day, year = "", "", ""
    try:
        mon = dt.split(' ')[0]
        day = dt.split(' ')[1].replace(",", "")
        year = dt.split(' ')[2]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def debian_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]

    dt = a

    if dt is "":
        dt_l = []
        for i in range(len(tokens)):
            if tokens[i][:4] == "Date":
                dt_l.append(tokens[i])
        if len(dt_l) == 0:
            return ""
        elif len(dt_l) == 1:
            for i in range(len(tokens)):
                if tokens[i] == "Date:":
                    x = tokens[i + 1][8:10]
                    y = tokens[i + 1][4:7]
                    z = tokens[i + 1][20:24]
                    dt = str(x) + " " + y + " " + str(z)
        else:
            try:
                dt = dt_l[0][11:22]
                if dt == "":
                    dt_l2 = []
                    for i in range(len(dt_l)):
                        if dt_l[i][11:22] != "":
                            dt_l2.append(dt_l[i])
                    dt = dt_l2[0][11:22]
            except:
                return ""

    mon, day, year = "", "", ""
    try:
        day = dt[:2]
        mon = dt[2:6]
        year = dt[6:11]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def openwall_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 2]

    try:
        dt = a[11:22]
        day = dt[:2]
        mon = dt[2:6]
        year = dt[6:12]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def opensuse_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]
            # print a

    try:
        dt = a[5:16]
        day = dt[:2]
        mon = dt[3:6]
        year = dt[7:11]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def redhat_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]
            try:
                dt = a[:10]
                a = dt.split('-')[0]
                return dt
            except IndexError:
                return ""

        elif a is "":
            for i in range(len(tokens)):
                if tokens[i] == "Public Date:":
                    a = tokens[i + 1]
                    try:
                        dt = a[:10]
                        return dt
                    except IndexError:
                        return ""


def secunia_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""

    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]

    dt = a[:10]

    day = dt[8:10]
    mon = dt[5:7]
    year = dt[:4]

    date = str(year) + "-" + str(mon) + "-" + str(day)
    date = create_date(date.rsplit("-")[0], date.rsplit("-")[1], date.rsplit("-")[2])
    return date


def securityfocus_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
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
            a = tokens[i + 1]

    try:
        dt = a[:11]
        mon = dt[:3]
        day = dt[4:6]
        year = dt[7:11]
        date = create_date(year, mon, day)
        return date
    except IndexError:
        return ""


def securitytracker_date(url1):
    response = ''
    html = ''
    try:
        req = urllib.request.Request(url1, headers={'User-Agent': 'Chrome/77.0.3865.90'})
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        return ""
    except urllib.error.URLError:
        return ""
    except socket.error as e:
        return ""
    except ssl.SSLError as err:
        return ""
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        with open('./beautifulSoupErrorUrls.txt', 'a') as fp:
            fp.write(url1+'\n')
    a = ''
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    tokens = text.rsplit('\n')
    for i in range(len(tokens)):
        if tokens[i].strip().startswith("Date"):
            try:
                a = tokens[i].split(':')[1]
                mon = a.split(' ')[-3][2:]
                year = a.split(' ')[-1]
                day = a.split(' ')[-2]
                date = create_date(year, mon, day)
            except:
                try:
                    mon = tokens[i].split(':')[1][2:]
                    day = tokens[i + 1].split(' ')[0]
                    year = tokens[i + 1].split(' ')[1]
                    date = create_date(year, mon, day)
                except IndexError:
                    return ""
            return date
        elif tokens[i].strip().startswith("Published"):
            try:
                a = tokens[i + 1]
                mon = a.split(' ')[0]
                year = a.split(' ')[1]
                day = a.split(' ')[2]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                return ""
        elif tokens[i].strip().startswith("Original Entry Date"):
            try:
                a = tokens[i].split(':')[1]
                mon = a.split(' ')[-3][2:]
                year = a.split(' ')[-1]
                day = a.split(' ')[-2]
                date = create_date(year, mon, day)
            except:
                try:
                    mon = tokens[i].split(':')[1][2:]
                    day = tokens[i + 1].split(' ')[0]
                    year = tokens[i + 1].split(' ')[1]
                    date = create_date(year, mon, day)
                except IndexError:
                    return ""
            return date
        elif tokens[i].strip().startswith("Published"):
            try:
                a = tokens[i + 1]
                mon = a.split(' ')[0]
                year = a.split(' ')[1]
                day = a.split(' ')[2]
                date = create_date(year, mon, day)
                return date
            except IndexError:
                return ""


def map_x(x):
    try:
        x = x.replace('"', '')
    except:
        pass
    if x == None:
        return ""
    try:
        a = x[9]
        return x
    except IndexError:
        return ""


def disclosure_dt_csv_creation():
    cve_url, cve_dt = {}, {}
    url_freq = {}
    t = "reference_freq"

    url_pdd = set()
    f = open('../../cve_url_dt.csv', 'rb')
    count = 0
    for line in f:
        tkn = line.decode().replace('\n', '').rsplit(';')
        cve_id = tkn[0]
        url = tkn[1]
        db_dt1 = tkn[2]
        if cve_id not in cve_url:
            cve_url[cve_id] = set()
            cve_url[cve_id].add(url)
        else:
            cve_url[cve_id].add(url)

        cve_dt[cve_id] = db_dt1

    for cve_id in cve_url:
        urlSet = cve_url[cve_id]
        db_dt1 = cve_dt[cve_id]

        public_date = ""
        date_list = set()

        for url in urlSet:
            token = url.split('/')[2]  # .split('/')[0]
            domain = token.split('.')[-2] + '.' + token.split('.')[-1]
            # print(cve_id, url)
            year = db_dt1[:4]
            count = count + 1
            print(count)

            # if domain in url_freq:
            #     url_freq[domain] = url_freq[domain]+1
            # else:
            #     url_freq[domain] = 1
            if count > 553317 and count <= 559407:
                x = ""

                if domain == "securityfocus.com":
                    x = securityfocus_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "securitytracker.com":
                    x = securitytracker_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "secunia.com":
                    x = secunia_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "redhat.com":
                    x = redhat_date(url)
                    x = map_x(x)
                    date_list.add(x)

                # if domain == "osvdb.org" or domain == "vupen.com":
                #     continue

                if domain == "opensuse.org":
                    x = opensuse_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "openwall.com":
                    x = openwall_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "debian.org":
                    x = debian_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "gentoo.org":
                    x = gentoo_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "ubuntu.com":
                    x = ubuntu_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "ibm.com":
                    x = ibm_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "oracle.com":
                    x = orcale_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "cert.org":
                    x = cert_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "securityreason.com":
                    x = secreason_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "github.com":
                    x = github_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "google.com":
                    x = google_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "fedoraproject.org":
                    x = fedora_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "mozilla.org":
                    x = mozilla_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "cisco.com":
                    x = cisco_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "seclists.org":
                    x = seclists_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "blogspot.com":
                    x = blogspot_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "jvn.jp":
                    x = jvnjp_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "packetstormsecurity.com":
                    x = packetss_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "adobe.com":
                    x = adobe_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "novell.com":
                    x = novell_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "sourceforge.net":
                    x = sourceforge_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "kernel.org":
                    x = kernel_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "sun.com":
                    x = sun_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "drupal.org":
                    x = drupal_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "zerodayinitiative.com":
                    x = zdi_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "android.com":
                    x = android_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "apache.org":
                    x = apache_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "wireshark.org":
                    x = wireshark_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "packetstormsecurity.org":
                    x = packetstormorg_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "vmware.com":
                    x = vm_date(url)
                    x = map_x(x)
                    date_list.add(x)

                if domain == "avaya.com":
                    x = avaya_date(url)
                    x = map_x(x)
                    date_list.add(x)

                # if domain == "hp.com":
                #     x = hp_date(url)
                #     x = map_x(x)
                #     date_list.append(x)

                if domain == "hpe.com":
                    x = hpe_date(url)
                    x = map_x(x)
                    date_list.add(x)
                    # if x == None:
                    #     print url

                out1 = cve_id + "," + url + "," + str(x) + "," + db_dt1 + "\n"
                output_array_creater(out1, "pdd_by_link")
                print(out1)

        if count > 553317 and count <= 559407:
            print(date_list)
            date_list = list(filter(None, list(date_list)))
            print(date_list)
            index1 = []
            # try:
            #     index1 = sorted(date_list, key=lambda d: map(int, d.split('-')))
            # except ValueError:
            #     pass
            if len(date_list) >= 1:
                print("Yaha Pey", date_list, type(date_list))
                try:
                    index1 = sorted(date_list, key=lambda x: datetime.strptime(x, "%Y-%m-%d").strftime("%Y-%m-%d"))
                except:
                    with open('./notInCorrectdateFormat.txt', 'a') as fout:
                        fout.write(str(cve_id)+"\n")
                    continue

                print(index1)
                public_date = index1[0]

            if public_date > db_dt1:
                public_date = db_dt1

            out = cve_id + "," + public_date + "," + db_dt1 + "\n"
            output_array_creater(out, "public_distribution_date_overall")
            print(out, index1, date_list)
            time.sleep(3)


def main():
    disclosure_dt_csv_creation()
    print("Done")


if __name__ == "__main__":
    main()
