from bs4 import BeautifulSoup
import requests
import csv
xboxx_link = 'https://www.playstation.com/en-gb/explore/ps4/tech-specs/'
xboxx_response = requests.get(xboxx_link, timeout=10)

page_content = BeautifulSoup(xboxx_response.content, "html.parser")

#print(page_content.prettify())

content1 = page_content.findAll(class_="CM183-table module richtext table-fixed")
data = content1[0].findAll("table")[0].findAll("td")
#print data

content2 = page_content.findAll(class_="CM183-table module richtext")
data2 = content2[0].findAll("table")[0].findAll("td")
#print data2

datalist = []
for i in range(len(data)-1):
    if i%2==0:
        datalist.append(data[i].get_text().encode('utf-8', 'ignore').strip() + ": " + data[i+1].get_text().encode('utf-8', 'ignore').strip())

datalist2 = []
for i in range(len(data2)-1):
    if i%2==0:
        datalist2.append(data2[i].get_text().encode('utf-8', 'ignore').strip() + ": " + data2[i+1].get_text().encode('utf-8', 'ignore').strip())


with open('consoles3.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in datalist:
        writer.writerow([row])

with open('consoles4.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in datalist2:
        writer.writerow([row])
