from bs4 import BeautifulSoup
import requests
import csv
xboxx_link = 'https://www.xbox.com/en-US/xbox-one-x#techSpecs'

xboxx_response = requests.get(xboxx_link, timeout=10)

page_content = BeautifulSoup(xboxx_response.content, "html.parser")


content1 = page_content.findAll(class_="x-type-center h-divider oneFiftyCol")
memorydata = content1[0].findAll("h4")
memorytitle = content1[0].findAll("p")

content2 = page_content.findAll(class_="x-type-center v-hidden h-divider oneFiftyCol")
storagedata = content2[0].findAll("h4")
storagetitle = content2[0].findAll("p")

content3 = page_content.findAll(class_="x-type-center oneFiftyCol")
GDDdata = content3[0].findAll("h4")
GDDtitle = content3[0].findAll("p")

capabilities = content1[1].findAll("h4")
captitle = content1[1].findAll("p")

hdmidata = content2[1].findAll("p")
hdmititle = content2[1].findAll("h4")

hdrdata = content3[1].findAll("p")
hdrtitle = content3[1].findAll("h4")

dtsdata = content1[2].findAll("p")
dtstitle = content1[2].findAll("h2")

dolbydata = content2[2].findAll("p")
dolbytitle = content2[2].findAll("h4")

PCMdata = content3[2].findAll("p")
PCMtitle = content3[2].findAll("h4")

wifidata = content2[3].findAll("p")
wifititle = content2[3].findAll("h4")

irdata = content3[3].findAll("p")
irtitle = content3[3].findAll("h4")

content4 = page_content.findAll(class_="specsRight connectivity")
condata = content4[0].findAll("p")

#Memory & Storage
memory = memorytitle[0].get_text() + ": " + memorydata[0].get_text()

storage = storagetitle[0].get_text() + ": " + storagedata[0].get_text()

GDD = GDDtitle[0].get_text() + ": " + GDDdata[0].get_text()

#Video Capabilities
cap = captitle[0].get_text() + ": " + capabilities[0].get_text()

HDMI = hdmititle[0].get_text() + ": " + hdmidata[0].get_text()

HDR = hdrtitle[0].get_text() + ": " + hdrdata[0].get_text()

#Audio Components
DTS = dtstitle[0].get_text() + ": " + dtsdata[0].get_text()

DOLBY = dolbytitle[0].get_text() + ": " + dolbydata[0].get_text()

PCM = PCMtitle[0].get_text() + ": " + PCMdata[0].get_text()

#Wireless Capability
WIFI = wifititle[0].get_text() + ": " + wifidata[0].get_text()

IR = irtitle[0].get_text() + ": " + irdata[0].get_text()

#Connectivity
Conn = "Connectivity: " + condata[0].get_text() + ", " + condata[1].get_text() + ", " \
       + condata[2].get_text() + ", " + condata[3].get_text() + ", " + condata[4].get_text() + ", " \
       + condata[5].get_text()



datalist = []
datalist.append(memory)
datalist.append(storage)
datalist.append(GDD)
datalist.append(cap)
datalist.append(HDMI)
datalist.append(HDR)
datalist.append(DTS)
datalist.append(DOLBY)
datalist.append(PCM)
datalist.append(WIFI)
datalist.append(IR)
datalist.append(Conn)

#print datalist

with open ('consoles.csv','wb') as csvfile:
       writer = csv.writer(csvfile, delimiter =',', quoting =csv.QUOTE_MINIMAL)
       for row in datalist:
              writer.writerow([row])
