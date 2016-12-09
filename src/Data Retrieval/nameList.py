#This was to fix a file formatting issue that occurred
# early one

totalLists = 10
final = open('allNames3.csv', 'w')
max_name_count = 100000
name_count = 0

for a0 in range(1,totalLists + 1):
    with open('TotalNames' + str(a0) + '.txt', 'r') as f:
        for line in f:
            if 'IS1' not in line:
                writeLine = line.replace(':',',')
                final.write(writeLine)
    f.close()
final.close()
