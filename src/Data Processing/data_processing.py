'''
Author: Jason Ma
Date: 12/4/2016
This code is used to aggregate all the champion data about a player and produce
extra features about the player
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
PRINT_FREQ = 10000
EXCLUDE = ['Player Id', 'Player Name', 'Champions Played', 'rankedSoloGamesPlayed', 'normalGamesPlayed', 'totalFirstBlood', 'mostSpellsCast',
'rankedPremadeGamesPlayed', 'botGamesPlayed', 'maxTimePlayed','totalUnrealKills', 'totalPentaKills', 'totalQuadraKills', 'totalTripleKills', 'totalDoubleKills', 'maxTimeSpentLiving',
 ]

STATS = ['Player Id', 'Player Name', 'Champions Played', 'totalSessionsPlayed', 
'totalSessionsWon', 'totalSessionsLost', 'normalGamesPlayed', 'rankedSoloGamesPlayed', 
'rankedPremadeGamesPlayed', 'botGamesPlayed', 'maxTimePlayed', 
'killingSpree', 'totalUnrealKills', 'totalPentaKills', 'totalQuadraKills', 'totalTripleKills', 'totalDoubleKills', 'totalFirstBlood', 
'mostChampionKillsPerSession', 'maxLargestKillingSpree', 'maxChampionsKilled', 'totalChampionKills', 
'totalDeathsPerSession', 
'totalDamageDealt', 'totalPhysicalDamageDealt', 'totalMagicDamageDealt', 'mostSpellsCast', 'maxLargestCriticalStrike', 
'totalDamageTaken', 'totalHeal', 'totalAssists',  'maxNumDeaths', 
'totalGoldEarned', 'totalMinionKills', 'totalTurretsKilled', 'maxTimeSpentLiving','totalNeutralMinionsKilled']

EXCLUDE += STATS

NEWSTATS = ['winLossRatio', 'killsPerSession', 'assistsPerSession', 'deathsPerSession',  
'goldPerSession', 'minionKillsPerSession', 'healsPerSession', 
'averageDamagePerSession', 'magicDamagePerSession', 'physicalDamageDealtPerSession']


def calculateNewStats(player_dict):
    totalGamesPlayed = int(player_dict['totalSessionsPlayed'])
    player_dict['winLossRatio'] = 100 * abs(int(player_dict['totalSessionsWon']) / totalGamesPlayed) #/ 47.880132  
    player_dict['killsPerSession'] = abs(int(player_dict['totalChampionKills']) / totalGamesPlayed) #/ 5.497961 
    player_dict['assistsPerSession'] = abs(int(player_dict['totalAssists']) / totalGamesPlayed) #/ 8.964787 
    player_dict['deathsPerSession'] = abs(int(player_dict['totalDeathsPerSession']) / totalGamesPlayed) #/ 6.000993 
    player_dict['goldPerSession'] = abs(int(player_dict['totalGoldEarned']) / totalGamesPlayed) #/ 11693.127607
    # print("Total Minions Killed:" + str(int((player_dict['totalMinionKills']))))
    # print("Total Neutral Killed:" + str(player_dict['totalNeutralMinionsKilled']))
    player_dict['minionKillsPerSession'] = abs(int(player_dict['totalMinionKills']) + int(player_dict['totalNeutralMinionsKilled'])) / totalGamesPlayed #/ 124.986912
    # print(player_dict['minionKillsPerSession'])
    player_dict['healsPerSession'] = abs(int(player_dict['totalHeal']) / totalGamesPlayed) #/ 2551.422964
    player_dict['averageDamagePerSession'] = abs(int(player_dict['totalDamageDealt']) / totalGamesPlayed) #/ 2.697392e+05
    player_dict['magicDamagePerSession'] = abs(int(player_dict['totalMagicDamageDealt']) / totalGamesPlayed ) #/ 44066.43638
    player_dict['physicalDamageDealtPerSession'] = abs(int(player_dict['totalPhysicalDamageDealt']) / totalGamesPlayed) #/ 63739.195741


new_f = open('player_data_plus.csv', 'w+')
for stat in STATS:
    if stat not in EXCLUDE:
        new_f.write(stat)
        new_f.write(', ')
for stat in range(len(NEWSTATS)):
    new_f.write(NEWSTATS[stat])
    if stat != len(NEWSTATS) - 1:
        new_f.write(', ')
new_f.write('\n')

debug = True
counter = 0
with open('champ_data.csv') as f:
    f.readline()
    for line in f:
        line_data = line.split(', ')
        for data in range(len(line_data)):
            if '\n' in line_data[data]: 
                line_data[data] = line_data[data].replace('\n', '')
        player_dict = {'Player Id':line_data[0], 'Player Name': line_data[1], 'Champions Played':line_data[2]}
        for i in range(3, len(line_data)):
            player_dict[STATS[i]] = line_data[i]
        calculateNewStats(player_dict)
        # print(player_dict)
        if 100 > float(player_dict['winLossRatio']) > 0:
            for stat in STATS:
                # print(player_dict[STATS[stat]])
                if stat not in EXCLUDE:
                    new_f.write(str(player_dict[stat]) + ', ')

            for stat in range(len(NEWSTATS)):   
                # print(player_dict[NEWSTATS[stat]])
                if NEWSTATS[stat] not in player_dict.keys():
                    print("This guy has no data {0}".format(player_dict['Player Name']))
                new_f.write(str(player_dict[NEWSTATS[stat]]) ) 
                if stat != len(NEWSTATS) - 1:
                    new_f.write(', ')
            new_f.write(' \n')
        counter += 1
        if counter % PRINT_FREQ == 0:
            print(counter)
        if counter > 3000000:
            break
new_f.close()