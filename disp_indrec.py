#<----------------------------->to display individual records<---------------------------->

#####################
#resident info table#
#####################
def display_riesrecord(rid):
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()


     mycur.execute("SELECT * from residentinfo WHERE Res_Id='{}'".format(rid))
     print("****************** Resident INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()


     info = mycur.fetchall()
     for i in info:
          
          print("SNO:",i[0])
          print("Resident ID:",i[1])
          print("Building ID:",i[2])
          print("First Name:",i[3])
          print("Last Name",i[4])
          print("Age:",i[5])
          print("Gender:",i[6])          
          print("No of Family Members:",i[7])
          print("No of Vehicles:",i[8])
          print("Email Address:",i[9])
          
          print("Occupation:",i[10])
          print("Phone Number:",i[11])
          print("Resident Type:",i[12])
          print("Building No:",i[13])
          print("Apartment No:",i[14])
          print("Rent:",i[15])
     

     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     mydb.commit()
     print()  


########################
#comsumption info table#
########################



def display_consirecord(R_id):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()


     mycur.execute("SELECT * from CONSUMPTION WHERE Res_Id='{}'".format(R_id))
     print("****************** CONSUMPTION INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()

     info = mycur.fetchall()
     for i in info:
          print("SNO:",i[0])
          print("Resident ID:",i[1])
          print("Building ID:",i[2])
          print("First Name:",i[3])
          print("Last Name",i[4])
          print("Phone Number",i[5])
          print("Electricity Consumption (KW/hr):",i[6])
          print("Electricity Price (Dhs):",i[7])
          print("Water Consumption (L/hr):",i[8])
          print("Water Price (Dhs):",i[9])
          print("LPG Consumption (gallon):",i[10])
          print("LPG Price (Dhs):",i[11])
          print("Total Consumption Price:",i[12])
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     mydb.commit()
     print()  

##################
#staff info table#
##################


def display_staff(s_pos):
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
     mycur.execute("SELECT * from staffinfo WHERE S_Desig='{}'".format(s_pos))
     print("****************** STAFF INFO TABLE ******************")
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     print()

     info = mycur.fetchall()
     for i in info:
          print("SNO:",i[0])
          print("Staff id:",i[1])
          print("Staff Name:",i[2])
          print("Staff Last name:",i[3])
          print("Staff Designation:",i[4])
          print("Staff phone number:",i[5])
          print("Staff Email id:",i[6])
          print("Staff address:",i[7])
          print("Staff Salary:",i[8])
     print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
     mydb.commit()
     print()  
