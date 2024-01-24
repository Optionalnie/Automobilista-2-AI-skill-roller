import random


t1=round(random.uniform(0.8,1), 2)
t2=random.randint(75,100)/100
t3=random.randint(70,100)/100
t4=random.randint(60,100)/100

print(t1)
print(t2)
print(t3)
print(t4)

#Quali
qualit1=round(t1 + random.uniform(0,0.050)-random.uniform(0,0.075), 2)
print(qualit1)