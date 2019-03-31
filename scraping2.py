from bs4 import BeautifulSoup
import requests
import csv
xboxx_link = 'https://www.lifewire.com/xbox-360-specs-3563140'

xboxx_response = requests.get(xboxx_link, timeout=10)

page_content = BeautifulSoup(xboxx_response.content, "html.parser")

#print(page_content.prettify())

content1 = page_content.findAll(class_="mntl-sc-block-heading__text")

content2 = page_content.findAll(class_="comp mntl-sc-block mntl-sc-block-html")

with open('consoles5.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    for i in range(len(content2)):
        if i !=0:
            data2 = content2[i].findAll("ul")
            for ul in data2:
                li = ul.find("li").get_text().encode('utf-8').strip()
                writer.writerow([content1[i-1].get_text().encode('utf-8').strip() + ": " +li])


