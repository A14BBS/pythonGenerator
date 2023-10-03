# import names_generator
import names

for i in range(0,10):

     nn1 = names.get_first_name()
     nn2 = names.get_last_name()

     result = nn1 + nn2 + '@gmail.com' # то что ищем
     print(i, result)
# nn = names.get_full_name() # эту переменную запускаем первую ответ должен придти (имя и фамилия)
# print(nn)