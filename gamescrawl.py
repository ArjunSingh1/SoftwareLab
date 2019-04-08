import requests
from bs4 import BeautifulSoup
import csv

ps4_path = "/wiki/List_of_PlayStation_4_games"
ps4_next = ps4_path + "_(M-Z)"
ps3_path1 = "/wiki/List_of_PlayStation_3_games_released_on_disc"
ps3_path2 = "/wiki/List_of_download-only_PlayStation_3_games"
switch_path = "/wiki/List_of_Nintendo_Switch_games#Games_list"
switch_next = "/wiki/List_of_Nintendo_Switch_games_(M-Z)#Games_list_(M-Z)"

xbox360_path = "/wiki/List_of_Xbox_360_games"
xbox360_next = xbox360_path + "_(M-Z)"
xboxone_path = "/wiki/List_of_Xbox_One_games"
wiiu_path = "/wiki/List_of_Wii_U_games"

domain = "https://en.wikipedia.org"

#scans given page for all games for each console
def main():
    tag = 'td'
    search_page(url = (domain + ps4_path), name = "PS4_Games", append=False, tag=tag)
    search_page(url = (domain + ps4_next), name = "PS4_Games", append=True, tag=tag)
    search_page(url = (domain + ps3_path1), name = "PS3_Games", append=False, tag=tag)
    search_page(url = (domain + ps3_path2), name = "PS3_Games", append=True, tag=tag)
    search_page(url = (domain + wiiu_path), name = "WiiU_Games", append=False, tag=tag)
    search_page(url = (domain + xbox360_path), name = "Xbox360_Games", append=False, tag=tag)
    search_page(url = (domain + xbox360_next), name = "Xbox360_Games", append=True, tag=tag)
    search_page(url = (domain + xboxone_path), name = "XboxOne_Games", append=False, tag=tag)
    tag = 'th'
    search_page(url = (domain + switch_path), name = "Switch_Games", append=False, tag=tag)
    search_page(url = (domain + switch_next), name = "Switch_Games", append=True, tag=tag)

    print("done")





#Spiders to pages in search of platforms and images
def search_game_page(path):
    url = domain + path
    #get contents from url 
    more_content = requests.get(url).content
    #get soup 
    more_soup = BeautifulSoup(more_content,'lxml') #choose lxml parser
    more_table = more_soup.find('table', {"class" : "infobox hproduct"})

    # find the tag : <img ... >
    image_tag = more_table.find('img')
    # return image urls
    image_url = image_tag.get('src')
    return image_url

#if game has a link, link is scraped and returned
def find_link(tag, tr):
    if tr.find(tag).find('a'):
        path = tr.find(tag).find('a')['href']
        return path

#saves all scraped games to a csv file
def file_save(csv_file, tr, tag, header):
    game_write = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    col1 = "title"
    col2 ="image_link"
    if header:
        game_write.writerow([col1, col2])
    
    length = len(tr)
    for i in range(2,(length-3)):
        try:
            title = tr[i].find(tag).find('i').text
            path = find_link(tag, tr=tr[i])
            if path:
                image = "https:" + search_game_page(path)
            else:
                image = "unreleased"
                #path = "0"
            game_write.writerow([title,image])
            print(title)
        except:
            print("failed:")

#given a url, search for all game names on A-L and M-Z
def search_page(url, name, append, tag):

    #get game html table
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {"id" : "softwarelist"})
    body = table.find('tbody')
    tr = body.find_all('tr')
    
    #save titles and links
    if append:
        with open(name, mode='a') as games_file:
            file_save(csv_file=games_file, tr=tr, tag=tag, header=0)
    else:
        with open(name, mode='w') as games_file:
            file_save(csv_file=games_file, tr=tr, tag=tag, header=1)

if __name__ == "__main__":
    main()




