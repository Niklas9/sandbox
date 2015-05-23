
import palindrome 


class TestPalindrome(object):

    def test_basics(self):
        pd = palindrome.Palindrome()
        assert pd.is_valid('a')
        assert pd.is_valid('aa')
        assert pd.is_valid('aba')
        assert pd.is_valid('abba')
        assert pd.is_valid('3443')
        assert pd.is_valid('tacocat')
        assert pd.is_valid('1234') == False
        assert pd.is_valid('ab') == False

    def test_remove_ws(self):
        pd = palindrome.Palindrome()
        assert pd._remove_ws('a a') == 'aa'
        assert pd._remove_ws('asdf f d s a  ') == 'asdffdsa'

    def test_full_str(self):
        pd = palindrome.Palindrome()
        m = pd.get_longest_out_of_str
        assert m('aa') == 'aa'
        assert m('abba') == 'abba'
        assert m(' aa ') == 'aa'
        assert m('taco cat') == 'tacocat'
        assert m('A man a plan a canal Panama') == 'amanaplanacanalpanama'
        assert m(' bajs No x in Nixon') == 'noxinnixon'
        assert not m('aaca') == 'aaca'
        assert not m('A man a paln a canal Panama') == 'amanaplanacanalpanama'
