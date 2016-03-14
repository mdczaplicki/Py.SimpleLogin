import peewee as pw
import datetime
from hashlib import sha1
from Exceptions import *

from Private.private import db_name, user, password


def SHA(data):
    return sha1(data.encode('utf-8')).hexdigest()

db = pw.MySQLDatabase(db_name, user=user, passwd=password)


class LoginUser(pw.Model):
    login = pw.CharField(unique=True, max_length=20, primary_key=True)
    first_name = pw.CharField(max_length=20)
    last_name = pw.CharField(max_length=30)
    password = pw.CharField(max_length=40)
    create_date = pw.DateField(default=datetime.date.today, choices=None)

    class Meta:
        database = db


class MySQLHandler:
    @staticmethod
    def register(username, checksum, first, last) -> bool:
        exist = False
        try:
            LoginUser.create(login=username,
                             first_name=first,
                             last_name=last,
                             password=checksum
                             ).save()
        except pw.IntegrityError as ex:
            if ex.args[0] == 1062:
                exist = True
            else:
                raise ex
        finally:
            if exist:
                raise UserAlreadyExistsException('User is already in database')
            return True
        # peewee.IntegrityError: (1062, "Duplicate entry 'dupaa' for key 'PRIMARY'")

    @staticmethod
    def log_in(username, checksum) -> bool:
        count = (LoginUser.select().where(LoginUser.login == username and LoginUser.password == checksum).count())
        if count not in [0, 1]:
            raise RecordsNumberException('Number of records corresponding to this user name is unusual: %s' % count)
        return bool(count)


# MySQLHandler().register('jottoooo', 'abc', 'a', 'a')
# print(SHA('abc'))
