my_dict={}
fl_obj = open("test5_6.txt", "r", encoding="utf_8_sig")
for line in fl_obj:
    subj, lect_hours, pract_hours, lab_hours = line.split()
    try:
        lh = int(''.join(filter(str.isdigit, lect_hours)))
    except ValueError:
        lh=0
    try:
        ph = int(''.join(filter(str.isdigit, pract_hours)))
    except ValueError:
        ph=0
    try:
        labh = int(''.join(filter(str.isdigit, lab_hours)))
    except ValueError:
        labh = 0
    total_sum = lh + ph + labh
    my_dict[subj[:-1]] = total_sum
print(my_dict)
fl_obj.close()
