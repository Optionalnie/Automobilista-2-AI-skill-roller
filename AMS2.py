import random

print('Podaj nick uczestnika: ')
nick1 = input()
print('Jaki tier wariacie')
tierchoose = input()


#Race skill
t1=round(random.uniform(0.8,1), 2)
t2=random.randint(75,100)/100
t3=random.randint(70,100)/100
t4=random.randint(60,100)/100

print('Oto race skill')
print(t1)
print(t2)
print(t3)
print(t4)

#Quali
print('Oto skill quali')
qualit1=round(t1 + random.uniform(0,0.050)-random.uniform(0,0.075), 2)
print(qualit1)
qualit2=round(t2 + random.uniform(0,0.050)-random.uniform(0,0.075), 2)
print(qualit2)
qualit3=round(t3 + random.uniform(0,0.050)-random.uniform(0,0.075), 2)
print(qualit3)
qualit4=round(t4 + random.uniform(0,0.050)-random.uniform(0,0.075), 2)
print(qualit4)

#Aggro skill
aggro=round(random.uniform(0.3,1), 2)
print('Oto współczynnik aggro')
print(aggro)

#Def skill
defence=round(random.uniform(0.75,1), 2)
print('Oto wartość umiejętnosci obrony pozycji')
print(defence)

#Stamina skill
stamina=round(random.uniform(0.75,1), 2)
print('Oto wartość wytrzymałości kierowcy')
print(stamina)

#Consistency
consistencyT1=round(t1 - aggro + (random.uniform(0.025, 0.040)), 2)
consistencyT2=round(t2 - aggro + (random.uniform(0.025, 0.040)), 2)
consistencyT3=round(t3 - aggro + (random.uniform(0.025, 0.040)), 2)
consistencyT4=round(t4 - aggro + (random.uniform(0.025, 0.040)), 2)
print('Oto consistency dla każdego tieru')
print(consistencyT1)
print(consistencyT2)
print(consistencyT3)
print(consistencyT4)

#Start skill
startskillt1 = round(t1 - (random.uniform(0, 0.020)), 2)
startskillt2 = round(t2 - (random.uniform(0, 0.020)), 2)
startskillt3 = round(t3 - (random.uniform(0, 0.020)), 2)
startskillt4 = round(t4 - (random.uniform(0, 0.020)), 2)

print('Oto umiejętności startowe kierowców na różnych tierach')
print(startskillt1)
print(startskillt2)
print(startskillt3)
print(startskillt4)

#Wet skill
wetskillt1 = round(t1 - (random.uniform(0.001, 0.3)), 2)
wetskillt2 = round(t2 - (random.uniform(0.001, 0.3)), 2)
wetskillt3 = round(t3 - (random.uniform(0.001, 0.3)), 2)
wetskillt4 = round(t4 - (random.uniform(0.001, 0.3)), 2)

print('Oto umiejętności deszczowe kierowców na różnych tierach')
print(wetskillt1)
print(wetskillt2)
print(wetskillt3)
print(wetskillt4)

#Tyre Mgmt
tyremgmt = round(random.uniform(0.7, 1) - (aggro - 0.3), 2)
print('Oto tyre mgmt')
print(tyremgmt)

#BFConcede
bfconcede=round(random.uniform(0.8, 1), 2)
print('Oto wartość podatności na niebieską flagę :D')
print(bfconcede)

#WeatherMgmt
weathermgmt=round(random.uniform(0.75, 1), 2)
print('Oto wartości umiejętności radzenia sobie kierowcy z pogodą')
print(weathermgmt)

if tierchoose is '1':
    print('Oto lista umiejętności dla zawodnika o nazwie ' + nick1)
    print('Race Skill: ' + str(t1))
    print('Quali: ' + str(qualit1))
    print('Aggro: ' + str(aggro))
    print('Def: ' + str(defence))
    print('Stamina: ' + str(stamina))
    print('Consistency: ' + str(consistencyT1))
    print('start skill: ' + str(startskillt1))
    print('Wet Skill: ' + str(wetskillt1))
    print('Tyre Mgmt: ' + str(tyremgmt))
    print('BFConcede: ' + str(bfconcede))
    print('WeatherMgmt: ' + str(weathermgmt))