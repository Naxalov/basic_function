try:
    from task_8 import fn
except ImportError:
    fn = None
# Create a test to check if function exists
def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'

def test_fn_args():
    # Get the arguments of the function
    args = fn.__code__.co_varnames
    assert args[0] == 'a', 'Function should take single argument "a"'

def test_fn_returns_2():
    assert fn(1) == 2, 'Function should return 2'
    assert fn(0) == 0, 'Function should return 0'
    assert fn(-1) == -2, 'Function should return -2'