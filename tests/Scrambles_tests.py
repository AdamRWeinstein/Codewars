import util.test as test
from solutions.Scrambles import scramble


def dotest(s1, s2, expected):
    actual = scramble(s1, s2)
    test.assert_equals(actual, expected, f"With\ns1 = \"{s1}\"\ns2 = \"{s2}\"")


def test_case():
    for s1, s2, expected in [
        ('rkqodlw', 'world', True),
        ('cedewaraaossoqqyt', 'codewars', True),
        ('katas', 'steak', False),
        ('scriptjava', 'javascript', True),
        ('scriptingjava', 'javascript', True)
    ]:
        dotest(s1, s2, expected)


def large_test():
    s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
    s2 = "zyxcba" * 9_000
    dotest(s1, s2, True)


test_case()
large_test()
