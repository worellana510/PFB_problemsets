#!/usr/bin/env python3

num = [101,2,15,22,95,33,2,27,72,15,52]
num.sort()

sum_even = 0
sum_odd = 0
for num in num:
    print(num)
    if num % 2 ==0:
        sum_even = sum_even + num
    else: 
        sum_odd = sum_odd + num

print(f'Sum of even number: {sum_even}\nSum of odds:{sum_odd}')       

        