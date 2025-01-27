n = int(input("Введите значение: "))

sum_of_factorials = 1
curr_factorial = 1
for i in range(2, n + 1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial
print(sum_of_factorials)