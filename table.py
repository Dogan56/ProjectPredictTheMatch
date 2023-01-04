import json
import os
def getdata():
    headings = ["#","TAKIM","O","G","B","M","A","Y","AV","P","SON 5"]
    path = path = os.path.abspath("register.json").replace("\\","/")
    with open(path,"r") as f:
        data = json.load(f)
        myData = data[-1][1:]
        newData = [i for i in myData]
        
        return headings,newData
