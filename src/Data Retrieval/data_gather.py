from riotwatcher import RiotWatcher
import time
w = RiotWatcher('<Insert Your API Key Here>')
# check if we have API calls remaining
print(w.can_make_request())
with open('allnames3.csv', 'r+') as f:
    fNew = open('player_data.csv', 'w+')
    while(True):
        line = f.readline()
        if line != "":
            #split data into player information
            time.sleep(1.75)
            line_data = line.replace('\n', '').split(', ')
            print(line_data)
            #Player Id is index 0
            #Try to get data, if none, then don't write anything
            try:
                player_stats = w.get_ranked_stats(line_data[0]) 
            except:
                #For rate limiting issues
                continue
            #Write all the data found into a csv format
            fNew.write(line_data[0] + ', ' + line_data[1] + ', ')
            # Write all the data for each champion down. 
            for champion in player_stats['champions']:
                fNew.write('Champion id, ' + str(champion['id']) + ', ')
                for data in champion['stats']:
                    fNew.write(str(data) + ', ' + str(champion['stats'][data]) + ', ')
            fNew.write('\n')
        else:
            break
    fNew.close()
