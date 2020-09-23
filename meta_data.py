import requests
# using the requests library in python
from bs4 import BeautifulSoup as bs
# importing from beautifulsoup

all_games = []

def get_url():
    # url from the site you want to scrap
    url = "https://store.playstation.com/en-us/grid/STORE-MSF77008-PS4ALLGAMESCATEG/1"
    # 
    response = requests.get(url)
    # print the output in text format
    #print(response.text)

#get_url()
    return response


def get_soup():
    response = get_url()
    # parse page source to bs4
    soup = bs(response.content, 'html.parser')
    
    #checking title of a page
    title = soup.title.string
    #print(title)

    #class for game cards
    game_class = "grid-cell grid-cell--game"

    games = soup.find_all("div",{"class":game_class})

    game_title ="grid-cell__title"
    game_price = "grid-cell__footer"
    
    for game in games:
        gm_name = game.find("div",{"class":game_title})
        gm_price = game.find("div", {"class":game_price})

        #gm_name = gm_name.text.replace("\n","")
        #gm_price = gm_price.text.replace("\n","")
        #gm_price = gm_price.replace("$"," $")
        
        link = game.find('a', href =True)
        #print((link['href']))
        link = link['href']

        game_link = "http://store.playstation.com"+str(link)

        all_games.append(game_link)
        print(game_link)



        # print(gm_name)
        # print(gm_price)
        # print("\n")

        # print(gm_name.text, gm_price.text,end =" ")
    return gm_name,gm_price
#get_soup()

def in_detail():

    for full_link in all_games:
        print(str(gm_name) + str(gm_price) , str(full_link))
        




#price-display__price
    
# <a href="/en-us/product/UP0006-CUSA19013_00-FIFA21PREDELUXNA" 
# id="ember1121" 
# class="internal-app-link ember-view">  


    # for game in games:
    #     price = game.find("div",{"class":game_price})
    #     print(price.text)
    #     #print(game.text)
    #     #print(game)
    #     #checking for the title
    #     #name = game.find("div",{"class":""})
    #     #print(name.text)
        






    # reponse.statuscode 
    # to check the website status
    # 200 mean okay 404 mean not found