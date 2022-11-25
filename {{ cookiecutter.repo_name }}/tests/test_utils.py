import pytest
import yaml
from src.utils.util import get_conf


@pytest.fixture
def example_yaml():
    return {"a": 1, "b": "2", "c": [3, 4, 5], "d": {6: 7}, "e": True}


def test_get_conf(tmp_path, example_yaml):
    fpath = tmp_path / "tmp.yaml"
    yaml.dump(example_yaml, open(fpath, "w"))
    conf = get_conf(fpath)
    assert conf == example_yaml
