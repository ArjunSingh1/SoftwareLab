from bs4 import BeautifulSoup
import requests
import csv
wiiu_link = 'https://kotaku.com/whats-inside-the-wii-u-lets-get-technical-5942980'

wiiu_response = requests.get(wiiu_link, timeout=10)

page_content = BeautifulSoup(wiiu_response.content, "html.parser")

#print(page_content.prettify())
content = page_content.findAll("ul")



with open('consoles6.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    list = content[5].findAll("li")
    for i in range(14):
        li = list[i].get_text().encode('utf-8').strip()
        writer.writerow([li])


