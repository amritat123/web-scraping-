

import json,os
file1=open("task_1.json","r")
data1=json.load(file1)
print(data1)
dict1={}
list1=[]
no = 1
for i in data1:
    link=i['url']
    id=link[-10:-1]
    if os.path.exists(id+".json"):
        print(no,"exist")
        no+=1
    else:
        print(no,"no")
        file2=open(id+".json","w")
        data2=json.dump(i,file2,indent=3)
        file2.close()
        no+=1
print("------------------------------------------------------------------------------------------------")

