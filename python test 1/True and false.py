#bool, false, true.
num = 10 < 5
print (num) # Ввывод не правда 10 > 5.
num0 = 10 == 6 # == проверяет что 6=10, он ввыыел не правда.
print (num0)
num1 = 10 != 6 # != проверяет что 6 не равно 10, он ввыыел правда.
print (num1)

#and= и (*), or = или (+).
number = int(input("work number:")) # num__1 = 12.
numb = int(input("work numb:")) # num__0 = 33,66,99.

num__0 = numb % 3 == 0 or numb > 100 # true если число делется на 3 и получает 0.
num__1 = number > 10 and number % 2 == 0 and number <20 # true если число больше 10 и делетца на 2 и равна 0.

#нормальное условие

num3 = int(input("work num_01:"))

if num3 > 10 and num3 // 2 == 0: # условие. Кстати условий можно делать куча.
    print('number больше 10 и четное')
elif num3 % 2 != 0: # ещё условие что число / на 2 не будет = 0.
    print('нечетное')
else:   # если не правильо.
    print('the end!')

print("end")

#not.

nump = True
print(not(nump))
