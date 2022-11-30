#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles


import flask
import datetime
import pandas as pd
from flask_restx import Resource


from adult_api.api.v1 import api
from adult_api.core import limiter
from adult_api import logger, config
from adult_api.utils import handle400error, handle404error, handle500error

from adult_api.api.adult_models import *
from adult_api.api.adult_parsers import *
from adult_api.model.adult_service import BeerRecognitionService


adult_ns = api.namespace('model', description='Income recognition model')


service = adultService(model_path=config.MODEL_PATH)


@adult_ns.route('/predict')
class Predict(Resource):


    @api.expect(adult_input_model)
    @api.response(404, 'Data not found')
    @api.response(500, 'Unhandled errors')
    @api.response(400, 'Invalid parameters')
    @api.marshal_with(adult_output_model, code=200, description='OK', as_list=False)
    @limiter.limit('1000000/hour') 
    def post(self):
        
        global service

        logger.info('new request arrived')

        logger.info('performing model prediction')

        try:
            income = service.classify()
        except Exception as e:
            logger.exception(f'Unknown error occurred {e}')
            return handle500error(adult_ns)

        # format results
        result = {
            'income_type': income.upper()
        }

        logger.info('request processed sucessfully')

        return result
