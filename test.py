import math

def test_sqrt():
    num=25
    assert math.sqrt(num) == 5

def test_square():

    num = 7
    assert num*num == 49

def test_check():

    x = 120
    assert x >=100

def test_multiply():

    x = 5
    y = 5

    assert x*y == 25

def test_fun():
    
    x = 6
    return x+1
    assert x == 6
