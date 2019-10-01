""" __doc__ """

import csv
import datetime
from datetime import date, datetime

RTN = lambda: "\n"

TODAY = date.today()

with open('file.csv', 'r') as in_csvfile: # replace 'file.csv' with file name
    READER = csv.DictReader(in_csvfile)
    for row in READER:
        email = row['EMAIL']
        last_login = row['LAST_LOGIN']
        format_str = '%Y-%m-%d' # the format
        last_login_obj = datetime.strptime(last_login, format_str)
        delta = date.today() - last_login_obj.date()
        if delta.days > 29:
            print RTN()
            print "account:", email
            print "days since last login:", delta.days
            print RTN()
