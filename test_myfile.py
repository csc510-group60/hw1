import pytest
from myfile import div

def test_div_pass():
    assert div(10, 2) == 5 

def test_div_fail():
    assert div(10, 0) == "Infinity"
