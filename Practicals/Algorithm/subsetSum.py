# A recursive solution for subset sum 

# Returns true if there is a subset  
# of set[] with sun equal to given sum 
def isSubsetSum(set,n, sum) : 
    
    # Base Cases 
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
    
    # If last element is greater than 
    # sum, then ignore it 
    if (set[n - 1] > sum) : 
        return isSubsetSum(set, n - 1, sum); 
   
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]) 
    

set = [3, 34, 4, 12, 5, 2] 
sum = 9
print("Input set is:", set)
print("Target sum is:", sum)
print()

n = len(set) 
if (isSubsetSum(set, n, sum) == True) : 
    print("Found a subset with given sum") 
else : 
    print("No subset with given sum") 
