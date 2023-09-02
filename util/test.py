
class AssertException(Exception):
    pass


def format_message(message):
    return message.replace("\n", "<:LF:>")


def display(type, message, label="", mode=""):
    print("\n<{0}:{1}:{2}>{3}".format(
        type.upper(), mode.upper(), label, format_message(message)), flush=True)


def expect(passed=None, message=None, allow_raise=False):
    if passed:
        display('PASSED', 'Test Passed')
    else:
        message = message or "Value is not what was expected"
        display('FAILED', message)
        if allow_raise:
            raise AssertException(message)


def assert_equals(actual, expected, message=None, allow_raise=False):
    equals_msg = "{0} should equal {1}".format(repr(actual), repr(expected))
    if message is None:
        message = equals_msg
    else:
        message += ": " + equals_msg

    expect(actual == expected, message, allow_raise)


'''
Usage:
@describe('describe text')
def describe1():
    @it('it text')
    def it1():
        # some test cases...
'''