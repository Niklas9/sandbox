
def isSubstring(s3, s1):
    return s3 in s1


def is_str_rot(s1, s2):
    if not len(s1) == len(s2):  return False
    s3 = get_m(s1, s2)
    if s3 is None:  return False
    return isSubstring(s3, s1)

def get_m(m, f):
    if len(m) == 0:  return None
    if f.find(m) == -1:  return get_m(m[:-1], f)
    return f[len(m):f.find(m)]