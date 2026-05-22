from calculate import add_func
from calculate import sub_func
from calculate import mut_func

def test_add_func():
    assert add_func(1,2) == 3
    assert add_func(0,0) == 0
    assert add_func(-1,-2) == -3

def test_sub_func():
    assert sub_func(1,2) == -1
    assert sub_func(0,0) == 0
    assert sub_func(-1,-2) == 1

def test_mut_func():
    assert mut_func(1,2) == 2
    assert mut_func(0,0) == 0
    assert mut_func(-1,-2) == 2