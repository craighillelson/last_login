""" __doc__ """

import csv
import re
from collections import namedtuple
from datetime import date
from datetime import datetime

RTN = lambda: '\n'

today = date.today()

DAYS_SINCE_LAST_LOGIN = {}

with open('OktaPasswordHealth.csv') as f:
    F_CSV = csv.reader(f)
    HEADERS = [re.sub('[^a-zA-Z_]', '_', h) for h in next(F_CSV)]
    ROW = namedtuple('Row', HEADERS)
    for rows in F_CSV:
        row = ROW(*rows)
        date = datetime.strptime(row.Last_Login, '%Y-%m-%d %H:%M:%S.%f')
        last_login = date.date()
        days_since_last_login = (today - last_login).days
        DAYS_SINCE_LAST_LOGIN[row.User] = days_since_last_login

print(RTN())
print('user, days since last login')
for user, days_since_last_login in sorted(DAYS_SINCE_LAST_LOGIN.items(),
                                          key=lambda x: x[1], reverse=True):
    print(user, days_since_last_login)

with open('days_since_last_login.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(['user','days_since_last_login'])
    for user, days_since_last_login in DAYS_SINCE_LAST_LOGIN.items():
        keys_values = (user, days_since_last_login)
        out_csv.writerow(keys_values)

print(RTN())
print('"days_since_last_login.csv" exported successfully')
print(RTN())
