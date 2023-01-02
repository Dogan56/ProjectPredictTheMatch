import json

path = r"C:/Users/sedat/OneDrive/Masaüstü/softwareengineering/app/weather.json"
with open(path,"r") as f:
    data = json.load(f)
    
    