from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd

team_1 = []
score_1 = []
team_2 = []
score_2 = []
time = []

def get_live_scores():
    URL = "https://www.espncricinfo.com/live-cricket-score"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="ds-p-0")

    item = soup.find_all("div", class_="ds-p-0")
    i = item[0]
    j = i.find_all("div", class_="ds-border-b ds-border-line ds-border-r ds-w-1/2")
    match1 = j[0]
    team1 = match1.find("p", class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
    team2 = match1.find("p", class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3")
    overs = match1.find("span", class_="ds-text-compact-xs ds-mr-0.5")
    run = match1.find_all("strong", class_="ds-text-typo-mid3")
    run_c = match1.find("strong", class_="")
    run_1 = run[0]
    run_2 = run[1]
    team_1.append(team1.text)
    team_2.append(team2.text)
    score_1.append(run_1.text)
    score_2.append(run_2.text)
    time_c = datetime.datetime.now()
    time.append(time_c)
    
    message_ = f"team 1 : {team1.text}   Score: {run_1.text}{run_c.text}   Overs: {overs.text} \n\
team 2 : {team2.text}   score: {run_2.text} \n\n summary = {match1.text}"
    return message_

def csv_generator():
  col = ["team_1" ,"scores_1","team_2","score_2","time"]
  data = pd.DataFrame({"team_1":team_1,"score_1":score_1,"team_2":team_2,"scores_2":score_2,"time":time})
  data.to_csv('scores.csv', index=False)


