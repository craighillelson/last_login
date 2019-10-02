""" __doc__ """

import csv
from datetime import date, datetime

RTN = lambda: "\n"

TODAY = date.today()

NUMBER_OF_DAYS = input("This script finds users who haven't logged in in a \
number of days. Please specify a number of days.\n")

with open('gg_test_data.csv', 'r') as in_csvfile:
    READER = csv.DictReader(in_csvfile)
    for row in READER:
        email = row['E-MAIL']
        last_login = row['LAST_LOGIN']
        last_login_obj = datetime.strptime(last_login, '%Y-%m-%d')
        delta = date.today() - last_login_obj.date()
        if delta.days > NUMBER_OF_DAYS:
            print RTN()
            print "account:", email
            print "days since last login:", delta.days
            print RTN()
