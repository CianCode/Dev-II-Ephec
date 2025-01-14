class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRE : None (type is verified before setting attributes)
        POST : self.numerator and self.denominator are stored as the most reduced form. Forces usage of both setters for error throwing
        RAISES : ValueError if den = 0
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        self._num = num
        self._den = den
        self.reduce_form()

    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

    def gcd(self, n: int, d: int):
        """
        Uses Euclid's algorithm to compute the GCD used to reduce the fraction form
        PRE : None (type is verified before computing)
        POST : Returns de GCD
        RAISES : TypeError if either argument is not an int
        """
        if not (isinstance(n, int) and isinstance(d, int)):
            raise TypeError("Both parameters of the gcd() method need to be of type int")
        while d != 0:
            n, d = d, n % d
        return abs(n)

    def reduce_form(self):
        d = self.gcd(self._num, self._den)
        self._num //= d
        self._den //= d
        if self._den < 0:
            self._num *= -1
            self._den *= -1

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : returns the reduced form of the fraction
        """
        den = ""
        if self._num % self._den:
            den = f"/{self._den}"
        return f"{self._num}" + den

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number
        A mixed number is the sum of an integer and a proper fraction

        PRE : None
        POST : returns the mixed form of the fraction
        """
        rest = ""
        if self._num % self._den:
            # If there is a rest to the division
            rest = f" and {self._num % self._den}/{self._den}"
        return f"{self._num // self._den}" + rest

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : None
         POST : returns a new instance of Fraction containing the sum of self and other
         RAISES : TypeError if other is not an instance of int or Fraction
         """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = (self._num * other._den) + (other._num * self._den)
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("You can only use Fraction's __add__ operator with another Fraction or int")

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : None
        POST : returns a new instance of Fraction containing the difference of self and other
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = (self._num * other._den) - (other._num * self._den)
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("You can only use Fraction's __sub__ operator with another Fraction or int")

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : None
        POST : returns a new instance of Fraction containing the product of self and other
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(num, den)
        raise TypeError("You can only use Fraction's __mul__ operator with another Fraction or int")

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : None
        POST : returns a new instance of Fraction containing the quotient of self and other
        RAISES : TypeError if other is not an instance of int or Fraction / ValueError if other represents zero
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            if not other._num:
                raise ValueError("You cannot divide a Fraction by 0")
            num = self._num * other._den
            den = self._den * other._num
            return Fraction(num, den)
        raise TypeError("You can only use Fraction's __truediv__ operator with another Fraction or int")

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : None
        POST : returns a new instance of Fraction containing self to the power of other
        RAISES : TypeError if other is not an instance of int or a Fraction representing an int
        """
        if isinstance(other, Fraction) and (not (other._num % other._den)):
            # other is a Fraction representing an integer
            other = int(other._num / other._den)
        if isinstance(other, int):
            if other >= 0:
                num = self._num ** other
                den = self._den ** other
            else:
                num = self._den ** -other
                den = self._num ** -other
            return Fraction(num, den)
        raise TypeError("You can only use Fraction's __pow__ operator with an int or a Fraction representing an int")

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : None
        POST : returns True if the Fraction objects represent the same value, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return (self._num == other._num) and (self._den == other._den)
        raise TypeError("You can only use Fraction's __eq__ operator with another Fraction or int")

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None
        POST : returns the decimal value of the fraction
        """
        return self._num / self._den

    def __ne__(self, other):
        """Overloading of the != operator for fractions

        PRE : None
        POST : returns False if the Fraction objects represent the same value, True if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return not ((self._num == other._num) and (self._den == other._den))
        raise TypeError("You can only use Fraction's __ne__ operator with another Fraction or int")

    def __gt__(self, other):
        """Overloading of the > operator for fractions

        PRE : None
        POST : returns True if self represents a greater number than other, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den > other._num * self._den
        raise TypeError("You can only use Fraction's __gt__ operator with another Fraction or int")

    def __ge__(self, other):
        """Overloading of the >= operator for fractions

        PRE : None
        POST : returns False if self represents a lower number than other, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den >= other._num * self._den
        raise TypeError("You can only use Fraction's __ge__ operator with another Fraction or int")

    def __lt__(self, other):
        """Overloading of the < operator for fractions

        PRE : None
        POST : returns True if self represents a lower number than other, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den < other._num * self._den
        raise TypeError("You can only use Fraction's __lt__ operator with another Fraction or int")

    def __le__(self, other):
        """Overloading of the <= operator for fractions

        PRE : None
        POST : returns False if self represents a greater number than other, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return self._num * other._den <= other._num * self._den
        raise TypeError("You can only use Fraction's __le__ operator with another Fraction or int")

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None
        POST : returns True if the Fraction is equal to 0, False if not
        """
        return self._num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None
        POST : returns True if the Fraction represents an integer
        """
        return self._den == 1  # Works because of the auto reduced form

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None
        POST : returns True if the Fraction represents a value lower than 1
        """
        return float(self) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None
        POST : returns True if the Fraction is equal to 1
        """
        return self._num == self._den  # == 1 because of the auto reduced form

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference between them is a unit fraction

        PRE : None
        POST : returns True if the two values differ by a unit fraction, False if not
        RAISES : TypeError if other is not an instance of int or Fraction
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            return abs((self - other)._num) == 1
            # return (self._den == other._den) and (((self._num - 1) == other._num) or ((self._num + 1) == other._num))
        raise TypeError("You can only use Fraction's is_adjacent_to method with another Fraction or int")
