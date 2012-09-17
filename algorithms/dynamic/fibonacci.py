
# NOTE(nandersson):
# * just did some performance testing for fun compared to C++ variant
#   fibonacci.cc

class Fibonacci(object):

    def __init__(self, n):
        self.n = n

    def get_value(self):
        if self.n < 2:
            v = self.n
        else:
            f1 = Fibonacci(self.n - 1)
            f2 = Fibonacci(self.n - 2)
            v = f1.get_value() + f2.get_value()
        return v


if __name__ == '__main__':
    n = 32
    print 'fibonacci(%d)==%d' % (n, Fibonacci(n).get_value())
