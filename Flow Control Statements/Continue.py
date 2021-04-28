while True:
    print('What is your name')
    name=input()
    if name != 'Ram':
     continue
    print('Hello, Ram. What is your password')
    password  = input()
    if password == 'swordfish':
        break
    else:
        print('Incorrect password, please enter the correct password')

print('Access granted')
