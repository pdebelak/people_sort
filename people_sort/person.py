from datetime import date


class InvalidDate(Exception):
    """Raised when a date cannot be parsed or is otherwise invalid"""


class Person:
    """Person represents a single person record"""
    REQUIRED_FIELDS = {
        'last_name',
        'first_name',
        'gender',
        'favorite_color',
        'birth_date',
    }
    VALID_GENDERS = {'N/A', 'M', 'F'}

    def __init__(self, last_name, first_name, gender, favorite_color,
                 birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.favorite_color = favorite_color
        self.birth_date_str = birth_date
        self.error = None

    def is_valid(self):
        """Returns false and sets error field with details of error"""
        try:
            self.birth_date
        except InvalidDate:
            self.error = 'Invalid birth date'
            return False
        for field in self.REQUIRED_FIELDS:
            if not getattr(self, field):
                self.error = 'Missing required field: {}'.format(field)
                return False
        if self.gender not in self.VALID_GENDERS:
            self.error = 'Invalid gender'
            return False
        return True

    @property
    def birth_date(self):
        """Turns M/D/YYYY date string into a date object"""
        if not self.birth_date_str:
            return None
        try:
            month, day, year = self.birth_date_str.split('/')
            return date(int(year), int(month), int(day))
        except (ValueError, AttributeError):
            raise InvalidDate

    def to_dict(self):
        return dict(
            last_name=self.last_name,
            first_name=self.first_name,
            gender=self.gender,
            favorite_color=self.favorite_color,
            birth_date=self.birth_date.strftime('%-m/%-d/%Y'),
        )
