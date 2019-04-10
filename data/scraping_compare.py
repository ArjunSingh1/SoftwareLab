from bs4 import BeautifulSoup
import requests
import csv
xboxx_link = 'https://www.nintendo.com/switch/features/tech-specs/'
xboxx_response = requests.get(xboxx_link, timeout=10)

page_content = BeautifulSoup(xboxx_response.content, "html.parser")

#print(page_content.prettify())

content1 = page_content.findAll("table")[0].findAll("td")
datalist = []
for i in range(len(content1)-1):
    if i%2==0:
        datalist.append(content1[i].get_text().encode('utf-8').strip() + ": " + content1[i+1].get_text().encode('utf-8').strip())


with open('consoles2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in datalist:
        writer.writerow([row])
