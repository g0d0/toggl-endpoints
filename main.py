# -*- coding: utf-8 -*-

from endpoints.me import get_workspaces
from endpoints.me import me
from endpoints.time_entries import time_entries_in_period
from datetime import datetime
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--start-date', help='Start date')
parser.add_option('-e', '--end-date', help='End date')

(options, args) = parser.parse_args()

TODAY = datetime.today().date()
PTBR_DATE_FORMAT = "%d/%m/%Y"

options.start_date = options.start_date or TODAY.isoformat()
options.end_date = options.end_date or TODAY.isoformat()

def show_entries(entries):
    if len(entries) == 0:
        print('Nothing found')
        return

    sumary_entries = [
        (
            entry['duration'],
            entry['start'],
            entry['description'],
        ) for entry in entries
    ]
    
    for entry in sumary_entries:
        hours = entry[0] / 60 / 60
        print('%.2f hours - %s -  %s' % (hours, entry[1], entry[2]))

try:
    print(
        'Hi %s, i\'m searching your time entries from %s to %s. Please wait.\n...\n'
        % (me('data', 'fullname'), TODAY.strftime(PTBR_DATE_FORMAT), TODAY.strftime(PTBR_DATE_FORMAT))
    )

    entries = time_entries_in_period(start_date=options.start_date, end_date=options.end_date)
    show_entries(entries)
    
except AssertionError as e:
    print(e)
