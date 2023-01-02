import json
def getdata():
    headings = ["#","TAKIM","O","G","B","M","A","Y","AV","P","SON 5"]
    path = r"C:/Users/sedat/OneDrive/Masaüstü/softwareengineering/app/register.json"
    with open(path,"r") as f:
        data = json.load(f)
        myData = data[-1][1:]
        newData = [i for i in myData]
        
        return headings,newData
