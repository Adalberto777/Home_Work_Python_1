# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def Check_XY(x, y):
    if(x > 0 and y > 0): 
        print("в плоскости 1");
    if(x > 0 and y < 0): 
        print("в плоскости 4");
    if(x < 0 and y > 0): 
        print("в плоскости 2");
    if(x < 0 and y < 0): 
        print("в плоскости 3");    


print('Enter X') 
x = int(input())

print('Enter Y') 
y = int(input())

Check_XY(x, y)