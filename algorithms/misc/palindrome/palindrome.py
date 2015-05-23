

class Palindrome(object):

    @staticmethod
    def get_longest_out_of_str(s):
        s = Palindrome._remove_ws(s)
        s = s.lower()
        max_len = 0
        max_palindorme = ''
        for i in xrange(len(s)):
            for j in xrange(len(s)):
                v = s[i:i + len(s) - j]
                if Palindrome.is_valid(v):
                    if len(v) > max_len:
                        max_len = len(v)
                        max_palindrome = v
        if max_len == 0:  return None
        return max_palindrome

    @staticmethod
    def is_valid(l):
        length = len(l)
        if length == 0:  return False
        for i in xrange(length):
            j = -i
            if not l[i] == l[j-1]:
                return False
        return True

    @staticmethod
    def _remove_ws(l):
        return ''.join([s for s in l if not s == ' '])
