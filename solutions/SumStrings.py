# Given the string representations of two integers, return the string representation of the sum of those integers.
#
# For example:
#
# sumStrings('1','2') // => '3'
#
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
#
# I have removed the use of BigInteger and BigDecimal in java
#
# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

def sum_strings(x, y):
    x = x.lstrip('0')
    if not len(x):
        x = '0'
    y = y.lstrip('0')
    if not len(y):
        y = '0'
    length = max([len(x), len(y)])
    x = x.zfill(length)
    y = y.zfill(length)
    carryTheOne = False
    result = ""
    for (a, b) in zip(x[::-1],y[::-1]):
        temp = int(a) + int(b)
        if carryTheOne:
            temp += 1
            carryTheOne = False
        if temp > 9:
            carryTheOne = True
            temp -= 10
        result += str(temp)
    if carryTheOne:
        result += "1"
    return result[::-1]