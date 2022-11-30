#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles


from flask_restx import Api


api = Api(version='1.0',
		  title='mhs-models-api',
		  description="API for serving models developed for MHS sensorization API.")