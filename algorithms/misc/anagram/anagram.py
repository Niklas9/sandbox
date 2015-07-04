
def is_anagram(s1, s2):
    if not len(s1) == len(s2):  return False
    return _get_str_sum(s1) == _get_str_sum(s2)
    
def _get_str_sum(s):
    i = 0
    for c in s:
        i += ord(c)
    return i

assert is_anagram('aab', 'baa')
assert is_anagram('abc', 'cba')
assert is_anagram('github', 'hubgit')
assert not is_anagram('aa', 'a')
assert not is_anagram('abc', 'abd')
assert not is_anagram('abc', 'Abc')  # case sensitive!
