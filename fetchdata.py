from requests_html import HTMLSession

import json
import time
import os
from calendar import monthrange
import datetime 
import requests



def getFirstFixture():
    now = time.localtime().tm_year
    s = HTMLSession()

# Futbol takımlarının fikstür bilgisi
    appendTable = []

    for url in range(2008, now):
        url = f"https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-s%C3%BCper-lig/{url}-{url+1}/482ofyysbdbeoxauk19yg7tdt"

        r = s.get(url)
        year = r.html.find('.component-dropdown__custom-label')[0].text
        myYear = int(year.split("/")[0])
        if myYear < now:

            table = r.html.find('table')[0]
            tabledata = [[c.text for c in row.find(
                'td')[2:]] for row in table.find('tr')[1:]]

            id = 1
            for data in tabledata:
                data.insert(0, id)
                id += 1

            tabledata.insert(0, year+" : ")
            appendTable.append(tabledata)
    link = r"app/r.text"        
    with open(link, "w") as f:
        x = time.time()
        f.write(f"{x}")
             
    with open(r"app/register.json", 'w') as f:
        json.dump(appendTable, f)
    


def fetchMatchData(func1, func2):

    if (not os.path.isfile(r"app/r.text")):
        func1
        func2
    else:
        func2


def presentMatchData():
    now = time.localtime().tm_year
    s = HTMLSession()
    url = f"https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-s%C3%BCper-lig/{now}-{now+1}/482ofyysbdbeoxauk19yg7tdt"
    r = s.get(url)
    year = r.html.find('.component-dropdown__custom-label')[0].text
    table = r.html.find('table')[0]
    tabledata = [[c.text for c in row.find('td')[2:]]
                 for row in table.find('tr')[1:]]

    id = 1
    for data in tabledata:
        data.insert(0, id)
        id += 1
    with open(r"app/register.json", 'r') as f:
        data = json.load(f)
        tabledata.insert(0, year+" : ")
        if (data[-1][0] == f"{now}/{now+1} : "):
            data[-1] = tabledata
        else:
            data.append(tabledata)
        with open(r'app/r.text', 'w') as f:
            x = time.time()
            f.write(f"{x}")   
        with open(r"app/register.json", 'w') as f:
            json.dump(data, f)
        


  

        
       




#now = time.localtime().tm_year

#https://tr.weatherspark.com/h/d/95434/2015/3/21/21-Mart-2015-Cumartesi-tarihinde-in%C4%B0stanbul-T%C3%BCrkiye-Ortalama-Hava-Durumu#Figures-Daylight

# History-MetarReports-outer_table





def Weather():
    myYear = int(datetime.datetime(2021, 1, 1, 0, 0).timestamp())

    rightNow = int(time.time())
    r = requests.get(f"https://history.openweathermap.org/data/2.5/history/city?lat=38.7219011&lon=35.4873214&appid=af60da058c566f2ba05e1255c1405503")



    r1 = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=Adıyaman,TR&limit=1&appid=af60da058c566f2ba05e1255c1405503")


    cities=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]
    weatherList = []
    if os.path.isfile(r"app/weather.json"):
        with open(r'app/weather.json','r') as f:
            data = json.load(f)
            weatherList = []
            weatherList1 = data
            for city in cities:
                r1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},TR&limit=1&appid=af60da058c566f2ba05e1255c1405503")
                r1 = json.loads(r1.text)    
                lat = r1[0]["lat"]
                lon = r1[0]["lon"] 
                r = requests.get(f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&appid=c6d2e2dc03a74ac5262983aa772c4420")
                r = json.loads(r.text)
                weatherList.append({city:r})
                
            weatherList1.extend(weatherList)    
            with open(r'app/weather.json', 'w') as f:
                json.dump(weatherList1, f)
            with open(r'app/r1.text', 'w') as f:
               x = time.time()
               f.write(f"{x}") 
    else:
        weatherList1 = []
        for city in cities:
            r1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},TR&limit=1&appid=af60da058c566f2ba05e1255c1405503")
            r1 = json.loads(r1.text)     
            lat = r1[0]["lat"]
            lon = r1[0]["lon"] 
            r = requests.get(f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&appid=c6d2e2dc03a74ac5262983aa772c4420")
            r = json.loads(r.text)
            
            weatherList.append({city:r})
        weatherList1.extend(weatherList)
        with open(r'app/weather.json', 'w') as f:
            json.dump(weatherList, f)
        with open(r'app/r1.text', 'w') as f:
            x = time.time()
            f.write(f"{x}")
          

def fetchBot():
    
    print("ok")
    if (not os.path.isfile(r'app/r.text')):
        fetchMatchData(getFirstFixture(), presentMatchData())
    else:
        path = r'app/r.text'
        with open(path,"r",encoding="utf-8") as f:
            
            data = float(f.readline())
            rightNow = time.time()
            myRange = rightNow - data
            if (myRange >= 10800):
                fetchMatchData(getFirstFixture(), presentMatchData())
    if (not os.path.isfile(r"app/r1.text")):
        Weather()
    else:
        path =r"app/r1.text"
        with open(path, "r") as f:
            data = float(f.readline())
            rightNow = time.time()
            rightNow = time.time()
            myRange = rightNow - data        
            if(myRange >=172800):
                Weather()  

