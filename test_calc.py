# test_calc.py
import pytest

def inc(x):
  """ Incremenet the value of x
  >>> inc(4)
  5
  """
  return x + 1
  
def dec(x):
  """  Decrement the value of x
  >>> dec(5)
  4
  """
  return x - 1
  
def test_inc():
  assert inc(4) == 5
  
def test_dec():
  assert dec(5) == 4
  
