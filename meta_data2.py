import requests

from bs4 import BeautifulSoup as bs
from requests import Response

all_games = []

def get_url():

    url = "https://store.playstation.com/en-us/grid/STORE-MSF77008-PS4ALLGAMESCATEG/1"

    response = requests.get(url)

    return response

def get_soup():
    response = get_url()

    soup = bs(response.content, 'html.parser')
    
    game_class = "grid-cell grid-cell--game"
    title = soup.title.string
    games = soup.find_all("div",{"class":game_class})

    game_title ="grid-cell__title"
    game_price = "grid-cell__footer"
    
    for game in games:
        gm_name = game.find("div",{"class":game_title})
        #gm_price = game.find("div", {"class":game_price})

        #gm_name = gm_name.text.replace("\n","")
        #gm_price = gm_price.text.replace("\n","")
        #gm_price = gm_price.replace("$"," $")

        #print(gm_name)
        #print(gm_price)
        #print("\n")

        
        link = game.find('a', href =True)
        link = link['href']

        game_link = "http://store.playstation.com"+str(link)

        all_games.append(game_link)

      
def for_page():   
    for each_page in all_games:
        responses = requests.get(each_page)
        return responses

def each_page():
        responses = for_page()
        soup = bs(responses.content, 'html.parser')



each_page()
    

