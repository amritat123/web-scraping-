import json
import pprint
from task_1 import movies_data
def group_by_decade():
    year_list=[]
    for i in movies_data:
        if i["year"] not in year_list:
            year_list.append(i["year"])
        # print(year_list)
    my_list=[]
    my_dict={}
    for i in year_list:
        mod=i%10
        dac=i-mod
        #    print(dac
        if  dac not in my_list:
            my_list.append(dac)
            my_dict[dac]=[]
    # print(my_dict)
    for var in my_dict:
        for var1 in movies_data:
            new=str(var)
            new2=str(var1["year"])
            # print(new2,new)
            if new[-2]==new2[-2]:
                my_dict[var].append(var1)
    
    with open ("task_3.json","w") as file:
        json.dump(my_dict,file,indent=3)

group_by_decade()
