# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def Chesk_Predicat(num_1, num_2):
    print(f"for range from {num_1} to {num_2}")
    for i in range(num_1, num_2 + 1):
        for j in range(num_1, num_2 + 1) :
            for k in range(num_1, num_2 + 1):
                if  - (i * j * k) == (- i) * (- j) * (- k):
                    print(f"for x = {i}, y = {j}, z = {k} True")
                else: print('False')

print('Enter first number')
num_1 = int(input())

print('Enter second number')
num_2 = int(input())

Chesk_Predicat(num_1, num_2)