import pytest
from awesome_tool.models import Person

def test_person_requires_name():
    with pytest.raises(ValueError):
        Person()

def test_person_accepts_optional_age():
    p = Person(name="Alice", age=30)
    assert p.name == "Alice"
    assert p.age == 30
