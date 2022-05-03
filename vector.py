class Vector:
      def __init__(self, *values):
            self.finite = list(values)
      def __len__(self):
            return len(self.finite)
      def __getitem__(self, key):
            if key < 0:
                  raise IndexError("not valid key '{}'".format(key))
            return self.finite[key] if key < len(self) else 0
      def __setitem__(self, key, value):
            if key < 0:
                  raise IndexError("not valid key '{}'".format(key))
            if key < len(self):
                  self.finite[key] = value
            else:
                  self.finite += [0] * (key - len(self)) + [value]
      def __iter__(self):
            return iter(self.finite)
      def __repr__(self):
            return "Vector: {" + ";".join(repr(e) for e in self) + "}"
      def __str__(self):
            return "<" + ",".join(str(e) for e in self) + ">"
      def __add__(self, other):
            return Vector(*(self[i] + other[i] for i in range(max(len(self), len(other)))))
      def __sub__(self, other):
            return Vector(*(self[i] - other[i] for i in range(max(len(self), len(other)))))
      def __and__(self, other):
            return Vector(*(self[i] & other[i] for i in range(max(len(self), len(other)))))
      def __or__(self, other):
            return Vector(*(self[i] | other[i] for i in range(max(len(self), len(other)))))
      def __xor__(self, other):
            return Vector(*(self[i] ^ other[i] for i in range(max(len(self), len(other)))))
      def __truediv__(self, scalar):
            return Vector(*(self[i] / scalar for i in range(len(self))))
      def __floordiv__(self, scalar):
            return Vector(*(self[i] // scalar for i in range(len(self))))
      def __mul__(self, scalar):
            return Vector(*(self[i] * scalar for i in range(len(self))))
      def __rmul__(self, scalar):
            return self * scalar
      def __mod__(self, scalar):
            return Vector(*(self[i] % scalar for i in range(len(self))))
      def __lshift__(self, scalar):
            return Vector(*(self[i] << scalar for i in range(len(self))))
      def __rshift__(self, scalar):
            return Vector(*(self[i] >> scalar for i in range(len(self))))
      def __pos__(self):
            while len(self.finite) > 0 and self.finite[-1] == 0:
                  self.finite.pop(-1)
            return self
      def __neg__(self):
            return self * (-1)
      def __abs__(self):
            return Vector(*(abs(e) for e in self))
      def __round__(self, ndigits = None):
            return Vector(*(round(e, ndigits)  for e in self))
      def __trunc__(self, ndigits = None):
            return Vector(*(e.__trunc__()  for e in self))
      def __floor__(self, ndigits = None):
            return Vector(*(e.__floor__()  for e in self))
      def __ceil__(self, ndigits = None):
            return Vector(*(e.__ceil__()  for e in self))
      def __eq__(self, other):
            if (len(self) == 1 and self[0] == other) or (len(self) == 0 and other == 0):
                  return True
            if not isinstance(other, Vector):
                  return False
            for i in range(max(len(self), len(other))):
                  if self[i] != other[i]:
                        return False
            return True
      def __ne__(self, other):
            return not (self == other)
      def __invert__(self):
            return sum(e ** 2 for e in self)
