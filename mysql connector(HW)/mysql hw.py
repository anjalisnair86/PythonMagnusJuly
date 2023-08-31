'''
from mysql import connector
myDbconnection = connector.connect(host='127.0.0.1',user='root',password='root',auth_plugin='mysql_native_password',
                                   database='pythonmagnus')
c1=myDbconnection.cursor()
c1.execute("drop table  if exists emp")
c1.execute("create table emp (empno int,ename varchar(20),sal int,deptno int)")
c1.execute("insert into emp values(100,'jfk',1500,10)")
c1.execute("insert into emp values(101,'lmn',2000,20)")

myDbconnection.commit()
myDbconnection.close()
'''

from mysql import connector
myDbconnection = connector.connect(host='127.0.0.1',user='root',password='root',auth_plugin='mysql_native_password',
                                   database='pythonmagnus')
c1=myDbconnection.cursor()
vempno= int(input("enter the empno value: "))
vename=input("enter the ename: ")
vsal=int(input("enter the sal value: "))
vdeptno=int(input("enter the Deptno value: "))
c1.execute("insert into emp(empno,ename,sal,deptno) values(%s,%s,%s,%s)",(vempno,vename,vsal,vdeptno))
myDbconnection.commit()
myDbconnection.close()

