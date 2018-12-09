from operator import attrgetter


class InvalidPerson(Exception):
    """Raises when trying to add an invalid person to a People
    collection"""


class People:
    """Represents a collection of people and is responsible for sorting
    them"""
    def __init__(self):
        self._people = []

    def add_person(self, person):
        """Adds a person to the collection. Ensures only valid people are
        added"""
        if not person.is_valid():
            raise InvalidPerson(person.error)
        self._people.append(person)

    def sorted_by_gender(self):
        return sorted(self._people, key=attrgetter('gender', 'last_name'))

    def sorted_by_birth_date(self):
        return sorted(self._people, key=attrgetter('birth_date', 'last_name'))

    def sorted_by_last_name(self, reverse=False):
        return sorted(self._people, key=attrgetter('last_name'),
                      reverse=reverse)
