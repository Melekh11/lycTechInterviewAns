import datetime
from task3_ans import sort_users  # ваша готовая функция

# вам нужно отсортировать массив так, чтобы даты выводились по возрастанию
# возможно вам поможет эта ссылка: https://proproprogs.ru/python_base/sortirovka-sort-i-sorted
# осталось оолько понять как сравнивать даты!

data = [(datetime.date(2022, 8, 22), 'Петя'), (datetime.date(2020, 3, 5), 'Саша'),
        (datetime.date(2024, 1, 3), 'Маша'), (datetime.date(2022, 8, 23), 'Паша')]


print([user[1] for user in sort_users(data)])  # ['Саша', 'Петя', 'Паша', 'Маша']
