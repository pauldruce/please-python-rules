import sys
def test_python_version_is_expected():
    assert sys.version_info[0] == 3
    assert sys.version_info[1] == 12