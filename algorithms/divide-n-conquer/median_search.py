#!/usr/bin/python

# NOTE(nandersson):
# * getting the median from two sorted list, A of length n and B of length n+1,
#   this is a requirement since we want an odd number to easily get the middle
#   element (definition of median)

A = [3, 12, 14, 44]
B = [5, 17, 28, 31, 40]

def med(a, b, c):
    C = [a, b, c]
    C.sort()
    return C[1]

def median(a, b, n):
    if n < 1:  return None
    elif n == 1:  return med(A[a], B[b], B[b+1])
    else:
        k = n/2
        if A[a+k] < B[b+k]:
            return median(a+k, b, k)
        else:
            return median(a, b+k, k)

print median(0, 0, len(A))