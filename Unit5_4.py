my_dict={"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
file_obj1 = open("test5_4.txt", "r")
file_obj2 = open("test5_4out.txt", "w")
for line in file_obj1:
        my_list = line.split()
        my_list[0] = my_dict[my_list[0]]
        print(" ".join(my_list), file=file_obj2)
file_obj1.close()
file_obj2.close()
