from sys import stdout

from .people import People
from .parser import parse_record


class InvalidSort(Exception):
    """Indicates in invalid sorting option"""


SORTS = ['last_name', 'gender', 'birth_date']
OUTPUT_FIELDS = [
    'Last Name',
    'First Name',
    'Gender',
    'Favorite Color',
    'Birth Date']


def sort_file(filename, sort, out=stdout):
    """Sorts the records in filename by the sort argument"""
    people = People()
    with open(filename, 'r') as f:
        for line in f:
            person = parse_record(line)
            people.add_person(person)
    if sort == 'last_name':
        people = people.sorted_by_last_name(reverse=True)
    elif sort == 'gender':
        people = people.sorted_by_gender()
    elif sort == 'birth_date':
        people = people.sorted_by_birth_date()
    else:
        raise InvalidSort('Invalid sort {}'.format(sort))
    for line in formatted_people(people):
        print(line, file=out)


def formatted_people(people):
    """Formats the list of people nicely for terminal output"""
    attribute_lists = [OUTPUT_FIELDS] + [
        [p.last_name, p.first_name, p.gender, p.favorite_color,
         p.birth_date.strftime('%-m/%-d/%Y')]
        for p in people]
    sizes = [2 + max(len(a[i]) for a in attribute_lists)
             for i in range(5)]
    return [_formatted_fields(l, sizes) for l in attribute_lists]


def _formatted_fields(attribute_list, sizes):
    return '|'.join(
        attr.center(sizes[idx]) for idx, attr in enumerate(attribute_list))
