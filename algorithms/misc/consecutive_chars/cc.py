
def cc(s):
    l = len(s)
    i = 0
    while i < (l-1):
        if s[i] == s[i+1]:
            s = s[:i] + s[i+1:]
            l -= 1
        else:
            i += 1
    return s 
