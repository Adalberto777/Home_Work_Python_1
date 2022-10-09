# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

def Check_Coordinate_Plane (coordinate_plane):
    if coordinate_plane == "1":
        print("x = (0; +бесконечность], у = (0; +бесконечность]") # если я паривльно помню "(" круглая скобка обозначает не включительно а "]" включительно
    elif coordinate_plane == "2":
        print("x = (0; -бесконечность], у = (0; +бесконечность]")
    elif coordinate_plane == "3":
        print("x = (0; -бесконечность], у = (0; -бесконечность]")
    elif coordinate_plane == "4":
        print("x = (0; +бесконечность], у = (0 ; -бесконечность]")
    else:
        print("нет такой плоскости")


print('Enter number of coordinate plane') 
coordinate_plane = input()

Check_Coordinate_Plane (coordinate_plane)