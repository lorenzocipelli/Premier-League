from utils import URL_INDEX, URL_BASE, HEADERS
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

pattern = re.compile('\W')

def get_teams_links() :
    links = [] # lista di stringhe
    try :
        req = requests.get(URL_INDEX, HEADERS)
        soup = BeautifulSoup(req.content, 'html.parser')

        # trovo il titolo della sezione Premier League
        h4 = soup.find('h4', id='premier-league')
        # prendo il div che segue, contenente tutti i teams
        div_teams = h4.find_next_sibling()
        # prendo tutti i figli contenenti i link ai teams
        teams_list = div_teams.find_all('li')

        # per ognuno di questi elementi prendo gli href
        # per costuire i link finali per ogni team
        for team in teams_list :
            link_team = team.a['href']
            link_team_name = re.sub(pattern, ' ', link_team).lstrip().rstrip().title()
            #print(link_team_name)
            link_team = URL_BASE + link_team 
            links.append((link_team_name, link_team)) # passo una tupla
    except :
        print("\nRequest error while getting teams links")

    return links

def get_team_top_news() :
    links = get_teams_links() # trovo gli url di ogni squadra e il nome della squadra
    top_news_list = []

    for link in links :
        req = requests.get(link[1], HEADERS)
        soup = BeautifulSoup(req.content, 'html.parser')

        news_title_tag = soup.find('a', class_='news-top-story__headline-link')
        news_title = news_title_tag.get_text()
        news_title = re.sub("\s\s+", " ", news_title)
        news_link = news_title_tag['href']
        
        # vado a questo punto a leggere il contenuto della notizia
        req = requests.get(news_link, HEADERS)
        soup = BeautifulSoup(req.content, 'html.parser')
        
        # cerco questo div per non avere testo che non appartiene alla news
        article_body = soup.find('div', class_='sdc-article-body sdc-article-body--lead')
        paragraphs = article_body.find_all('p')

        content_list = [] # svuoto la lista / creo
        for para in paragraphs : # per ogni paragrafo nella lista
            content_list.append(para.get_text()) # prendo il testo

        content = " ".join(content_list) # unisco i vari paragrafi
        content = re.sub("\s\s+", " ", content) # tolgo gli spazi in eccesso
        content = content.replace(';', '.') # per non avere problemi con le stringhe

        object_to_append = {
            'team_name': link[0],
            'news_content': content 
        }

        # aggiungo la news al dictionary
        top_news_list.append(object_to_append)

    df = pd.DataFrame.from_dict(top_news_list) 
    df.to_csv (r'database/football_news.csv', index = False, header=True)
    print("DOWNLOAD news completed!")

#get_team_top_news()