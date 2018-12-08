from .person import Person


class InvalidRecord(Exception):
    """Raised when a record cannot be parsed correctly"""


def parse_record(record):
    """Parse a string record into a Person object"""
    person_data = _separate_record(record)
    if len(person_data) != 5:
        raise InvalidRecord('Incorrect field count: Expected 5 fields')
    return Person(*person_data)


def _separate_record(record):
    """Parses a record into a list of attributes with leading and trailing
    whitespace stripped"""
    return [r.strip() for r in record.split(_record_separator(record))]


def _record_separator(record):
    """Determines the separator for a given record"""
    if record.count('|') == 4:
        return '|'
    if record.count(',') == 4:
        return ','
    return ' '
