# -*- coding: utf-8 -*-

from endpoints.me import get_workspaces
from endpoints.me import me
from endpoints.time_entries import time_entries_in_period
import datetime

entries = time_entries_in_period(start_date='2021-04-01', end_date='2021-04-30')

print('Hi %s, these are yours time entries: ' % me('data', 'fullname'))
print([entry['description'] for entry in entries])