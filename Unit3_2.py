nm = input("Введите Ваше имя: ")
snm = input("Введите Вашу фамилию: ")
bd = input("Введите Вашу дату рождения: ")
city = input("Введите Ваш город проживания: ")
email = input("Введите Ваш email: ")
phone_n = input("Введите Ваш телефон: ")


def res_func(nm_f, snm_f, bd_f, city_f, email_f, phone_n_f):
    return print(f"{nm_f} {snm_f}, {bd_f}, {city_f}, {email_f}, {phone_n_f}")


res_func(nm_f=nm, snm_f=snm, bd_f=bd, city_f=city, email_f=email, phone_n_f=phone_n)