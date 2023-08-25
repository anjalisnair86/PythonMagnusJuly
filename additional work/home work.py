
from mysql import connector
myDbconnection=connector.connect(host='localhost',user='root',password='root')
print(myDbconnection)


