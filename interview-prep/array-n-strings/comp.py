

NULL = '\x00'

# TODO(niklas9):
# * this should is space O(2n).. could be made in-place
# * string concatenation is usually an time O(n^2) operation, could use
#   string buffers to avoid this

def comp(s):
    if not type(s) == str:  return None
    s += NULL  # add null byte to end
    c = ''
    last_e = None
    count = 0
    for e in s:
        if not e == last_e:
            if count > 1:
                c += str(count)
            if e == NULL:  break
            c += e
            last_e = e
            count = 1
        else:
            count += 1
    if not len(c) < len(s[:-1]):
        return s[:-1]
    return c


def decomp(s):
    if not type(s) == str:  return None
    s2 = ''
    for i, e in enumerate(s):
        if e.isdigit():
            if i == 0:  return None  # can't start with digits
            k = int(e)
            for j in xrange(k-1):
                s2 += s[i-1]
        else:
            s2 += e
    return s2
