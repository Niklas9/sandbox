

def zrc(m):
    if m is None:  return None
    ps = []
    for i in xrange(len(m)):
        for j in xrange(len(m[i])):
            if m[i][j] == 0:
                ps.append((i, j))
    M = len(m)
    N = len(m[0])
    for p in ps:
        i, j = p
        for k in xrange(M):
            m[k][j] = 0
        for q in xrange(N):
            m[i][q] = 0
    return m