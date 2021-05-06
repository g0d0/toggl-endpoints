# -*- coding: utf-8 -*-

from os import getenv

"""
toggl
=======

Este módulo viabiliza a comunicação mais básica com quaisquer endpoints da API Toggl
"""

from requests import request
from requests.auth import HTTPBasicAuth


def toggl(method, route, params={}):
    """
    toggl.toggl
    ===========

    Viabiliza a comunicação mais básica com quaisquers endpoints da API Toggl
    """

    auth = HTTPBasicAuth(getenv('APP_API_USERNAME'), getenv('APP_API_PASSWORD'))
    return request(method=method, url=getenv('APP_API_URL') + route, auth=auth)