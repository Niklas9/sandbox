#!/usr/bin/python

# NOTE(nandersson):
# * getting the median from two sorted list, A of length n and B of length n+1,
#   this is a requirement since we want an odd number to easily get the middle
#   element (definition of median)

A = [3, 12, 14, 44]
B = [5, 17, 28, 31, 40]

def med(a, b, c):
    C = [a, b, c]
    C.sort()  # O(n log n) worst case
    return C[1]

def median(a, b, n):
    # NOTE(nandersson):
    # * upper bound of O(log n)
    if n < 1:  return None  # silly
    elif n == 1:
        return med(A[a], B[b], B[b+1])  # always O(3*log3) no matter of n
    else:
        k = n/2
        if A[a+k] < B[b+k]:
            return median(a+k, b, k)
        else:
            return median(a, b+k, k)

print median(0, 0, len(A))