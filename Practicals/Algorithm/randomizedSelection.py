from random import randrange

def partition(input_array, pivot_index = 0):
    i = 0
    if pivot_index != 0:
        input_array[0], input_array[pivot_index] = input_array[pivot_index], input_array[0]
    for j in range(len(input_array) - 1):
        if input_array[j + 1] < input_array[0]:
            input_array[j + 1],input_array[i + 1] = input_array[i + 1],input_array[j + 1]
            i += 1
    input_array[0], input_array[i] = input_array[i], input_array[0]
    return input_array,i

def RSelect(input_array,k):
    if len(input_array) == 1:
        return input_array[0]
    else:
        xpart = partition(input_array,randrange(len(input_array)))
        input_array = xpart[0] # partitioned array
        j = xpart[1] # pivot index
        if j == k:
            return input_array[j]
        elif j > k:
            return RSelect(input_array[ : j],k)
        else:
            k = k - j - 1
            return RSelect(input_array[(j + 1) : ], k)
        
input_array = [3,1,8,4,7,9]
print("Input array is", input_array)
print("Selected elements are:")

for i in range(len(input_array)):
    print (RSelect(input_array,i))