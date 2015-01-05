

class Pixel(object):

    color = None

    def __init__(self, color):
        self.color = color

class NotNxNMatrixException(Exception):  pass

def rot90(m):
    if m is None:  return None
    # NOTE(niklas9):  check that it's a NxN matrix
    last_r_len = None
    for r in m:
        if last_r_len is None:
            last_r_len = len(r)
        if not len(r) == last_r_len:
            raise NotNxNMatrixException
    if not len(m) == last_r_len:
        raise NotNxNMatrixException
    # NOTE(niklas9): rotating a 1x1 matrix doesn't do anything
    if len(m) == 1:  return m
    n = last_r_len
    m2 = [[None] * n] * n
    # TODO(niklas9):
    # * fix this, doesn't work
    for i, r in enumerate(m):
        for j, e in enumerate(r):
            m2[i][n-1] = e
        break
    print repr(m2)
    return m2