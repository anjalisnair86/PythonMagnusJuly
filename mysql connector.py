
from mysql import connector
myDbconnection = connector.connect(host='127.0.0.1',user='root',password='root',auth_plugin='mysql_native_password')
print(myDbconnection)


