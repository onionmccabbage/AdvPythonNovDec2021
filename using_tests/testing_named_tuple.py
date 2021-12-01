# invoke pytest like this:
# python -m pytest testing_named_tuple

from collections import namedtuple

task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# we can set defaults for values that may not be provided
task.__new__.__defaults__ = (None, None, False, None)

# write tests to check it behaves as intended
def test_defaults():
    '''using no parameters should invoke the default values'''
    t = task() # use defaults
    s = task(None, None, False, None) # provide values
    assert t == s # the defaults should match the provided values in this case

def test_member_access():
    '''check we can access members of the task using dot notation'''
    t = task('Have Lunch', 'Grace') # other values will be defaults
    assert t.summary == 'Have Lunch'
    assert t.owner   == 'Grace'
    assert (t.done, t.id) == (False, None) # uses the default values