import argparse
import datetime
import getpass
import requests


def get_arg():
    parser = argparse.ArgumentParser(description='Get PR(Pull Request) '
                                     'statistics from GitHub')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')
    parser.add_argument('-n', '--number of days', action="store_true",
                        dest='n', help='show number of days')
    parser.add_argument('-u', '--user', action="store_true",
                        dest='u', help='show user')
    parser.add_argument('-d', '--day', action="store_true",
                        dest='d', help='day of the week')
    parser.add_argument('-H', '--hour', action="store_true",
                        dest='h', help='hour of the day')
    parser.add_argument('-w', '--number', action="store_true",
                        dest='w', help='number of weeks')
    parser.add_argument(metavar='<user>', type=str,
                        dest='user', help='login')
    parser.add_argument(metavar='<repo>', type=str,
                        dest='repo', help='repository ')
    args = parser.parse_args().__dict__
    return args


def get_getapi(username, rep):
    p = getpass.getpass()
    result = requests.get('https://api.github.com/repos/'
                          'alenaPy/{0}/pulls?'
                          'page=1&per_page=100'.format(rep),
                          auth=(username, p))
    return result.json()


def take_day_opened(data):
    for k in data:
        m = k["created_at"]
        print(
        'User: ', k['user']['login'],
        '\n Day opened:k6 ',
        datetime.datetime.strptime(str(m),'%Y-%m-%dT%H:%M:%SZ').strftime('%A'))


def take_hour_opened(data):
    for k in data:
        print('User: ', k['user']['login'],
              '\n Hour opened: ',
              datetime.datetime.strptime(str(k["created_at"]),
                                         '%Y-%m-%dT%H:%M:%SZ').strftime('%H'))


def take_week_opened(data):
    for k in data:
        print('User: ', k['user']['login'],
              '\n Week opened: ',
              datetime.datetime.strptime(str(k["created_at"]),
                                         '%Y-%m-%dT%H:%M:%SZ').strftime('%V'))


def user_who_opened(data):
    for k in data:
        print('User: ', k['user']['login'])


def number_of_days_opened(data):
    for k in data:
        print('User: ', k['user']['login'],
              '\n Number of days: ',
              int(datetime.datetime.now().strftime('%j')) -
              int(datetime.datetime.strptime(str(k["cre\
              ated_at"]), '%Y-%m-%dT%H:%M:%SZ').strftime('%j')))


def first():
    arg = get_arg()
    data = get_getapi(arg['user'], arg['repo'])
    if arg['d']:
        take_day_opened(data)
    if arg['h']:
        take_hour_opened(data)
    if arg['w']:
        take_week_opened(data)
    if arg['n']:
        number_of_days_opened(data)
    if arg['u']:
        user_who_opened(data)


first()
