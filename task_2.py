import json
from task_1 import movies_data
a=(movies_data)
def group_by_year(movies):
    emp_dic={}
    for i in movies:
        movie_list=[]
        year=i["year"]
        # print(year)
        if year not in  emp_dic:
            for i in movies:
                # print(year)
                if year==i["year"]:
                    movie_list.append(i)
                    # print(movie_list)
            emp_dic[year]=movie_list
            
    with open("task_2.json","w+")as file:
        json.dump(emp_dic,file,indent=4)

print(group_by_year(a)) 

# from task_1 import movies_data
# import json 
# year_list=[]
# for i in movies_data:
#     if i['year'] not in year_list:
#         year_list.append(i['year'])
# # print(year_list)
# my_list=[]
# dic_1={}
# for i in year_list:
#     modules=i%10
#     # print(modules)
#     dec=i-modules
#     # print(decade)
#     if dec not in my_list:
#         my_list.append(dec)
#         dic_1[dec]=[]
#         # print(dic_1)
# # print(list1)
# # print(dic_1)
# for x in dic_1:
#     for i in movies_data:
#         h=str(x)
#         j=i['year']
#         if h[-2]==j[-2]:
#             dic_1[x].append(i)
# with open("tas_3.json","w") as a:
#     json.dump(dic_1,a,indent=4)




