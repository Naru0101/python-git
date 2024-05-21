# Пример условного оператора
x = 10
if x > 0:
    print("Число положительное")
elif x == 0:
    print("Число равно нулю")
else:
    print("Число отрицательное")

#Циклы (for, while): 
#Циклы позволяют выполнять блок кода несколько раз.

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

i = 1

while i <= 5:
    print(i)
    i += 1


#Прерывание цикла (break, continue):
#Оператор break используется для прерывания выполнения цикла. 
#Оператор continue используется для пропуска оставшейся части текущей итерации цикла и перехода к следующей итерации.

# Использование оператора break
for i in range(5):
    if i == 3:
        break
    print(i)

# Использование оператора continue

for i in range(5):
    if i == 3:
        continue
    print(i)


