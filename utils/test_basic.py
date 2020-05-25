from utils.friendly_exceptions import *

def test(func):
    """
    Test the function for basic input
    :param func: function definition to be tested
    :return: string output message
    """
    out = "Simple Test OKAY"
    try:
        func([0, 0, 0, 0])
    except Exception as e:
        out = msg(e)
    return out