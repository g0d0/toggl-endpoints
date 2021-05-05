from endpoints.request import request_json

"""
endpoints.me
=============

Obtém dados pessoais
"""

def me(*argv):
    """
    Informações Pessoais
    =====================

    Obtém informações pessoais do entpoint /me
    """

    return request_json('GET', 'me', {}, *argv)

def get_workspaces(*argv):
    """
    Workspaces
    ==========

    Obtém lista de workspaces do entpoint /me
    """
    return me('data', 'workspaces', *argv)