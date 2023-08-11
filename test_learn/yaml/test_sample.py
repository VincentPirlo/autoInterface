import pytest
import yaml

with open("test_yaml.yml", "r", encoding="utf-8") as f:
    data = yaml.load(stream=f, Loader=yaml.FullLoader)


@pytest.mark.parametrize("caselist", data)
def test_case(caselist):
    print(caselist)
