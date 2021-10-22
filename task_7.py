import json
with open ("task_5.json","r") as file:
    data1=json.load(file)

def analyse_movies_directors(movies):
    my_list=[]
    my_dict={}
    for var in movies:
        for b in var:
            if b=="director":
                my_list.append(var[b])

    for index in range(0,len(my_list)):
        count=0
        for i in range(0,len(my_list)):
            if my_list[index]==my_list[i]:
                count+=1
        if my_list[index] not in my_dict:
            my_dict[my_list[index]]=count
            print(my_dict)
            
    with open ("task_7.json","w")as file:
        json.dump(my_dict,file,indent=3)

analyse_movies_directors(data1)




        






