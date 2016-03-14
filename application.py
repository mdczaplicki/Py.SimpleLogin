from Handler import SHA, MySQLHandler as msql


def main():
    choice = input("1. Login User\n2. Register User")
    login = input('Login:')
    password = input('Password:')
    checksum = SHA(login + password)
    logged, registered = bool(), bool()
    if choice == '1':
        logged = msql.log_in(login, checksum)
    elif choice == '2':
        registered = msql.register(login, checksum, input('First name:'), input('Last name:'))
    print('Successfully %s user %s' % ('logged in' if logged else 'registered' if registered else '', login))

if __name__ == '__main__':
    main()
