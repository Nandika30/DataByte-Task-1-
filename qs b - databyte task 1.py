import csv
with open (r"C:\Users\Ramadurai\Desktop\Nandika\data_csv.csv","r") as f1:
    r=csv.reader(f1,delimiter=",")
    d={}
    a=0
    for i in r:
        d1={}
        if a==0:
            d1["heading 1"]=i[0]
            d1["heading 2"]=i[1]
            a=1
            d[a]=d1
         elif a!=0:
            d1["name"]=i[0]
            d1["country code"]=i[1]
            a=a+1
            d[a]=d1
    l=[]
    a=0
    for i in d:
        l1=[]
        if a==0:
            a=1
            continue
        elif a!=0:
            m=d[i]["name"]
            n=d[i]["country code"]
            l1=[n,m]
        l.append(l1)        
    l.sort()
    x=input("country code 1 = ")
    y=input("country code 2 = ")
    for i in l:
        if i[0]>x and i[0]<y:
            print(i[0],i[1])
