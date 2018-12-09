from flask import Flask, request, Response
import json

from .people import People, InvalidPerson
from .person import InvalidDate
from .parser import parse_record, InvalidRecord


app = Flask(__name__)
people = People()


@app.route('/records', methods=['POST'])
def add_person():
    """Adds a person record to the global people object. Expects formatted
    as accepted by parse_record"""
    body = request.get_data(as_text=True)
    people.add_person(parse_record(body))
    return Response(None, mimetype='application/json', status=204)


@app.route('/records/gender', methods=['GET'])
def sort_by_gender():
    return people_response(people.sorted_by_gender())


@app.route('/records/birthdate', methods=['GET'])
def sort_by_birth_date():
    return people_response(people.sorted_by_birth_date())


@app.route('/records/name', methods=['GET'])
def sort_by_last_name():
    return people_response(people.sorted_by_last_name())


def people_response(people):
    data = {'people': [p.to_dict() for p in people]}
    return Response(json.dumps(data), mimetype='application/json')


@app.errorhandler(InvalidRecord)
def invalid_record(e):
    return error_response(e, 400)


@app.errorhandler(InvalidPerson)
def invalid_person(e):
    return error_response(e, 400)


@app.errorhandler(InvalidDate)
def invalid_date(e):
    return error_response(e, 400)


@app.errorhandler(404)
def not_found(_):
    return error_response('Not found', 404)


@app.errorhandler(500)
def exception(e):
    return error_response(e, 500)


def error_response(err, status_code):
    data = {'error': str(err)}
    return Response(json.dumps(data),
                    mimetype='application/json',
                    status=status_code)
