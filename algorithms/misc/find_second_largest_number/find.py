

class ArrayTooSmallException(Exception):  pass


def find(a):
    if len(a) < 2:  raise ArrayTooSmallException()
    hi = a[0]
    si = a[1]
    if si > hi:
        hi = a[1]
        si = a[0]
    for i in a[2:]:
        if i > hi:
            tmp = hi
            hi = i
            si = tmp
        elif i > si:
            si = e
    return si


assert find([1, 2]) == 1
assert find([192, 29]) == 29
assert find([192, 283, -291, 389, 0]) == 283
assert find([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
