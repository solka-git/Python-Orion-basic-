# 1. Написати програму яка буде зберігати username і email в файл json.
#     При наявності користувачів перед тим як додати юзера програма повинна перевірити чи не існує на данний момент
#     користувача з таким username і email,
#     якщо існує вивести помилку.

import argparse
import json


class UserNameError(Exception):
    pass


class UserEmailError(Exception):
    pass


parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Your user username")
parser.add_argument("--email", help="Your user email")

args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict['username'] = args.username
if args.email:
    user_dict['email'] = args.email

with open('users.json', 'r') as user_file:
    users_data = json.loads(user_file.readline())

try:
    for user in users_data:
        if user['username'] == user_dict['username']:
            raise UserNameError
        elif user['email'] == user_dict['email']:
            raise UserEmailError

    users_data.append(user_dict)

except UserNameError:
    print("Error! This user already exists.")
except UserEmailError:
    print("Error! A user with this email already exists")


with open('users.json', 'w') as user_file:
    user_file.write(json.dumps(users_data))

