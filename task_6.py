import json
# from task_5 import movies
with open("task_5.json","r")as file:
    data1=json.load(file)
def analyse_movies_language(movie):
    my_list=[]
    dict1={}
    for a in movie:
        for b in a:
            if b == 'langauge':
                my_list.append(a[b])  
    index=0
    while index<len(my_list):
        i=0
        count=0
        while i<len(my_list):
            if my_list[index]==my_list[i]:
                count=count+1
            i=i+1
        if my_list[index] not in dict1:
            dict1[my_list[index]]=count
        index=index+1
    # print(dict1)
    with open("task_6.json","w") as file:
        json.dump(dict1,file,indent=4)        
analyse_movies_language(data1)







