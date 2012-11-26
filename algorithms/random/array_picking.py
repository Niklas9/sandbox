
# NOTE(nandersson):
# * just some random tests of picking an element in a randomized array
#   at random to see after how many times it takes before we find it..
# * results as pre-calculated, n iterations if only picking, and n/2
#   iterations if removing each tried random element
# * the downside of using element removal is that it requires more
#   operations, worst case O(n) just for that process, which makes it
#   way worse

import random


def picking(n, times, remove=False):
    i_average = 0
    ops_average = 0
    a = []
    for j in xrange(times):
        a = random.sample(xrange(n*100), n)
        search_el = random.choice(a)
        i = 0  # iterator
        ops = 0  # operations, for calculation upper bound, O
        i_search = None
        is_found = False
        while not is_found:
            i += 1
            ops += 1
            choice = random.choice(a)
            if search_el == choice:
                is_found = True
            elif remove:
                ops += a.index(choice)
                a.remove(choice)
        i_average += i
        ops_average += ops
   
    i_average /= times
    ops_average /= times
    print 'sampled %d times:' % times
    print '\t%d-length array' % n
    print '\t%d tries on average before randomly hitting right element' % i_average
    print '\t%d operations on average used' % ops_average
    print '\tremove used: %s' % remove


n = 100
times = 10000

picking(n, times)
picking(n, times, remove=True)
