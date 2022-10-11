# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def Chesk_Predicat(num_1, num_2): # проверяем истинность утверждения в диапозоне между введенными числами        
    for i in range(num_1, num_2 + 1):
        for j in range(num_1, num_2 + 1) :
            for k in range(num_1, num_2 + 1):
                if  not(i or j or k) == (not i and not j and not k):
                    print(f"for x = {i}, y = {j}, z = {k} True")
                else: print(f"for x = {i}, y = {j}, z = {k} False")


num_1 = 0
num_2 = 1

Chesk_Predicat(num_1, num_2)