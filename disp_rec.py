from prettytable import PrettyTable



#<----------------------------->to display records<---------------------------->

#####################
#resident info table#
#####################




def display_resrecord():
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()

     mycur.execute("USE nakheel")

     mycur.execute("SELECT * from residentinfo")
     print("****************** Resident INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()


     myTable = PrettyTable(["SNO","Res ID","Bldg Id.","First Name","Last Name","Age","Gender","Members","Vehicles","Email","Occupation","Phone No","Res Type","Bldg No","Apt No","Rent"])
     info = mycur.fetchall()
     for i in info:
          myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15]])
          
     mydb.commit()
     print()
     print(myTable)
     

     

########################
#comsumption info table#
########################



def display_consrecord():
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()


     mycur.execute("SELECT * from CONSUMPTION")
     print("****************** CONSUMPTION INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()

     myTable = PrettyTable(["SNO","Res ID","Bldg Id.","First Name","Last Name","Phone No","Elect Cons (KW/hr)","Elect Price (Dhs)","Water Cons (L/hr)","Water Price (Dhs)", "LPG Cons (gallon)","LPG Price (Dhs)", "Total Cons Price"])
     info = mycur.fetchall()
     for i in info:
          myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]])


     print("Legend:\n Cons-Consumption\nElec-Electricity")     
     mydb.commit()
     print()
     print(myTable)


####################
#in complaint table#
####################

def display_comrecord():
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()


     mycur.execute("SELECT * from COMPLAINT")
     print("****************** COMPLAINT INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()


     myTable = PrettyTable(["SNO","Res ID","Bldg Id.","First Name","Last Name","Phone No","Complaint Type","Registered Complaint","Date Issued","Remarks","Date Resolved"])
     
     info = mycur.fetchall()
     for i in info:
          myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
     mydb.commit()
     print()

     print(myTable)

########################
#maintenance info table#
########################

def display_mainrecord():
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()


     mycur.execute("SELECT * from MAINTENANCE")
     print("****************** MAINTENANCE INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()
     myTable = PrettyTable(["SNO","Bldg ID","Bldg No.","Security Guard","Lift Check","Lift Date", "Fire Check","Fire Date","AC Check","AC Date","Waste Check","Waste Date"])
     info = mycur.fetchall()
     for i in info:
          myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]])
     mydb.commit()
     print()
     print(myTable)



     
##################
#staff info table#
##################

     
def display_srecord():
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
#S_Id,S_Fname, S_Lname,S_Desig ,S_Pno,S_email, S_address, S_salary

     mycur.execute("SELECT * from staffinfo")
     print("****************** STAFF INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()
     myTable = PrettyTable(["SNO","Staff ID","First Name","Last Name","Designation","Phone Number","Email ID","Address","Salary"])
     info = mycur.fetchall()
     for i in info:
          myTable.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
     mydb.commit()
     print()
     print(myTable)



     
