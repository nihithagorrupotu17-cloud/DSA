arr = list(map(int, input("Enter array elements: ").split()))

largest = arr[0]
second_largest = arr[0]

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second largest element:", second_largest)