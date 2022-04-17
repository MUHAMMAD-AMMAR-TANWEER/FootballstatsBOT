from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
#options.add_argument("--headless") #To take part in linux server
driver = webdriver.Firefox(options=options)
driver.get("https://www.flashscore.com/")

bi = driver.find_element(By.ID,"onetrust-accept-btn-handler")
bi.click()
time.sleep(4)

# wd = driver.find_element(By.CLASS_NAME, "event__participant event__participant--home")
#event__match event__match--live event__match--twoLine
# print(wd)
html = driver.page_source

soup= BeautifulSoup(html,'lxml')

a = soup.find_all("div",class_="event__match event__match--live event__match--twoLine")
#event__match event__match--live event__match--last event__match--twoLine
#class="highlightMsg fontBold" goal notation
print("+++++++++++++++++++++++++++++")
print(a)
print(len(a))
# b = soup.find_all("div" , class_="event__match event__match--live event__match--last event__match--twoLine")
# print(b)
# print(len(b)) To get the finished match right now
#doing the parsing of data
list_of_home_teams = []
list_of_away_teams = []
home_score = []
away_score = []
red_card_status = []
Goal_status = []
time_list = []
c= 0
finallst = []
for stats in a:
    tmp={}
    hometeam = stats.find("div" , class_="event__participant event__participant--home")

    c+=1


    try:
        list_of_home_teams.append(hometeam.text)
        realtext = str(hometeam)
        print(realtext)
        tmp["HomeTeam"] = str(hometeam.text)
        tmp["HomeCard"] = False
        tmp["HomeGoal"] = False

        if 'redCard' in realtext:
            print("RED CARD #################################")
            tmp["HomeCard"] = True
        if 'highlightMsg' in realtext:

            print("Goal")
            tmp["HomeGoal"] = True
        else:
            tmp["HomeCard"] = False
            tmp["HomeGoal"] = False



    except:
        print(hometeam)
        print("Red card")


    awayteam = stats.find("div", class_="event__participant event__participant--away")
    try:
        list_of_away_teams.append(awayteam.text)
        realtext = str(awayteam)
        print(realtext)
        tmp["AwayTeam"] = awayteam.text
        tmp["AwayCard"] = False
        tmp["AwayGoal"] = False
        if 'redCard' in realtext:
            tmp["AwayCard"] = True
            print("RED CARD #################################")
        if 'highlightMsg' in realtext:

            print("Goal")
            tmp["AwayGoal"] = True
        else:
            tmp["AwayCard"] = False
            tmp["AwayGoal"] = False


    except:
        print(awayteam)
        print("red card")
    homescore = stats.find("div", class_="event__score event__score--home")
    home_score.append(homescore.text)
    tmp["HomeScore"] = homescore.text
    awayscore = stats.find("div",class_= "event__score event__score--away")
    away_score.append(awayscore.text)
    tmp["AwayScore"] = awayscore.text
    tim = stats.find("div",class_ ="event__stage--block")
    time_list.append(tim.text.replace(u'\xa0', u' '))
    tmp["MatchTime"] = tim.text.replace(u'\xa0', u' ')
    finallst.append(tmp)
# print("Home Teams")
# print(list_of_home_teams)
# print("Away Teams")
# print(list_of_away_teams)
# print("Home scores")
# print(home_score)
# print("Away Scores")
# print(away_score)
# print("Time of match")
# print(time_list)
print(finallst)




























































#class need to search
# event__participant event__participant--home Team names
#event__participant event__participant--away
#event__score event__score--home #team scores
#event__score event__score--away
#card___l6qxVPI redCard___Re9RTjx icon--redCard icon--redCard-first icon--redCard-last ####red card
#text x="50%" y="15" visibility="hidden" #LIVE MATCHES
#card___l6qxVPI redCard___Re9RTjx icon--redCard
#highlightMsg fontBold goal
#event__stage--block time

#
# time.sleep(5)
# a=0
# # driver.find_element(By.X)
# while a < 10:
#     a+=1
#     # driver.get("https://es.tradingview.com/symbols/BABYDOGEUSDT/")
#     time.sleep(1)
#     # search = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]/span')
#     # base_price = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]')
#     base_price = driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]')
#     # print(search.text)
#     print(base_price.text)
#
# driver.quit()
# #price for OKEX has been done
# Done! Congratulations on your new bot. You will find it at t.me/Soccorfnbot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 5353002254:AAEKDwHpqsfUJWuF1JIPJysWvXcLHfvyeuE
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api
