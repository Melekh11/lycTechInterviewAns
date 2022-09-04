from functools import cmp_to_key


def comparator(user):
    return user[0].year * 365 + user[0].month * 30 + user[0].day


def sort_users(data):
    return sorted(data, key=comparator)
