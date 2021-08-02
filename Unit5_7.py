import json
count=0
sum_profit=0
my_dict1={}
my_dict2={}
with open("test5_7.txt", "r") as fl_obj:
    for line in fl_obj:
        firm_name, s, income, outcome = line.split()
        if int(income)-int(outcome)>0:
            count+=1
            sum_profit+=int(income)-int(outcome)
        my_dict1[firm_name]=int(income)-int(outcome)
    average_profit=round(sum_profit/count,0)
    my_dict2["average profit"]=average_profit
    my_ls = []
    my_ls.append(my_dict1)
    my_ls.append(my_dict2)
with open ("test5_6.json", "w") as js_obj:
    json.dump(my_ls, js_obj)