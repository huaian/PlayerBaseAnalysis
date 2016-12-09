from riotwatcher import RiotWatcher
import time
w = RiotWatcher('<Insert your API Key Here>')
# check if we have API calls remaining
print(w.can_make_request())

#start = 38010076
#start = 38074796
start = 25406330
num_summoners = 40000000


currentDict = {}
#totalDict = {}
if (w.can_make_request()):  
    print("Start")
    for a0 in range(start, num_summoners, 40):
        time.sleep(0.55)
        try:
            names = w.get_summoner_name([x for x in range(a0, a0 + 40)] , region = 'na')
            time.sleep(2)
        except Exception:
            names ={}   
            print("Failed")
            time.sleep(2.5)
            continue
        f2 = open('TotalNames10.txt','a+')
        for name in names:
            try:
                if len(names[name]) <= 3 or names[name][:3] != 'IS1': 
                    f2.write(str(name) + ', ' + str(names[name]) + '\n' )
            except Exception:
                print(a0)
                continue
        f2.close()
        #print(names)
        print(a0)


#newNames = [[name, totalDict[name]] for name in totalDict]
#sorted(newNames)
#for n in newNames:
    
#f2.close()

