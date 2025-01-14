import unittest
from main import Fraction


class FractionTestCase(unittest.TestCase):
    def test_init_int(self):
        """Verifying Fraction initialization and property getters with integers"""
        f1, f2 = Fraction(7, 3), Fraction(21, 6)
        self.assertEqual(f1.numerator, 7)
        self.assertEqual(f1.denominator, 3)
        # Asserting the form is reduced
        self.assertEqual(f2.numerator, 7)
        self.assertEqual(f2.denominator, 2)

    def test_init_wrong_type(self):
        """Verifying Fraction initialization with float numbers or strings"""
        self.assertRaises(TypeError, Fraction, 1, 3.1)
        self.assertRaises(TypeError, Fraction, 2.0, 4)
        self.assertRaises(TypeError, Fraction, "hello", 5)
        self.assertRaises(TypeError, Fraction, 2, "test")

    def test_init_zero(self):
        """Verifying Fraction initialization with zero values"""
        f = Fraction(0, 5)
        self.assertEqual(f.numerator, 0)
        self.assertEqual(f.denominator, 1)
        self.assertRaises(ValueError, Fraction, 12, 0)

    def test_init_negative(self):
        """Verifying Fraction initialization with negative values"""
        f1, f2, f3 = Fraction(-6, 12), Fraction(7, -2), Fraction(-15, -10)
        self.assertEqual(f1.numerator, -1)
        self.assertEqual(f1.denominator, 2)
        self.assertEqual(f2.numerator, -7)
        self.assertEqual(f2.denominator, 2)
        self.assertEqual(f3.numerator, 3)
        self.assertEqual(f3.denominator, 2)

    def test_gcd(self):
        """Verifying gcd computing"""
        f = Fraction(1, 1)
        self.assertEqual(f.gcd(16, 4), 4)
        self.assertEqual(f.gcd(24, 18), 6)
        self.assertEqual(f.gcd(12, -8), 4)
        self.assertEqual(f.gcd(-9, -6), 3)

    def test_str(self):
        """"Verifying the standard string format"""
        self.assertEqual(str(Fraction(8, 2)), "4")
        self.assertEqual(str(Fraction(7, 2)), "7/2")
        self.assertEqual(str(Fraction(18, 16)), "9/8")

    def test_as_mixed_number(self):
        """Verifying the mixed number string format"""
        self.assertEqual(Fraction(7, 2).as_mixed_number(), "3 and 1/2")
        self.assertEqual(Fraction(46, 16).as_mixed_number(), "2 and 7/8")
        self.assertEqual(Fraction(9, 3).as_mixed_number(), "3")

    def test_add(self):
        """"Verifying the overloaded + operator"""
        f1, f2, f3 = Fraction(5, 3), Fraction(12, 4), 8
        f4, f5, f6 = Fraction(-7, 5), Fraction(0, 1), Fraction(1, 7)
        self.assertEqual(f1 + f2, Fraction(14, 3))
        self.assertEqual(f1 + f3, Fraction(29, 3))
        self.assertEqual(f2 + f3, Fraction(11, 1))
        self.assertEqual(f1 + f4, Fraction(8, 15))
        self.assertEqual(f1 + f5, f1)
        self.assertEqual(f1 + f6, Fraction(38, 21))
        self.assertEqual(f4 + f6, Fraction(-48, 35))
        self.assertEqual(f5 + f6, f6)
        with self.assertRaises(TypeError):
            f1 + 5.2

    def test_sub(self):
        """"Verifying the overloaded - operator"""
        f1, f2, f3 = Fraction(4, 6), Fraction(9, 4), 2
        f4, f5, f6 = Fraction(-3, 5), Fraction(0, 1), Fraction(1, 8)
        self.assertEqual(f1 - f2, Fraction(-19, 12))
        self.assertEqual(f2 - f1, Fraction(19, 12))
        self.assertEqual(f1 - f3, Fraction(-4, 3))
        self.assertEqual(f2 - f3, Fraction(1, 4))
        self.assertEqual(f1 - f4, Fraction(38, 30))
        self.assertEqual(f1 - f5, f1)
        self.assertEqual(f1 - f6, Fraction(15, 24))
        self.assertEqual(f5 - f4, Fraction(3, 5))
        with self.assertRaises(TypeError):
            f1 - 5.0

    def test_mul(self):
        """"Verifying the overloaded * operator"""
        f1, f2, f3 = Fraction(6, 5), Fraction(9, 34), -3
        f4, f5, f6 = Fraction(-4, 9), Fraction(0, 1), Fraction(1, 2)
        self.assertEqual(f1 * f2, Fraction(27, 85))
        self.assertEqual(f1 * f3, Fraction(-18, 5))
        self.assertEqual(f2 * f3, Fraction(-27, 34))
        self.assertEqual(f1 * f4, Fraction(-24, 45))
        self.assertEqual(f1 * f5, Fraction(0, 1))
        self.assertEqual(f1 * f6, Fraction(3, 5))
        self.assertEqual(f4 * f6, Fraction(-2, 9))
        self.assertEqual(f5 * f6, Fraction(0, 1))
        with self.assertRaises(TypeError):
            f1 * 1.1

    def test_truediv(self):
        """"Verifying the overloaded / operator"""
        f1, f2, f3 = Fraction(9, 5), Fraction(8, -2), 5
        f4, f5, f6 = Fraction(-3, 7), Fraction(0, 1), Fraction(1, 3)
        self.assertEqual(f1 / f2, Fraction(-9, 20))
        self.assertEqual(f2 / f1, Fraction(-20, 9))
        self.assertEqual(f1 / f3, Fraction(9, 25))
        self.assertEqual(f2 / f3, Fraction(-4, 5))
        self.assertEqual(f1 / f4, Fraction(-21, 5))
        self.assertEqual(f2 / f6, Fraction(-24, 1))
        self.assertEqual(f4 / f6, Fraction(-9, 7))
        self.assertEqual(f1 / f6, Fraction(27, 5))
        with self.assertRaises(ValueError):
            f1 / f5
        with self.assertRaises(TypeError):
            f1 / 2.1

    def test_pow(self):
        """"Verifying the overloaded ** operator"""
        f1, f2 = Fraction(5, 4), Fraction(-4, 2)
        self.assertEqual(f1 ** 3, Fraction(125, 64))
        self.assertEqual(f1 ** -5, Fraction(1024, 3125))
        self.assertEqual(f1 ** f2, Fraction(16, 25))
        self.assertEqual(f2 ** 4, Fraction(16, 1))
        self.assertEqual(f2 ** -3, Fraction(-1, 8))
        with self.assertRaises(TypeError):
            f1 ** 1.2

    def test_eq(self):
        """"Verifying the overloaded == operator"""
        f1, f2, f3 = Fraction(-8, 4), Fraction(18, 38), Fraction(9, 19)
        self.assertFalse(f1 == f2)
        self.assertTrue(f1 == -2)
        self.assertFalse(f1 == f3)
        self.assertTrue(f2 == f3)
        self.assertFalse(f2 == 5)
        with self.assertRaises(TypeError):
            f1 == -2.0

    def test_float(self):
        """"Verifying the float format"""
        f1, f2, f3, f4 = Fraction(5, 6), Fraction(93, 14), Fraction(9, -32), Fraction(-12, -35)
        self.assertEqual(float(f1), 0.8333333333333334)
        self.assertEqual(float(f2), 6.642857142857143)
        self.assertEqual(float(f3), -0.28125)
        self.assertEqual(float(f4), 0.34285714285714286)

    def test_ne(self):
        """"Verifying the overloaded != operator"""
        f1, f2, f3 = Fraction(5, 23), Fraction(12, 6), Fraction(15, 69)
        self.assertTrue(f1 != f2)
        self.assertFalse(f1 != f3)
        self.assertTrue(f2 != f3)
        self.assertFalse(f2 != 2)
        with self.assertRaises(TypeError):
            f1 != 0.8

    def test_gt(self):
        """"Verifying the overloaded > operator"""
        f1, f2, f3 = Fraction(35, 32), Fraction(6, -10), Fraction(-7, -5)
        self.assertTrue(f1 > f2)
        self.assertFalse(f1 > f3)
        self.assertFalse(f2 > f3)
        self.assertFalse(f2 > f1)
        self.assertTrue(f3 > f1)
        self.assertTrue(f3 > f2)
        self.assertTrue(f1 > 1)
        self.assertFalse(f2 > 0)
        self.assertFalse(f3 > 2)
        with self.assertRaises(TypeError):
            f1 > 9.3

    def test_ge(self):
        """"Verifying the overloaded >= operator"""
        f1, f2, f3 = Fraction(9, 3), Fraction(18, 7), Fraction(36, 14)
        self.assertTrue(f1 >= f2)
        self.assertTrue(f1 >= f3)
        self.assertTrue(f2 >= f3)
        self.assertFalse(f2 >= f1)
        self.assertFalse(f3 >= f1)
        self.assertTrue(f3 >= f2)
        self.assertTrue(f1 >= 3)
        self.assertTrue(f2 >= 0)
        self.assertFalse(f3 >= 6)
        with self.assertRaises(TypeError):
            f1 >= 1.8

    def test_lt(self):
        """"Verifying the overloaded < operator"""
        f1, f2, f3 = Fraction(-3, -7), Fraction(12, 9), Fraction(32, 19)
        self.assertTrue(f1 < f2)
        self.assertTrue(f1 < f3)
        self.assertTrue(f2 < f3)
        self.assertFalse(f2 < f1)
        self.assertFalse(f3 < f1)
        self.assertFalse(f3 < f2)
        self.assertTrue(f1 < 1)
        self.assertFalse(f2 < 0)
        self.assertTrue(f3 < 2)
        with self.assertRaises(TypeError):
            f1 < 3.7

    def test_le(self):
        """"Verifying the overloaded <= operator"""
        f1, f2, f3 = Fraction(4, 2), Fraction(10, 5), Fraction(7, 4)
        self.assertTrue(f1 <= f2)
        self.assertFalse(f1 <= f3)
        self.assertFalse(f2 <= f3)
        self.assertTrue(f2 <= f1)
        self.assertTrue(f3 <= f1)
        self.assertTrue(f3 <= f2)
        self.assertTrue(f1 <= 2)
        self.assertFalse(f2 <= 1)
        self.assertTrue(f3 <= 2)
        with self.assertRaises(TypeError):
            f1 <= 1.2

    def test_is_zero(self):
        """Verifying the is_zero() method"""
        f1, f2, f3 = Fraction(0, 7), Fraction(12, 9), Fraction(0, -5)
        self.assertTrue(f1.is_zero())
        self.assertFalse(f2.is_zero())
        self.assertTrue(f3.is_zero())

    def test_is_integer(self):
        """Verifying the is_integer() method"""
        f1, f2, f3 = Fraction(6, 3), Fraction(15, 7), Fraction(-8, 2)
        self.assertTrue(f1.is_integer())
        self.assertFalse(f2.is_integer())
        self.assertTrue(f3.is_integer())

    def test_is_proper(self):
        """Verifying the is_proper() method"""
        f1, f2, f3 = Fraction(3, 7), Fraction(10, 3), Fraction(-5, 9)
        self.assertTrue(f1.is_proper())
        self.assertFalse(f2.is_proper())
        self.assertTrue(f3.is_proper())

    def test_is_unit(self):
        """Verifying the is_unit() method"""
        f1, f2, f3 = Fraction(1, 3), Fraction(1, 1), Fraction(-1, 1)
        self.assertFalse(f1.is_unit())
        self.assertTrue(f2.is_unit())
        self.assertFalse(f3.is_unit())

    def test_is_adjacent_to(self):
        """Verifying the is_adjacent_to() method"""
        f1, f2, f3 = Fraction(4, 2), Fraction(7, 4), Fraction(5, 2)
        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertTrue(f1.is_adjacent_to(f3))
        self.assertFalse(f2.is_adjacent_to(f3))
        self.assertTrue(f2.is_adjacent_to(f1))
        self.assertTrue(f3.is_adjacent_to(f1))
        self.assertFalse(f3.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(2))
        self.assertTrue(f2.is_adjacent_to(2))
        self.assertTrue(f3.is_adjacent_to(3))
        with self.assertRaises(TypeError):
            f1.is_adjacent_to(4.2)


if __name__ == "__main__":
    unittest.main()
