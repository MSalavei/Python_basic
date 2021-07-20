n = int(input ("Введите количество наименований товаров, данные о которых Вы хотите сохранить: "))
i = 1
my_ls=[]
ls_name=[]
ls_price=[]
ls_qnt=[]
ls_ed=[]
for l in range(n):
    name_th = input ("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    qnt = int(input("Введите количество товара: "))
    ed = input("Введите единицу измерения: ")
    ls_name.append(name_th)
    ls_name = list(set(ls_name))
    ls_price.append(price)
    ls_price = list(set(ls_price))
    ls_qnt.append(qnt)
    ls_qnt = list(set(ls_qnt))
    ls_ed.append(ed)
    ls_ed=list(set(ls_ed))
    my_tpl = (i,{"название":name_th, "цена":price, "количество":qnt, "eд":ed})
    my_ls.append(my_tpl)
    i+=1
print ("Структура данных товары:")
for el in my_ls:
    print(el)
dict_analysis = {"название":ls_name, "цена":ls_price, "количество":ls_qnt, "eд":ls_ed}
print("Аналитика")
for k, v in dict_analysis.items():
    print(f"{k}: {v}")