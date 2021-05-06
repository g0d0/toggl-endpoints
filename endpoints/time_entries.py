# -*- coding: utf-8 -*-

from endpoints.request import request_json
import datetime
import re

"""
endpoints.time_entries
=============

Gerenciamento de lançamentos de horas
"""

def time_entries_in_period(start_date, end_date, *argv):
    """
    Horas lançadas
    =====================

    Obtém horas lançadas dado o período do endpoint time_entries?start_date=%&end_date%
    """

    isValidDate = lambda date : re.match('[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}', date) != None

    assert isValidDate(start_date), "Data inicial inválida. Formato aceito: YYYY-mm-dd"
    assert isValidDate(end_date), "Data final é inválida. Formato aceito: YYYY-mm-dd"

    params = {}
    (year, month, day) = start_date.split('-')
    params['start_date'] = datetime.date(year=int(year), month=int(month), day=int(day)).isoformat()

    (year, month, day) = end_date.split('-')
    params['end_date'] = datetime.date(year=int(year), month=int(month), day=int(day)).isoformat()
    
    return request_json('GET', 'time_entries', params=params, *argv)


def get_time_entry_details(id, *argv):
    """
    Detalhes de um lançamento de horas
    =====================

    Obtém detalhes de um lançamento de hora do endpoint time_entries?id=%
    """
    return request_json('GET', 'time_entries/' + str(id), *argv)
