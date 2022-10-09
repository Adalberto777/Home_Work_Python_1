# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def Check_Day(num_day):
    if (num_day < 1 or num_day > 7):
        print("in week only 7 day's")
    else: 
        if (num_day > 0 and num_day < 6):
            print('no')
        else:
            print('yes')


print('Enter the number day of week')
num_day = int(input())

Check_Day(num_day)



