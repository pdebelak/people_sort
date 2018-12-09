from sys import argv, exit

from .api import app
from .cli import sort_file, InvalidSort
from .parser import InvalidRecord
from .people import InvalidPerson


def main():
    """Run the cli interface to people_sort"""
    if len(argv) != 3:
        print('Usage people_sort filename sort')
        exit(1)
    try:
        sort_file(argv[1], argv[2])
    except (InvalidSort, InvalidRecord, InvalidPerson) as e:
        print(e)
        exit(1)


main()
