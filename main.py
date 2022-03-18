import requests
from bs4 import BeautifulSoup
import csv


URL="https://www.premierleague.com/stats/top/players"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")

all_scorer_name=soup.findAll(name="a",class_="statName")[:20]

goal_scorer=[scorer.getText() for scorer in all_scorer_name]

goal_scored=soup.findAll(name="div",class_="stat")[:20]
num_goal_scored=[scorer.getText().strip() for scorer in goal_scored]

players_club=soup.findAll(name="a",class_="statNameSecondary")[:20]
players_clubs=[scorer.getText().strip() for scorer in players_club]


assist_name=soup.findAll(name="a",class_="statName")[:20]
assist_player_name=[scorer.getText() for scorer in assist_name]

with open('premier_league.csv','w',newline='') as f:
    the_writer=csv.writer(f)
    the_writer.writerow(['position','Player Name','goals','Club'])
    for i,(x,y,z) in enumerate(zip(goal_scorer, num_goal_scored,players_clubs)):
        the_writer.writerow([i, x, y, z])