import sqlite3
class myconnect:
      
      
      def __init__(self):
            #4
            #5
            try :
                  
                  self.conn = sqlite3.connect('emp.db')
                  self.conn.execute('''CREATE TABLE if not exists Student (id INTEGER PRIMARY KEY AUTOINCREMENt,
                                                            name text , 
                                                            email text ,
                                                            mobileno int,
                                                            type text,
                                                            exp int,
                                                            salary int  );''')
                       
            except :
                  pass
                  
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            self.conn.execute("insert into Student values (null,'{}','{}','{}','{}','{}','{}')".format(ename,eemail,emob,etype,eexp,esalary))
            self.conn.commit()


      def display(self):
            #7
            id = int(input("Enter Employee id : "))
            c= self.conn.execute("select * from Student where id = '{}'".format(id))
            result=(c.fetchall())  
            for i in result :
                  print(i[1])
                  print(i[2])
                  print(i[3])
                  print(i[4])
                  print(i[5])
                  print(i[6])
            
      
