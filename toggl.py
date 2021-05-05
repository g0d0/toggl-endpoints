# -*- coding: utf-8 -*-

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
    auth = HTTPBasicAuth('antoniomquadrosfilho@gmail.com', 'xpto@1234')
    return request(method=method, url='https://api.track.toggl.com/api/v8/' + route, auth=auth)