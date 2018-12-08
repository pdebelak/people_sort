from datetime import date
import pytest

from people_sort.person import Person, InvalidDate


def test_person():
    person = Person('Debelak', 'Peter', 'M', 'Orange', '1/2/2018')
    assert person.last_name == 'Debelak'
    assert person.first_name == 'Peter'
    assert person.gender == 'M'
    assert person.favorite_color == 'Orange'
    assert person.birth_date == date(2018, 1, 2)
    assert person.is_valid()
    assert person.error is None


def test_invalid_date():
    person = Person('Debelak', 'Peter', 'M', 'Orange', '2/30/2018')
    assert person.is_valid() is False
    with pytest.raises(InvalidDate):
        person.birth_date


def test_non_date_date():
    person = Person('Debelak', 'Peter', 'M', 'Orange', 'hello')
    assert person.is_valid() is False
    with pytest.raises(InvalidDate):
        person.birth_date


def test_invalid_gender():
    person = Person('Debelak', 'Peter', 'H', 'Orange', '1/2/2018')
    assert person.is_valid() is False
    assert person.error == 'Invalid gender'


def test_missing_last_name():
    person = Person(None, 'Peter', 'M', 'Orange', '1/2/2018')
    assert person.is_valid() is False
    assert person.error == 'Missing required field: last_name'


def test_missing_first_name():
    person = Person('Debelak', '', 'M', 'Orange', '1/2/2018')
    assert person.is_valid() is False
    assert person.error == 'Missing required field: first_name'


def test_missing_gender():
    person = Person('Debelak', 'Peter', None, 'Orange', '1/2/2018')
    assert person.is_valid() is False
    assert person.error == 'Missing required field: gender'


def test_missing_favorite_color():
    person = Person('Debelak', 'Peter', 'M', '', '1/2/2018')
    assert person.is_valid() is False
    assert person.error == 'Missing required field: favorite_color'


def test_missing_birth_date():
    person = Person('Debelak', 'Peter', 'M', 'Orange', None)
    assert person.is_valid() is False
    assert person.error == 'Missing required field: birth_date'
