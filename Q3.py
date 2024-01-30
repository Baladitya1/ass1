def match(A,B):
    A=set(A)
    B=set(B)
    count=0
    for i in A :
        if i in B:
            count=count + 1
    return count

l1 = [3, 2, 4]
l2 = [4, 1, 6]
result = match(l1, l2)
print(result)
