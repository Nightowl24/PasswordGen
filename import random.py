import random
import json


print('Password Generator')

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-.,:;'\/+-`>?<{""}"
password_list = []

while 1:
    password_len = int(input("How long do you want your password: "))
      
    password_count = int(input("How many passwords do you want: "))
    for x in range(0,password_count):
        password = ''
        for x in range (0,password_len):
            password_char = random.choice(chars)
            password = password + password_char                  
        print("Heres the password:",password)      
        password_list.append(password)
    user = input('Do you want more passwords? yes or no:')
    if user == 'yes':
        continue
    else:
        print ('Good, Im tired')
        print(password_list)
    user = input('Want to export list? yes or no:')
    if user == 'yes':
        with open('PassList.txt', 'w') as f:
            f.write(json.dumps(password_list))
        print('If you want to start again restart the app again.')
        break
      
    elif user == 'no':
        print('Copy and paste it, Go way ')
        exit()
        break
    