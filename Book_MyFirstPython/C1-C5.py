'''
password_list = ['*#*#', '12345']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print('Login success!')
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print('Your password has changed successfully!')
            account_login()
        else:
            print('Wrong password or invalid input!')
            tries = tries - 1
            account_login()
    else:
        print('Your account has been suspended')
account_login()
'''

# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{} X {} = {}'.format(i, j, i * j))

# import random
# p1 = random.randrange(1, 7)
# p2 = random.randrange(1, 7)
# p3 = random.randrange(1, 7)
#
# print(p1, p2, p3)