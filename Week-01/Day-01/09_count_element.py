arr = list(map(int, input("enter array elements: ").split()))
target = int(input("enter target element:"))
count = 0
for i in arr:
    if i == target:
        count += 1
if count > 0:
    print("Element found", count, "times")
else:
    print("Element not found")
    