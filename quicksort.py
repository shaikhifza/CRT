def quick_sort(arr):
    if len(arr)<=1:
        return arr
    left=[]
    right=[]
    equal=[]
    pvt=arr[-1]
    for i in arr:
        if i<pvt:
            left.append(i)
        elif i>pvt:
            right.append(i)
        else:
            equal.append(i)
    print("pivot:",pvt)
    print("Left sub array:",left)
    print("Right sub array:",right)
    return quick_sort(left)+equal+quick_sort(right)
arr=[23,63,44,57,12,45,36]
sorted_array=quick_sort(arr)
print(sorted_array)
    
