arr = list(map(int, input("Enter array elements: ").split()))
total = 0
for i in range(len(arr)):
    total+=arr[i]
    average =total/len(arr)
print("Average:", average)