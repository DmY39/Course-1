# 1. Окончания
a = int(input())
if 11 <= a%100 <= 14: print(a, 'программистов')
else:
    if 2 <= a%10 <= 4: print(a, 'программиста')
    elif a%10 == 1: print (a, 'программист')
    else: print(a, 'программистов')
input()
