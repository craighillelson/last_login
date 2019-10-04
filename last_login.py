""" __doc__ """

import csv
from datetime import date, datetime

RTN = lambda: "\n"

TODAY = date.today()

NUMBER_OF_DAYS = input("This script finds users who haven't logged in in a \
number of days.\nPlease specify a number of days since last login.\n")

USERS_LOGINS = {}

# loop through the contents csv and populate a dictionary
with open('gg_test_data.csv', 'r') as in_csvfile:
    READER = csv.DictReader(in_csvfile)
    for row in READER:
        email = row['E-MAIL']
        last_login = row['LAST_LOGIN']
        last_login_obj = datetime.strptime(last_login, '%Y-%m-%d')
        delta = date.today() - last_login_obj.date()
        if delta.days > NUMBER_OF_DAYS:
            USERS_LOGINS[email] = last_login_obj
        else:
            pass

# if the dictionary populated above has any values, print them
# if not, alert user
if USERS_LOGINS:
    print RTN()
    for k, v in USERS_LOGINS.items():
        print "user:", k
        print "last login:", v.date()
        print RTN()
else:
    print "Each user has logged in within the number of days you specified."
