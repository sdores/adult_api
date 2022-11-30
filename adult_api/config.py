#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles

import os


# api config
PORT = 5000
HOST = '0.0.0.0'
URL_PREFIX = '/adult/v1'
DEBUG_MODE = True

# model path config
MODEL_PATH = os.getenv('MODEL_PATH', default='./model')  