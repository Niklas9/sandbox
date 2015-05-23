
import cc

class TestConsecutiveChars(object):

    def test_basics(self):
        m = cc.cc
        assert m('aa') == 'a'
        assert m('abba') == 'aba'
        assert m('aabbccddee') == 'abcde'
        assert m('abc') == 'abc'
        assert m('abbc') == 'abc'
        assert m('abcc') == 'abc'
