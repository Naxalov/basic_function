try:
    from task_5 import fn
except ImportError:
    fn = None
# Create a test to check if function exists
def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'


def test_fn_float_value():
    expected = float
    output = type(fn())
    assert output == expected, 'Function should return an float value'

