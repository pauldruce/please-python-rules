import sys
import os 
def test_python_version_is_expected():
    version = os.environ['PYTHON_VERSION']
    ver_nums = version.split('.')
    assert sys.version_info[0] == ver_nums[0]
    assert sys.version_info[1] == ver_nums[1]