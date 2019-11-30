# test_calc.py
import pytest

def inc(x):
  return x + 1
  
def dec(x):
  return x - 1
  
def test_inc():
  assert inc(4) == 5
  
def test_dec():
  assert dec(5) == 4
  
