arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter target element: "))

for i in arr:
    if i == target:
        print("Element found")
        break
else:
    print("Element not found")