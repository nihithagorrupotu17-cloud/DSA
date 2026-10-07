arr = [10, -5, 0, 7, -2, 0, 8, -9]
count_positive = 0
count_negative = 0
count_zero = 0
for i in arr:
    if i>0:
        count_positive+=1
    elif i<0:
        count_negative+=1
    else:
        count_zero+=1
print("Positive numbers:",count_positive)
print("Negative numbers:",count_negative)
print("Zero numbers:",count_zero)