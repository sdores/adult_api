#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles


from flask_restx import reqparse, inputs
from werkzeug.datastructures import FileStorage


adult_parser = reqparse.RequestParser()
adult_parser.add_argument('picture', location='files', type=FileStorage, required=False)