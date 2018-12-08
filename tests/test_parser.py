from datetime import date
import pytest

from people_sort.parser import parse_record, InvalidRecord


def test_pipe_delimited():
    parsed = parse_record('Debelak | Peter | M | Orange | 1/1/2018')
    assert parsed.last_name == 'Debelak'
    assert parsed.first_name == 'Peter'
    assert parsed.gender == 'M'
    assert parsed.favorite_color == 'Orange'
    assert parsed.birth_date == date(2018, 1, 1)


def test_comma_delimited():
    parsed = parse_record(' Debelak, Peter, N/A, Light Blue, 12/1/1960')
    assert parsed.last_name == 'Debelak'
    assert parsed.first_name == 'Peter'
    assert parsed.gender == 'N/A'
    assert parsed.favorite_color == 'Light Blue'
    assert parsed.birth_date == date(1960, 12, 1)


def test_space_delimited():
    parsed = parse_record('Debelak Peter F Orange 1/31/2018')
    assert parsed.last_name == 'Debelak'
    assert parsed.first_name == 'Peter'
    assert parsed.gender == 'F'
    assert parsed.favorite_color == 'Orange'
    assert parsed.birth_date == date(2018, 1, 31)


def test_too_few_fields():
    with pytest.raises(InvalidRecord) as ext_info:
        parse_record('Debelak | Peter')
    assert str(ext_info.value) == 'Incorrect field count: Expected 5 fields'


def test_too_many_fields():
    with pytest.raises(InvalidRecord) as ext_info:
        parse_record('Debelak, Lucas, Peter, M, Orange, 1/1/2018')
    assert str(ext_info.value) == 'Incorrect field count: Expected 5 fields'
