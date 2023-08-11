import pytest
import os

class TestLuo:
    def test_add(self):
        a = 2
        b = 3
        sum = a + b
        assert sum == 5


pytest.main(['test_123.py', '-s', '--alluredir', './123', '--clean-alluredir'])
os.system('allure generate ./123 -o ./234 --clean')
