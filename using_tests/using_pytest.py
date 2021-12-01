# we run pytest outside of any particular module
# NB pytest will look for functions begining test
def test_Sets():
    assert {1,2,3} == {3,2,1} # same members therefore these sets are the same

def test_thisWillPass():
    assert (1,2,3) == (1,2,3) # same ordinal values, test will pass

def test_thisWillFail():
    assert (1,2,3) == (3,2,1) # different ordinal values, test will fail

