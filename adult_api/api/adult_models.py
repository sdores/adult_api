#!/usr/bin/python3
# Copyright 2022 Francisco Pinto-Santos
# See LICENSE for details.
# Author: Francisco Pinto-Santos (@gandalfran on GitHub)


from flask_restx import fields

from adult_api.api.v1 import api


adult_input_model = api.model('adultInput', {
	'picture': fields.String(description="File used to detect the income", required=False)
}, description="Input model for prediction.")


adult_output_model = api.model('adultOutput', {
	'income': fields.String(description="Predicted income. This can be <= 50 or > 50.", required=True, example='>50')
}, description="Prediction output.")