def mergesort(seq):
    half=len(seq)//2
    left=seq[0:half]
    right=seq[half:len(seq)]
    left.sort()
    right.sort()
    print(left)
    print(right)
    result=[]
    l=0
    r=0
    while(l<len(left) and r<len(right)):
        if left[l]>right[r]:
            print(right[r])
            result.append(right[r])
            r+=1
        else:
            print(left[l])
            result.append(left[l])
            l+=1
    if l<len(left):
        result.append(left[l])

    if r<len(right):
        result.append(right[r])
    print(result)



m = mergesort([5, 29, 4, 2, 9, 3, 1,344,28])
