from io import StringIO
import pytest

from people_sort.cli import formatted_people, sort_file, parse_record, \
    InvalidSort
from people_sort.people import People
from people_sort.person import Person


def test_formatted_people():
    person1 = Person('Debelak', 'Peter', 'M', 'Light Blue', '1/1/2018')
    person2 = Person('Bebelak', 'Peter', 'M', 'Orange', '12/12/2018')
    person3 = Person('Aebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person4 = Person('Cebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    people = People()
    people.add_person(person1)
    people.add_person(person2)
    people.add_person(person3)
    people.add_person(person4)
    formatted = formatted_people(people.sorted_by_last_name())
    assert formatted[0] == \
        ' Last Name | First Name | Gender | Favorite Color | Birth Date '
    assert formatted[1] == \
        '  Aebelak  |   Peter    |   M    |     Orange     | 1/31/2018  '
    assert formatted[2] == \
        '  Bebelak  |   Peter    |   M    |     Orange     | 12/12/2018 '
    assert formatted[4] == \
        '  Debelak  |   Peter    |   M    |   Light Blue   |  1/1/2018  '


def parse_output(out):
    """Parses sort_file output back into people record"""
    return [parse_record(l) for l in
            out.getvalue().strip('\n').split('\n')[1:]]


def test_sort_file_last_name():
    filename = 'tests/fixtures/valid.txt'
    out = StringIO()
    sort_file(filename, 'last_name', out=out)
    parsed = parse_output(out)
    assert parsed[0].last_name == 'Debelak'
    assert parsed[1].last_name == 'Cebelak'
    assert parsed[2].last_name == 'Bebelak'
    assert parsed[3].last_name == 'Aebelak'


def test_sort_file_gender():
    filename = 'tests/fixtures/valid.txt'
    out = StringIO()
    sort_file(filename, 'gender', out=out)
    parsed = parse_output(out)
    assert parsed[0].last_name == 'Aebelak'
    assert parsed[1].last_name == 'Bebelak'
    assert parsed[2].last_name == 'Debelak'
    assert parsed[3].last_name == 'Cebelak'


def test_sort_file_birth_date():
    filename = 'tests/fixtures/valid.txt'
    out = StringIO()
    sort_file(filename, 'birth_date', out=out)
    parsed = parse_output(out)
    assert parsed[0].last_name == 'Debelak'
    assert parsed[1].last_name == 'Bebelak'
    assert parsed[2].last_name == 'Cebelak'
    assert parsed[3].last_name == 'Aebelak'


def test_sort_file_invalid_sort():
    filename = 'tests/fixtures/valid.txt'
    with pytest.raises(InvalidSort) as ext_info:
        sort_file(filename, 'birth_name')
    assert str(ext_info.value) == 'Invalid sort birth_name'
