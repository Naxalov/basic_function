try:
    from task_3 import fn
except ImportError:
    fn = None
# Create a test to check if function exists
def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'

def test_fn_returns_codeschool():
    assert fn() == 'CODESCHOOL', 'Function should return "CODESCHOOL"'