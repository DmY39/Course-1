# 2. Счастливый ли билет
a = int(input())
b = a//100000 + (a//10000)%10 + ((a//1000)%100)%10;
c = a%10 + a%100//10 + a%1000//100
if b == c: print('Счастливый')
else: print('Обычный')
