from bs4 import BeautifulSoup
import requests,json 
def Test_Sites():
    dict={}
    a=[]
    movie_link=("https://webscraper.io/test-sites")
    url=requests.get(movie_link)
    beauti=BeautifulSoup(url.text,"html.parser")

    for i in beauti.find_all('div',class_="col-md-7 pull-right"):   
        name=i.find("h2",class_="site-heading").a.text.strip()
        a.append(name)
        dict["test_sites"]=a

    with open ("test_sites.json","w+")as file:
        json.dump(dict,file,indent=3)

Test_Sites()
