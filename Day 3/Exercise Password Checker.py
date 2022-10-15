uname = input('What is your username? ')
pswd = input('What is your password? ')

pswd_len = len(pswd)
hidden_pswd = '*' * pswd_len
# by multiplying the password length with the star sign any other person including the person who inputs will be unable to see the password in words.
# Smart cuz looking at it that probably how most things related to password in devices word. New knowledge learned.
print(f'{uname}, your password {hidden_pswd}, is {pswd_len} letter long')
