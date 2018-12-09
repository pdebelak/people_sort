People Sort
===========

An application for sorting people.

## Installation

Requires `python3` to be installed.

Install dependencies:

```
$ make deps
```

Run tests:

```
$ make
```

## Usage

From the cli:

```
$ ./sort_people /path/to/filename sort
```

Valid options for `sort` are:

1. `last_name` sorts by last name, descending
2. `gender` sorts by gender, ascending
3. `birth_date` sorts by birth date, ascending

On the server:

```
$ make server
```

Post to `/records` to add a person.

Get to `/records/gender` returns people sorted by gender.

Get to `/records/birthdate` returns people sorted by birth date.

Get to `/records/name` returns people sorted by last name.

All sorts are ascending.
