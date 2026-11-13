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