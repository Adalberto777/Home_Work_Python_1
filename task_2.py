# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def Chesk_Predicat(num_1, num_2): # проверяем истинность утверждения в диапозоне между введенными числами
    if num_1 <= num_2:
        print(f"for range from {num_1} to {num_2}")
        for i in range(num_1, num_2 + 1):
            for j in range(num_1, num_2 + 1) :
                for k in range(num_1, num_2 + 1):
                    if  - (i * j * k) == (- i) * (- j) * (- k):
                        print(f"for x = {i}, y = {j}, z = {k} True")
                    else: print('False')
    else:
        print(f"for range from {num_2} to {num_1}")
        for i in range(num_2, num_1 + 1):
            for j in range(num_2, num_1 + 1) :
                for k in range(num_2, num_1 + 1):
                    if  - (i * j * k) == (- i) * (- j) * (- k):
                        print(f"for x = {i}, y = {j}, z = {k} True")
                    else: print('False')

print('Enter first number') # вводим первое число дапозона проверки
num_1 = int(input())

print('Enter second number') # вводим первое число дапозона проверки
num_2 = int(input())

Chesk_Predicat(num_1, num_2)