# -*- coding: utf-8 -*-

from endpoints.toggl import toggl

def request_json(method, route, params={}, *argv):
    response = toggl(method=method, route=route, params=params,).json()

    for arg in argv:
        response = response[arg]

    return response

def request_text(method, route, *argv):
    response = toggl(method=method, route=route).text
