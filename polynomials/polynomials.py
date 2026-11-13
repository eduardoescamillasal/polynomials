from numbers import Number
class Polynomial:
  def __init__(self, coeffs):
    self.coefficients = coeffs

  def degree(self):
    return len(self.coefficients) - 1
  
  def __str__(self):
    coeffs = self.coefficients
    terms = []

    if coeffs[0]:
      terms.append(str(coeffs[0]))
    if self.degree() > 0 and coeffs[1]:
      terms.append(f"{coeffs[1]}x")

    terms += [f"{'' if c == 1 else c}x^{d}" 
              for d, c in enumerate(coeffs[2:], start=2) if c]
    
    return " + ".join(reversed(terms)) or "0"
  
  def __repr__(self):
    return type(self).__name__ + "(" + repr(self.coefficients) + ")"
  
  def __eq__(self, other):
    return isinstance(other, Polynomial) and self.coefficients == other.coefficients
  
  def __add__(self, other):
    if isinstance(other, Number):
      return Polynomial((self.coefficients[0] + other,)
                        + self.coefficients[1:])
    elif isinstance(other, Polynomial):
      common = min(self.degree(), other.degree()) + 1
      coeffs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                           other.coefficients[:common]))
      coeffs += self.coefficients[common:] + other.coefficients[common:]
      return Polynomial(coeffs)
    else:
      return NotImplemented
    
  def __radd__(self, other):
    return self + other
  
  def __sub__(self, other):
     if isinstance(other, Number):
        return Polynomial((self.coefficients[0] - other,)
                        + self.coefficients[1:])
     elif isinstance(other, Polynomial):
        common = min(self.degree(), other.degree()) + 1
        coeffs = tuple(a - b for a, b in zip(self.coefficients[:common],
                                                 other.coefficients[:common]))
        coeffs += self.coefficients[common:] + tuple(-c for c in other.coefficients[common:])
        return Polynomial(coeffs)
     else:
       return NotImplemented

  def __neg__(self):
    return Polynomial(tuple(-c for c in self.coefficients))

  def __rsub__(self, other):
    if isinstance(other, Number):
      return (-self) + other
    else:
      return NotImplemented

  def __mul__(self, other):
    if isinstance(other, Number):
      return Polynomial(tuple(other * c for c in self.coefficients))
    elif isinstance(other, Polynomial):
      deg = self.degree() + other.degree() + 1
      coeffs = [0] * deg
      for deg1, coeff1 in enumerate(self.coefficients):
        for deg2, coeff2 in enumerate(other.coefficients):
          coeffs[deg1 + deg2] += coeff1 * coeff2
      return Polynomial(tuple(coeffs))
    else:
      return NotImplemented

  def __rmul__(self, other):
    return self * other

  def __pow__(self):
    pass

  def __call__(self, *args, **kwds):
    pass