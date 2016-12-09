import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
PRINT_FREQ = 1000
NUM_FILES = 15
STATS = ['Player Id', 'Player Name', 'Champions Played', 'totalSessionsPlayed', 
'totalSessionsWon', 'totalSessionsLost', 'normalGamesPlayed', 'rankedSoloGamesPlayed', 
'rankedPremadeGamesPlayed', 'botGamesPlayed', 'maxTimePlayed', 
'killingSpree', 'totalUnrealKills', 'totalPentaKills', 'totalQuadraKills', 'totalTripleKills', 'totalDoubleKills', 'totalFirstBlood', 
'mostChampionKillsPerSession', 'maxLargestKillingSpree', 'maxChampionsKilled', 'totalChampionKills', 
'totalDeathsPerSession', 
'totalDamageDealt', 'totalPhysicalDamageDealt', 'totalMagicDamageDealt', 'mostSpellsCast', 'maxLargestCriticalStrike', 
'totalDamageTaken', 'totalHeal', 'totalAssists',  'maxNumDeaths', 
'totalGoldEarned', 'totalMinionKills', 'totalTurretsKilled', 'maxTimeSpentLiving','totalNeutralMinionsKilled']

champStats = ['totalQuadraKills', 'maxChampionsKilled', 'mostChampionKillsPerSession', 'totalSessionsPlayed', 'totalDeathsPerSession', 'totalDamageDealt', 'totalMinionKills', 'totalChampionKills', 'totalFirstBlood', 'totalGoldEarned', 'Champion Id', 'totalDoubleKills', 'totalTurretsKilled', 'totalUnrealKills', 'maxNumDeaths', 'totalSessionsLost', 'totalMagicDamageDealt', 'totalSessionsWon', 'totalAssists', 'totalPhysicalDamageDealt', 'totalTripleKills', 'totalPentaKills', 'mostSpellsCast', 'totalDamageTaken']
fAllChamps = open('champ_data.csv', 'w+')

lineNum = 0
championL = []
champIdL = []
nowBreak = False
#with open('player_data.csv', 'r+') as f:
for file_num in range(1, NUM_FILES + 1):
    f = open('player_data' + str(file_num) + '.csv', 'r+')
    if file_num == 2:
        line = f.readline()
        line = f.readline()
    for line in f:
        if lineNum % PRINT_FREQ == 0:
            print(lineNum)

        lines = line.split(', ')[:-1]
        # print(lines)
        # print(len(lines))
        #for data in lines:
        numChamps = 0
        champId = None
        for data in range(2, len(lines),2):
            if lines[data] == 'Champion id':
                if lines[data + 1] not in champIdL:
                    champId = lines[data + 1]
                    champIdL.append(lines[data + 1])
                    championL.append({'Champion Id': champId})
                else:
                    champId = lines[data + 1]

            else:
                # print(lines[data])
                ind = champIdL.index(champId)
                if lines[data] not in championL[ind].keys():
                    championL[ind][lines[data]] = lines[data + 1]
                else:
                    championL[ind][lines[data]] += lines[data + 1]

        # nowPrint = False
        # for data in lines:
        #     if nowPrint:
        #         print(data)
        #         nowPrint = False
        #     if data == "Champion id":
        #         nowPrint = True


        # if nowBreak:
        #     breaknowBreak = True
        lineNum += 1
    print(championL[0].keys())
    f.close()

for champion in championL:
    fAllChamps.write("Champion Id, " + champion["Champion Id"])
    for key in champion.keys():
        if key != "Champion Id":
            fAllChamps.write(key + ', ' + champion[key] + ', ')
    fAllChamps.write('\n')
fAllChamps.close()
