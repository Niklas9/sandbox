
ASCII_MAX_CHARS = 256

def is_perm(s1, s2):
    if s1 is None or s2 is None:  return False
    if not len(s1) == len(s2):  return False
    return _get_ascii_table_count(s1) == _get_ascii_table_count(s2)

def _get_ascii_table_count(s):
    u = [0] * ASCII_MAX_CHARS
    for e in s:
        c = ord(e)
        # TODO(niklas9):
        # * check here that ord() doesn't return a value above 256, if so it's a
        #   unicode string
        u[c] += 1
    return u
