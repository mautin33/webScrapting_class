import requests
from bs4 import BeautifulSoup as bs


all_games = []

def get_url():
    url = "https://store.playstation.com/en-us/grid/STORE-MSF77008-PS4ALLGAMESCATEG/"
    response = requests.get(url)

    return response



def get_soup():
    response = get_url()#call the get_url function
    return response



def get_soup():
    response = get_url()#call the get_url function
    soup = bs(response.content, 'html.parser')#parse page source to bs4

    title = soup.title.string#for the page title

    game_class = "grid-cell grid-cell--game"#class for the game cards

    games = soup.find_all("div",{"class":game_class})

    for game in games:
        name = game.find("div", {"class":"grid-cell__title"})
        #print(name.text)

        link = game.find('a', href=True)
        link = link['href']

        game_link = "http://store.playstation.com"+str(link)

        all_games.append(game_link)

        #print(game_link)


def get_game():
    game_pg_pc = "price-display__price"
    game_pg_genre = "tech-specs__menu-items"
    game_pg_rating = "provider-info__rating-count"
    game_pg_reldate = "provider-info__text"
    game_pg_descrip = "pdp__description"
    for link in all_games:
        response = requests.get(link)
        game_page = bs(response.content, 'html.parser')
        try:
            game_pg_price = game_page.find("h3",{"class":game_pg_pc}).text
        except:
            game_pg_price = ""
        try:    
            game_pg_gen = game_page.find("li",{"class":game_pg_genre}).text
        except:
            game_pg_gen =""
        try:
            game_pg_rate = game_page.find("div",{"class":game_pg_rating}).text
        except:
            game_pg_rate = ""
        try:
            game_pg_release = game_page.find_all("span",{"class":game_pg_reldate}).text
            #game_pg_release = game_page.find_all("h5",{"class":game_pg_reldate}).text
        except:
            game_pg_release = ""
        try:
            game_pg_description = game_page.find("div",{"class":game_pg_descrip}).text
        except:
            game_pg_description = ""

        title = game_page.title.string
        print("Game Name : ", title)
        print("Game Price :", game_pg_price)
        print("Game Genre: ", game_pg_gen)
        print("Game Rating : ", (game_pg_rate).strip())
        print("Game Release Date: ", game_pg_release)
        print("Game Description : ", game_pg_description)  
        
        print("\n")
        
        


get_soup()
get_game()