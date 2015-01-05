
# TODO(niklas9):
# * could prob do this one without using any extra space, by returning the last
#   char and remove the first, iterively

def reverse(s):
    if s is None:  return None
    s2 = ''
    # TODO(niklas9):
    # * there's prob a better way to do this, not using xrange but something
    #   else that iterates down instead..
    i = len(s) -1
    for e in s:
        s2 += s[i]
        i = i -1
    return s2
