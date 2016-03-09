import peewee as pw
import datetime
from hashlib import sha1
from random import randint

from Private.private import password


def SHA(data):
    return sha1(data.encode('utf-8')).hexdigest()

db = pw.MySQLDatabase('LoginUsers', user='Marek', passwd=password)


class LoginUser(pw.Model):
    login = pw.CharField(unique=True, max_length=20, primary_key=True, constraints=pw.Check('login REGEXP "[a-z][0-9]"'))
    first_name = pw.CharField(max_length=20)
    last_name = pw.CharField(max_length=30)
    password = pw.CharField(max_length=40)
    create_date = pw.DateField(default=datetime.date.today)

    class Meta:
        database = db

# db.create_table(LoginUser)
jotto = LoginUser.create(login='JOTTO22412',
                         first_name='Marek',
                         last_name='Czaplicki',
                         password=SHA('JOTTO22412abc123')
                         )
jotto.save()



# user = db.execute('SELECT * FROM loginuser;')
user = db.execute_sql('SELECT * FROM loginuser')
print('\n'.join([str(x) for x in list(user.fetchall())]))

