def match(A, B):
    A = set(A)
    B = set(B)
    
    count = 0
    # Iterate through elements in set A
    for i in A:
        # Cheking if the element of B is in A
        if i in B:
            count += 1  
    return count  

# Define two lists
l1 = [3, 2, 4]
l2 = [4, 1, 6]

# Call the function
result = match(l1, l2)
print(result)  # Output 
