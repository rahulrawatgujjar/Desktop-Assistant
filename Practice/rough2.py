import datetime
import calendar
from os import name


query="tell me about weather at bhiwani rha"
# print(a.index("ul"))
ind=int(query.index("weather") + 11)
last=ind
while  True:
    if last==len(query):
        break
    elif query[last]==" ":
        break
    last+=1
    # print(last)
city=query[ind:last]
print(city)
print(len(city))
print(datetime.datetime.now().minute)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().date())
print(datetime.datetime.now().second)
mon_num=datetime.datetime.now().month
# mon=str(calendar.month_name[mon_num])

print(str(datetime.datetime.now().month))
mon=calendar.month_name[mon_num]
print(mon)
print(datetime.datetime.now().year)
print(datetime.datetime.now().day)

query="whatsapp to rohit rawat"
ind=int(query.index("to")+3)
last=ind
while last!=len(query):
    last+=1    
name=query[ind:last]
print(name)
print(len(name))