try:
    from task_1 import fn
except ImportError:
    fn = None
# Create a test to check if function exists
def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'

def test_fn_integer_value():
    expected = int
    output = type(fn())
    assert output == expected, 'Function should return an integer value'