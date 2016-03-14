# Simple login module
#### Usage
Simple Login module used to store user names and their password in database.
#### How?
Username is stored in base in-clear. Passwords are not present in database as-is. Database holds a SHA-1 hash of concatenation of login and password.
#### Technology
* MySQL database
* Python3.4
* peewee as MySQL connector(pymysql)
* hashlib for SHA-1 checksum calculator

#### Table diagram
![alt tag](https://github.com/mdczaplicki/Py.SimpleLogin/blob/master/db_diagram.png)
#### Database dump
<table border="1" style="border-collapse:collapse">
<tr><th>login</th><th>first_name</th><th>last_name</th><th>password</th><th>create_date</th></tr>
<tr><td>jotto_</td><td>Marek</td><td>Czaplicki</td><td>1f9f58e294a70335a971d49cae88d006f66a5f69</td><td>2016-03-14</td></tr>
<tr><td>test1</td><td>Edward</td><td>Nozycoreki</td><td>5c9f97c752304912c9b3429484aa33e21d331969</td><td>2016-03-14</td></tr>
<tr><td>test2</td><td>Janusz</td><td>Kowalski</td><td>e13e27124123361709d747182ef9fa1ffb6ae173</td><td>2016-03-14</td></tr>
<tr><td>test3</td><td>Krzysztof</td><td>Bengalski</td><td>e0b4ed2dbb0789da0378e8948552c847423dad33</td><td>2016-03-14</td></tr>
<tr><td>test4</td><td>Artur</td><td>Barcis</td><td>72dcab12ec4e00e2eb64aed375a65b5d6b765927</td><td>2016-03-14</td></tr>
<tr><td>test5</td><td>Cezary</td><td>Zak</td><td>fd95579625cb9ca52a5027b54b4359d1bff6a102</td><td>2016-03-14</td></tr>
</table>
