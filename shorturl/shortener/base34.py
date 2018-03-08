import unittest


characters = 'abcdefghijklmnopqrstuvwxyz23456789'

def encode(num, base=len(characters)):
    """
    takes a number and converts to base30 of characters above
    """

    s = ""
    while num:
        s = characters[num % base] + s
        num //= base
    return s

def decode(num, base=len(characters)):
    values = dict((v, i) for i, v in enumerate(characters))
    power = len(num) - 1
    result = 0
    for char in num:
        result += (values[char] * (base ** power))
        power -= 1
    return result


class TestBase30(unittest.TestCase):

    def test_encode(self):
        num = encode(1)
        self.assertEqual(num, 'b')
        num2 = encode(34)
        self.assertEqual(num2, 'ba')
        num4 = encode(4411)
        self.assertEqual(num4, 'd3z')

    def test_decode(self):
        num = decode('b')
        self.assertEqual(num, 1)
        num2 = decode('ba')
        self.assertEqual(num2, 34)
        num4 = decode('d3z')
        self.assertEqual(num4, 4411)

if __name__ == '__main__':
    unittest.main()
