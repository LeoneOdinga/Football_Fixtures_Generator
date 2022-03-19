from csv import DictReader
from secrets import choice
max_iterations=10
teams={}
legs=[1,1]
matches=[]
fixtures=[]
#transcribing to usable dic
with open('teams.csv','r') as data_file:
    csv_data=DictReader(data_file)
    for i in csv_data:
            teams.update({i['Team Name']:{'Town':i['Local Town'],'Stadium':i['Team Stadium']}})
#Creating every possible match
for i in teams:
    for j in teams:
        if i!=j:
            matches.append([i,j])
#creating fixture timetable
while matches:
    if len(matches)>1:
        first=choice(matches)
        for i in range(max_iterations):
            if teams[first[0]]['Town']== teams[first[1]]['Town']:
                first=choice(matches)
                #print('Regenerating 1st pair')
            else:
                break
        matches.remove(first)
        second=choice(matches)
        for i in range(len(matches)):
            if len(set(first)-set(second))!=2 or teams[second[0]]['Town']== teams[second[1]]['Town']:
                second=choice(matches)
                #print('Regenerating 2nd pair')
            else:
                break
        matches.remove(second)
        fixtures.append([first,second])
    else:
        fixtures.append(matches[0])
        matches.pop(0)
    #print('Fixture made')
#Formatting timetable
with open('Fixtures.txt','w') as timetable:
    for i in range(len(fixtures)):
        timetable.write(f'Weekend #{i+1}:\n')
        print(f'Weekend #{i+1}:')
        for j in fixtures[i]:
            print(f"\t{teams[j[0]]['Stadium']},{teams[j[0]]['Town']}")
            timetable.write(f"\t{teams[j[0]]['Stadium']},{teams[j[0]]['Town']}\n")
        #Legs attempt
            '''for k in j:
                for l in range(i):
                    #print(f'Checking for {k} in {fixtures[l]}')
                    if k in fixtures[l][0] or k in fixtures[l][1]:
                        legs[0]=20
                        break
                        break
                    else:
                        legs[1]=1
            print(legs)
            print('\t\t',j[0],legs[0],'vs',j[1],legs[1])'''
            timetable.write(f'\t\t{j[0]} vs {j[1]}\n')
            print('\t\t',j[0],'vs',j[1])
            
        
        



