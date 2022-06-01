def infores(R_id):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
     mycur.execute("USE nakheel")

     mycur.execute("SELECT * from residentinfo")
     info = mycur.fetchall()
     for i in info:
          if R_id in i:
               flag=True
               break
          else:
               flag=False
     return flag

def infobldgm(B_id):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
     mycur.execute("USE nakheel")

     mycur.execute("SELECT * from MAINTENANCE")
     info = mycur.fetchall()
     for i in info:
          if B_id in i:
               flag=True
               break
          else:
               flag=False
     return flag

def infostaffp(s_pos):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
     mycur.execute("USE nakheel")

     mycur.execute("SELECT * from staffinfo")
     info = mycur.fetchall()
     for i in info:
          if s_pos in i:
               flag=True
               break
          else:
               flag=False
     return flag
def infostaff(Sid):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
     mycur.execute("USE nakheel")

     mycur.execute("SELECT * from staffinfo")
     info = mycur.fetchall()
     for i in info:
          if Sid in i:
               flag=True
               break
          else:
               flag=False
     return flag
