""" __doc__ """

import csv
import datetime

RTN = lambda: "\n"

NUMBER_OF_DAYS = input("This script finds users who haven't logged in in a \
number of days.\nPlease specify a number of days since last login.\n")

USERS_LOGINS = {}

# loop through the contents csv and populate a dictionary
with open('file.csv', 'r') as in_csvfile:
    READER = csv.DictReader(in_csvfile)
    for row in READER:
        email = row['Email Address [Required]']
        last_login = row['Last Sign In [READ ONLY]']
        last_login_obj = datetime.datetime.strptime(last_login, \
        '%m/%d/%y %H:%M')
        delta = datetime.datetime.now() - last_login_obj
        if delta.days > int(NUMBER_OF_DAYS):
            USERS_LOGINS[email] = last_login_obj, delta
        else:
            pass

# if the dictionary populated above has any values, print them
# if not, alert user
if USERS_LOGINS:
    print(RTN())
    for k, v in USERS_LOGINS.items():
        print("user:", k)
        print("last login:", v[0].date())
        print("days since last login:", v[1].days)
        print(RTN())
else:
    print("Each user has logged in within the number of days you specified.")
