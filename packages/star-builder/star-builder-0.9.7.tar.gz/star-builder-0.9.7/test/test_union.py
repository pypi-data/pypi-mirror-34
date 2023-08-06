import pytest

from apistar.exceptions import ValidationError
from star_builder import Type, validators


class Union(Type):
    field = (validators.Array(validators.String()) | validators.String()) \
            << {"allow_null": True}


def test_union1():
    a = Union()
    a.format()
    assert a.field is None
    a.field = ["aaa"]
    assert a.field == ["aaa"]
    a.field = "aaa"
    assert a.field == "aaa"
    with pytest.raises(ValidationError):
        a.field = 1


