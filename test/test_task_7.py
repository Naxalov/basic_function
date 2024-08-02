

try:
    from task_7 import fn
 
except ImportError:
    fn = None

def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'
    
def test_fn_args():
    # Get the arguments of the function
    args = fn.__code__.co_varnames
    assert args[0] == 'a', 'Function should take single argument "a"'
def test_fn_returns_1():
    assert fn(1) == 1, 'Function should return 1'
    assert fn(0) == 0, 'Function should return 0'