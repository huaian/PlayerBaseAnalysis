import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
PRINT_FREQ = 10000
NUM_FILES = 20
STATS = ['Player Id', 'Player Name', 'Champions Played', 'totalSessionsPlayed', 
'totalSessionsWon', 'totalSessionsLost', 'normalGamesPlayed', 'rankedSoloGamesPlayed', 
'rankedPremadeGamesPlayed', 'botGamesPlayed', 'maxTimePlayed', 
'killingSpree', 'totalUnrealKills', 'totalPentaKills', 'totalQuadraKills', 'totalTripleKills', 'totalDoubleKills', 'totalFirstBlood', 
'mostChampionKillsPerSession', 'maxLargestKillingSpree', 'maxChampionsKilled', 'totalChampionKills', 
'totalDeathsPerSession', 
'totalDamageDealt', 'totalPhysicalDamageDealt', 'totalMagicDamageDealt', 'mostSpellsCast', 'maxLargestCriticalStrike', 
'totalDamageTaken', 'totalHeal', 'totalAssists',  'maxNumDeaths', 
'totalGoldEarned', 'totalMinionKills', 'totalTurretsKilled', 'maxTimeSpentLiving','totalNeutralMinionsKilled']

fAllChamps = open('champ_data.csv', 'w+')

for stat in range(len(STATS)):
    fAllChamps.write(STATS[stat] + ', ')
fAllChamps.write('\n')
lineNum = 0
#with open('player_data.csv', 'r+') as f:
for file_num in range(1, NUM_FILES + 1):
    f = open('player_data' + str(file_num) + '.csv', 'r+')
    if file_num == 2:
        line = f.readline()
        line = f.readline()
    for line in f:
        if lineNum % PRINT_FREQ == 0:
            print(lineNum)
        line_data = line.split(', ')
        player_dict = {'Champions Played': "", 'Player Id':line_data[0], 'Player Name': line_data[1]}
        for i in range(2, len(line_data) - 1 , 2):
            if line_data[i] == "Champion id":
                player_dict['Champions Played'] += line_data[i + 1]+ ';'
            else: 
                if line_data[i] not in player_dict.keys():
                    player_dict[line_data[i]] = int(line_data[i + 1])
                else:
                    player_dict[line_data[i]] += int(line_data[i + 1])
        for data in STATS:
            # if data == "Player Id" or data == "Player Name":
            #     continue
            if data in player_dict.keys():
                fAllChamps.write(str(player_dict[data]))
            else:
                fAllChamps.write('0')
            if (data != STATS[-1]):
                    fAllChamps.write(', ')
        fAllChamps.write('\n')
        lineNum += 1
    f.close()
fAllChamps.close()
