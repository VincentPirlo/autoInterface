import pytest
import warnings


def test_demo1():
    print("in test_demo1 ...")
    warnings.warn(SyntaxWarning("warning£¬used to test..."))
    assert 1 == 1
