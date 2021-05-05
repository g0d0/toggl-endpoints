# -*- coding: utf-8 -*-

from endpoints.request import request_text

"""
endpoints.projects
=============

Viabiliza a manipulação projetos
"""

def get_workspace_projects(workspace, *argv):
    """
    Informações Pessoais
    =====================

    Obtém lista de projetos do endpoint /projects
    """

    return request_text('GET', 'workspaces/' + str(workspace) + '/projects', *argv)