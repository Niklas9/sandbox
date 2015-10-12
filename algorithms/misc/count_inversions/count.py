
def get_list_from_file():
    with open('IntegerArray.txt', 'r') as f:
        content = f.read()
    l = []
    for line in content.splitlines():
        l.append(int(line))
    return l

def count_inversions(l):
    count = 0
    for i in xrange(len(l)):
        for j in xrange(i, len(l)):
            if (j+1) >= len(l):  break
            if l[i] > l[j+1]:
                count += 1
    return count


m = count_inversions

assert m([1,2,3,4]) == 0
assert m([1,2,4,3]) == 1
assert m([1,3,5,2,4,6]) == 3

#print count_inversions(get_list_from_file())
