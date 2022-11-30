#!/usr/bin/python3
# Copyright 2022 Sergio Doreste Buerles
# See LICENSE for details.
# Author: Sergio Doreste Buerles


from flask_limiter import Limiter	
from flask_limiter.util import get_remote_address


limiter = Limiter(	
	key_func=get_remote_address,	
	default_limits=["1000 per hour"]
)