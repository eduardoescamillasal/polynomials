
import pytest
from polynomials import Polynomial
def test_equality():
  assert Polynomial((0, 1)) == Polynomial((0, 1))

@pytest.mark.parametrize(
  "a, b, expected_sum",
  (((0,), (0,1),(0,1)),
   ((2, 0, 3), (1, 2), (3, 2, 3)),
   ((4, 2), (10, 2, 4), (14, 4, 4)))
)
def test_add(a, b, expected_sum):
  assert Polynomial(a) + Polynomial(b) == Polynomial(expected_sum)

def test_add_scalar():
  assert  3 + Polynomial((2, 1)) == Polynomial((5, 1))

@pytest.mark.parametrize(
    "a, b, expected_sub",
    (
        ((0,), (0, 1), (0, -1)),
        ((2, 0, 3), (1, 2), (1, -2, 3)),
        ((4, 2), (10, 2, 4), (-6, 0, -4)),
    ),
)
def test_sub(a, b, expected_sub):  
    assert Polynomial(a) - Polynomial(b) == Polynomial(expected_sub)

def test_sub_scalar():
  assert 3 - Polynomial((2,1)) == Polynomial((1,-1))

def test_add_unknown():
  with pytest.raises(TypeError):
    Polynomial((1,)) + "frog"