from sys import argv, exit

from .cli import sort_file, InvalidSort
from .parser import InvalidRecord
from .people import InvalidPerson


def main():
    """Either run the people_sort server or cli interface to people_sort"""
    if len(argv) < 2:
        print('Usage people_sort [server|filename sort]')
        exit(1)
    if argv[1] == 'server':
        pass
    try:
        if len(argv) != 3:
            print('Usage people_sort filename sort')
            exit(1)
        sort_file(argv[1], argv[2])
    except (InvalidSort, InvalidRecord, InvalidPerson) as e:
        print(e)
        exit(1)


main()
