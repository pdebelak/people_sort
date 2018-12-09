import pytest

from people_sort.people import People, InvalidPerson
from people_sort.person import Person


def test_add_person():
    people = People()
    person = Person('Debelak', 'Peter', 'M', 'Orange', '1/1/2018')
    people.add_person(person)
    assert people._people == [person]


def test_add_invalid_person():
    people = People()
    person = Person('Debelak', 'Peter', 'M', 'Orange', '1/41/2018')
    with pytest.raises(InvalidPerson) as ext_info:
        people.add_person(person)
    assert str(ext_info.value) == 'Invalid birth date'


def test_sorting_by_gender():
    person1 = Person('Debelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person2 = Person('Debelak', 'Peter', 'N/A', 'Orange', '1/31/2018')
    person3 = Person('Debelak', 'Peter', 'F', 'Orange', '1/31/2018')
    person4 = Person('Bebelak', 'Peter', 'F', 'Orange', '1/31/2018')
    people = People()
    people.add_person(person1)
    people.add_person(person2)
    people.add_person(person3)
    people.add_person(person4)
    assert people.sorted_by_gender() == [person4, person3, person1, person2]


def test_sorting_by_birth_date():
    person1 = Person('Debelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person2 = Person('Debelak', 'Peter', 'M', 'Orange', '2/1/2018')
    person3 = Person('Debelak', 'Peter', 'M', 'Orange', '1/30/2018')
    person4 = Person('Bebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    people = People()
    people.add_person(person1)
    people.add_person(person2)
    people.add_person(person3)
    people.add_person(person4)
    assert people.sorted_by_birth_date() == [person3, person4, person1,
                                             person2]


def test_sorted_by_last_name():
    person1 = Person('Debelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person2 = Person('Bebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person3 = Person('Aebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person4 = Person('Cebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    people = People()
    people.add_person(person1)
    people.add_person(person2)
    people.add_person(person3)
    people.add_person(person4)
    assert people.sorted_by_last_name() == [person3, person2, person4, person1]


def test_sorted_by_last_name_reversed():
    person1 = Person('Debelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person2 = Person('Bebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person3 = Person('Aebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    person4 = Person('Cebelak', 'Peter', 'M', 'Orange', '1/31/2018')
    people = People()
    people.add_person(person1)
    people.add_person(person2)
    people.add_person(person3)
    people.add_person(person4)
    assert people.sorted_by_last_name(reverse=True) == [
        person1, person4, person2, person3]
