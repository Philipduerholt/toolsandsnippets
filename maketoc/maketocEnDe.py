#
#Auf mein eigenes github hochladen. Thorsten holt sich's ab
#

import requests
from bs4 import BeautifulSoup
import re
from lxml import html
import lxml.etree as ET


result = requests.get("https://wiki.de.dariah.eu/display/TextGrid/User+Manual+2.0")

x = result.content

soup = BeautifulSoup(x, "lxml")

elements = soup.find("ul", class_="childpages-macro")

tagsEn = soup.select('ul.childpages-macro a[href]')

urls =[]
labelsEn =[]
labelsDe =[]

#
#Populate labelsEn
#

for tag in tagsEn:
    url = 'https://wiki.de.dariah.eu' + str(re.findall(r'(?:[/]).*?(?=")',str(tag)))[2:-2]
    urls.append(url)
    labelsEn.append(tag.contents)

#
#Populate labelsDe
#

for url in urls:
    temp = str(url)
    headers = {'Accept-Language' : 'de'}
    r = requests.get(temp, headers=headers)
    try:
        func = re.search('document\.title\.replace\(pageTitleOld\, \".*\"\)', r.text).group()
        label = re.search('\".*\"\)', func).group()
        label = label[1:-2]
    except:
        tempList = url.split("/")
        label = tempList[-1].replace("+", " ")
    labelsDe.append(label)

#
#Write elementsEn.xml
#
	
with open("elementsEn.xml", 'w', encoding = 'utf-8') as elementoutEn:
    elementsTmp = "<root>" + str(elements) + "</root>"
    elementoutEn.write(elementsTmp)

#
#Write elementsDe.xml
#

with open("elementsDe.xml", 'w', encoding = 'utf-8') as elementoutDe:
    counter = 0
    for node in elements.findAll(text = True):
        node.replace_with(labelsDe[counter])
        counter += 1
    elements = "<root>" + str(elements) + "</root>"
    elementoutDe.write(elements)

#
#Transform both
#
	
domEn, domDe = ET.parse('elementsEn.xml'), ET.parse('elementsDe.xml')
xslt = ET.parse("textgridtransform.xsl")
transform = ET.XSLT(xslt)
newdomEn, newdomDe = transform(domEn), transform(domDe)

#
#Write both tocs
#

with open('tocmasterEn.xml', 'w', encoding = 'utf-8') as toc:
    toc.write(str(ET.tostring(newdomEn, pretty_print=True, encoding = 'utf-8')).replace('\\n', '\n')[2:])


with open('tocmasterDe.xml', 'w', encoding = 'utf-8') as toc:
    toc.write(str(ET.tostring(newdomDe, pretty_print=True, encoding = 'utf-8')).replace('\\n', '\n')[2:])