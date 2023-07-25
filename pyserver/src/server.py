#!/usr/bin/env python3

from flask import Flask, abort, current_app, make_response, send_from_directory
from flask_cors import cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import InternalServerError
import json

from src.config.security import STATE_DB
from src.models.baseresponse import BaseResponse
from src.models.encoder import CustomEncoder
from src.services.aggregator import AggregatorService


app = Flask(__name__)
app.register_blueprint(get_swaggerui_blueprint(
	'/v1/api/docs',
	'http://127.0.0.1:5000/v1/api/docs/openapi.json',
	config = { 'app_name': "RPI Server" }
))


@app.route('/v1/system', methods=['GET'])
@cross_origin(origin='192.168.178.*')
def system() -> BaseResponse:
    try:
        status = AggregatorService.getHardwareStatus()
        return get_response(status)
    except Exception as e:
	    abort(500)

@app.route('/v1/bookmarks', methods=['GET'])
@cross_origin(origin='192.168.178.*')
def bookmarks() -> BaseResponse:
    try:
        bookmakars = AggregatorService.getBookmarks(STATE_DB)
        return get_response(bookmakars)
    except Exception as e:
	    abort(500)

@app.route('/v1/api/docs/openapi.json', methods=['GET'])
@cross_origin(origin='192.168.178.*')
def swagger() -> str:
	json = send_from_directory(app.root_path + '/config', 'openapi.json')
	response = make_response(json, 200)
	response.headers['Content-Type'] = 'application/json'
	return response

@app.errorhandler(InternalServerError)
def page_not_found(error):
	msg = error.message if hasattr(error, 'message') else str(error)
	current_app.logger.exception(
		'Error while processing request: {}'.format(msg))
	return get_response(None, 500, str(error))


def get_response(body, status=200, error=None, content_type='application/json'):
	base_response = BaseResponse(status, error, body)
	response = make_response(json.dumps(base_response, cls=CustomEncoder), status)
	response.headers['Content-Type'] = content_type
	return response
