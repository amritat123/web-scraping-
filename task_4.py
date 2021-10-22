from bs4 import BeautifulSoup
import requests
import json 

def scrape_movie_details():
    # all_list=[]
    deatils_dict = {}
    director = []
    gensure = []
    url="https://www.imdb.com/title/tt8108198/"
    # print(url.text)
    responce= requests.get(url)
    # print(responce.text)
    soup=BeautifulSoup(responce.text,"html.parser")

    movie_name=soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
    deatils_dict["Movie_name"]=movie_name

    lan = soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base") 
    for i in lan:
        f=i.findAll('li',class_="ipc-metadata-list__item")
        for fi in f:
            if "Country" in fi.text:
                country=fi.find('div',class_="ipc-metadata-list-item__content-container").text
                # print(country)
            elif "Language" in fi.text:
                languages=fi.findAll('a')
                for lang in languages:
                    # print(lang.text)
                    deatils_dict["language"]=lang.text
                    deatils_dict["country"]=country

    gensure_div=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").text
    gensure.append(gensure_div)
    deatils_dict["gensure"]=gensure

    director_div=soup.find("li",class_="ipc-metadata-list__item").a.text
    director.append(director_div)

    deatils_dict["director"]=director

    with open("task_4.json","w")as file:
        json.dump(deatils_dict,file,indent=4)

scrape_movie_details()