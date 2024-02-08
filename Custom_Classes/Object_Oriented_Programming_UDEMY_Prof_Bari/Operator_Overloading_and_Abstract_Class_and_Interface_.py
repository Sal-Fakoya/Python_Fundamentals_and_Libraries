"""
                    OPERATOR OVERLOADING
-->




"""

class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, other):
        s = Rational()
        s.p = self.p * other.q
        s.q = self.q + other.p


















