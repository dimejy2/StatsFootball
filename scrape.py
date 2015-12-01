import os
import sys
import pandas as pd
import pandas_datareader as pdr

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import my_django_project,my_app
from django.db import models
from my_app.models import Player
### Step 4.b - You need to import beautifulsoup or pandas like you ###
### did in the hw so that you can access the module and recycle the code you wrote ###

#def updateplayer(playername,updated_stat1,updated_stat2):
#    try:
#        temp_instance = Player.objects.get(name=playername)

#        try:
#            temp_instance.stat1 = updated_stat1
#        except:
#            pass

#        try:
#            temp_instance.stat2 = updated_stat2
#        except:
#            pass

#        temp_instance.save()

#    except:
#        temp_instance = Player()
#        temp_instance.name=playername

#        try:
#            temp_instance.stat1 = updated_stat1
#        except:
#            pass

#        try:
#            temp_instance.stat2 = updated_stat2
#        except:
#            pass

#        temp_instance.save()


def updateplayer(player_dict):
    playername = ""
    if(player_dict['Player']):
        playername = player_dict['Player']
    else:
        playername = player_dict['Name']

    try:
        temp_instance = Player.objects.get(name=playername)

        try:
            temp_instance.pos = player_dict['Posyahoo-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat1 = player_dict['F Ptsyahoo-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat2 = player_dict['F Ptsfanduel-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat3 = player_dict['F Ptsdraftkings-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat4 = player_dict['F Ptsfantasydraft-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat5 = player_dict['Sunday DraftKings Predfanduel-thursday-ownership-percentages']
        except:
            pass

        try:
            temp_instance.stat6 = player_dict['Thursday%fanduel-thursday-ownership-percentages']
        except:
            pass

        try:
            temp_instance.stat7 = player_dict['Sunday FanDuel Predfanduel-thursday-ownership-percentages']
        except:
            pass

        temp_instance.save()

    except:
        temp_instance = Player()
        temp_instance.name=playername

        try:
            temp_instance.pos = player_dict['Posyahoo-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat1 = player_dict['F Ptsyahoo-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat2 = player_dict['F Ptsfanduel-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat3 = player_dict['F Ptsdraftkings-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat4 = player_dict['F Ptsfantasydraft-nfl-projections']
        except:
            pass

        try:
            temp_instance.stat5 = player_dict['Sunday DraftKings Predfanduel-thursday-ownership-percentages']
        except:
            pass

        try:
            temp_instance.stat6 = player_dict['Thursday%fanduel-thursday-ownership-percentages']
        except:
            pass

        try:
            temp_instance.stat7 = player_dict['Sunday FanDuel Predfanduel-thursday-ownership-percentages']
        except:
            pass

        temp_instance.save()

### Step 4.d - This is where you want to scrape the data ###

### Step 4.e - This is where you want to push the scraped data to your player records ###
### Instead of thet test cases I entered below, write a function to iterate through ###
### Your scraped data records and call the updateplayer funcion to update ###

def scrapeData(url):
    df_list = pd.read_html(url,header=0)
    for df in df_list:
        for i in range(0,len(df)):
            player_dict = {}
            for name in list(df):
                if("Player" in name) or ("Name" in name):
                    player_dict[name] = df[name][i]
                else:
                    player_dict[name+url.split("/")[3]] = df[name][i]
                #player_d['Player'])
            #print(df_rowict['F Pts'] = f_pts[i]
                #player_dict['SiteDiff'] = sitediff[i]
            print(player_dict)
            #print(df_row['F Pts'])
            updateplayer(player_dict)


scrapeData('https://dfsreport.com/yahoo-nfl-projections/')
scrapeData('https://dfsreport.com/fanduel-nfl-projections/')
scrapeData('https://dfsreport.com/fanduel-thursday-ownership-percentages/')
scrapeData('https://dfsreport.com/draftkings-nfl-projections/')
scrapeData('https://dfsreport.com/fantasydraft-nfl-projections/')
#scrapeData('https://dfsreport.com/draftkings-ownership-percentages/')

#def averageprojections():
    #for i in Player:
        #temp_instance.stat8 = (stat1 + stat2 + stat3 +stat4) / 4

Players = Player.objects.all()
for person in Players:
    stat1_type = 0
    stat2_type = 0
    stat3_type = 0
    stat4_type = 0
    summation = 0

    if person.stat1 is None:
        stat1_type = 0
    else:
        stat1_type = 1

    if person.stat2 is None:
        stat2_type = 0
    else:
        stat2_type = 1

    if person.stat3 is None:
        stat3_type = 0
    else:
        stat3_type = 1

    if person.stat4 is None:
        stat4_type = 0
    else:
        stat4_type = 1

    if stat1_type == 1:
        summation = summation + person.stat1

    if stat2_type == 1:
        summation = summation + person.stat2

    if stat3_type == 1:
        summation = summation + person.stat3

    if stat4_type == 1:
        summation = summation + person.stat4

    num_float = stat1_type + stat2_type + stat3_type + stat4_type

    try:
        person.stat8 = summation/num_float
    except:
        pass

    person.save()

#Players = Player.objects.all()
#for person in Players:
    #person.stat8 = ((float(person.stat1) + float(person.stat2) + float(person.stat3) + float(person.stat4)) / 4)

#averageprojections(Player)

#print(stat8)


#
# urlFanDuelProjections='https://dfsreport.com/fanduel-nfl-projections/'
# df_list = pd.read_html(urlFanDuelProjections,header=0)
#
# for df in df_list:
#     player_names = df['Player']
#     f_pts = df['F Pts']
#     sitediff = df['SiteDiff']
#     print(list(df))
#     for i in range(0,len(df)):
#         player_dict = {}
#         player_dict['Name'] = df['Player'][i]
#         player_dict['F Pts'] = f_pts[i]
#         player_dict['SiteDiff'] = sitediff[i]
#         print(player_dict)
#         #print(df_row['Player'])
#         #print(df_row['F Pts'])
#         updateplayer(player_dict['Name'],f_pts[i],sitediff[i])
