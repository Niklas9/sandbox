
ASCII_MAX_CHARS = 256

class InvalidInputStringException(Exception):  pass

def is_all_unique(s):
    # NOTE(niklas9):
    # * only ascii input, so max 256 chars
    if s is None or len(s) > ASCII_MAX_CHARS:  return False
    u = [False] * ASCII_MAX_CHARS
    for e in s:
        c = ord(e)
        if not c < ASCII_MAX_CHARS:  raise InvalidInputStringException
        if u[c] == True:  return False
        u[c] = True 
    return True
