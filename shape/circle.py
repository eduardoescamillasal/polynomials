
class Circle:
  def __init__(self, centre, radius):
    self.centre = centre
    self.radius = radius

  def __contains__(self,point):
    [px, py] = point
    [cx, cy] = self.centre
    return (px - cx)**2 + (py - cy)**2 < self.radius**2