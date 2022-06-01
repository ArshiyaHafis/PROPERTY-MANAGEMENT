#<--------------------------->To Update Records<----------------------------->
#####################
#resident info table#
#####################

def update_recordres(R_id,ch4):

     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     mycur.execute("SET sql_safe_updates=0")
     
     if ch4.lower() == 'a':
          n = input("Enter the new first name:")
          mycur.execute("UPDATE residentinfo set Res_FirstName='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'b':
          n = input("Enter the new last name:")
          mycur.execute("UPDATE residentinfo set Res_LastName='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'c':
          n = input("Enter the age:")
          mycur.execute("UPDATE residentinfo set Res_Age='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'd':
          n = input("Enter the gender:")
          mycur.execute("UPDATE residentinfo set Res_Gender='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'e':
          n = input("Enter the No of family members:")
          mycur.execute("UPDATE residentinfo set Res_Family='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'f':
          n = input("Enter the No of vehicles:")
          mycur.execute("UPDATE residentinfo set Res_Vehicles='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'g':
          n = input("Enter the new email:")
          mycur.execute("UPDATE residentinfo set Res_Email='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'h':
          n = input("Enter the occupation:")
          mycur.execute("UPDATE residentinfo set Res_Occupation='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'i':
          n = input("Enter the new phone number:")
          mycur.execute("UPDATE residentinfo set Res_Pno='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'j':
          n = input("Enter the Resident type:")
          mycur.execute("UPDATE residentinfo set Res_Type='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'k':
          n = input("Enter the Building No:")
          mycur.execute("UPDATE residentinfo set Res_BldgNo='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'l':
          n = input("Enter the Building Id:")
          mycur.execute("UPDATE residentinfo set Bldg_Id='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'm':
          n = input("Enter the Apartment No:")
          mycur.execute("UPDATE residentinfo set Res_AptNo='{}' where Res_Id='{}' ".format(n,R_id))
          
     else:
          print("Wrong choice entered")
          
     mydb.commit()


####################
#in complaint table#
####################


def update_recordcomp(R_id,ch4):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     mycur.execute("SET sql_safe_updates=0")

     
     if ch4.lower() == 'a':
          n = input("Enter the Cpmplaint remarks:")
          mycur.execute("UPDATE COMPLAINT set Complt_Remarks='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'b':
          n = input("Enter the Date (YYYY/MM/DD) Resolved:")
          mycur.execute("UPDATE COMPLAINT set Date_Resolved='{}' where Res_Id='{}' ".format(n,R_id))
     else:
          print("Wrong choice entered")
          
     mydb.commit()


########################
#maintenance info table#
########################
     
def update_recordmaint(B_id,ch4):
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()


     mycur.execute("SET sql_safe_updates=0")
     
     if ch4.lower() == 'a':
          n = input("Enter the IF Lift check DONE or DUE:")
          mycur.execute("UPDATE MAINTENANCE set Lift_check='{}' where Bldg_Id='{}' ".format(n,B_id))
          
     elif ch4.lower() == 'b':
          n = input("Enter the Date (YYYY/MM/DD) when Lift check Done:")
          mycur.execute("UPDATE MAINTENANCE set Lift_Date='{}' where Bldg_Id='{}' ".format(n,B_id))
          
     elif ch4.lower() == 'c':
          n = input("Enter the IF Fire check DONE or DUE:")
          mycur.execute("UPDATE MAINTENANCE set Fire_check='{}' where Bldg_Id='{}' ".format(n,B_id))
          
     elif ch4.lower() == 'd':
          n = input("Enter the Date (YYYY/MM/DD) when Fire check Done:")
          mycur.execute("UPDATE MAINTENANCE set Fire_Date='{}' where Bldg_Id='{}' ".format(n,B_id))
     elif ch4.lower() == 'e':
          n = input("Enter the IF AC check DONE or DUE:")
          mycur.execute("UPDATE MAINTENANCE set AC_check='{}' where Bldg_Id='{}' ".format(n,B_id))
          
     elif ch4.lower() == 'f':
          n = input("Enter the Date (YYYY/MM/DD) when AC check Done:")
          mycur.execute("UPDATE MAINTENANCE set AC_Date='{}' where Bldg_Id='{}' ".format(n,B_id))
     elif ch4.lower() == 'g':
          n = input("Enter the IF Waste check DONE or DUE:")
          mycur.execute("UPDATE MAINTENANCE set Waste_check='{}' where Bldg_Id='{}' ".format(n,B_id))
          
     elif ch4.lower() == 'h':
          n = input("Enter the Date (YYYY/MM/DD) when Waste check Done:")
          mycur.execute("UPDATE MAINTENANCE set Waste_Date='{}' where Bldg_Id='{}' ".format(n,B_id))
     else:
          print("Wrong choice entered")
          
     mydb.commit()
########################
#comsumption info table#
########################


def update_recordcons(R_id,ch4):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     mycur.execute("SET sql_safe_updates=0")

     
     if ch4.lower() == 'a':
          n = input("Enter the Electricity CONSUMPTION (KW/hr):")
          mycur.execute("UPDATE CONSUMPTION set Elctry_Cons='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'b':
          n = input("Enter the Electricity Price:")
          mycur.execute("UPDATE CONSUMPTION set Elctry_Price='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'c':
          n = input("Enter the Water Consumption (L/hr): ")
          mycur.execute("UPDATE CONSUMPTION set Water_Cons='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'd':
          n = input("Enter the Water Price (Dhs):")
          mycur.execute("UPDATE CONSUMPTION set Water_Price='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'e':
          n = input("Enter the LPG Consumption (gallon):")
          mycur.execute("UPDATE CONSUMPTION set LPG_Cons='{}' where Res_Id='{}' ".format(n,R_id))
          
     elif ch4.lower() == 'f':
          n = input("Enter the LPG Price (Dhs):")
          mycur.execute("UPDATE CONSUMPTION set LPG_Price='{}' where Res_Id='{}' ".format(n,R_id))
     
     else:
          print("Wrong choice entered")

     mydb.commit()

##################
#staff info table#
##################


def update_records(Sid,ch4):

     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()


     mycur.execute("SET sql_safe_updates=0")
     

     if ch4.lower() == 'a':
          n = input("Enter the First Name:")
          mycur.execute("UPDATE staffinfo set S_Fname='{}' where S_Id='{}' ".format(n,Sid))
          
     elif ch4.lower() == 'b':
          n = input("Enter the Last Name:")
          mycur.execute("UPDATE staffinfo set S_Lname='{}' where S_Id='{}' ".format(n,Sid))
          
     elif ch4.lower() == 'c':
          n = input("Enter the Designation: ")
          mycur.execute("UPDATE staffinfo set S_Desig='{}' where S_Id='{}' ".format(n,Sid))
          
     elif ch4.lower() == 'd':
          n = input("Enter the Phone Number:")
          mycur.execute("UPDATE staffinfo set S_Pno='{}' where S_Id='{}' ".format(n,Sid))
          
     elif ch4.lower() == 'e':
          n = input("Enter the Email ID:")
          mycur.execute("UPDATE staffinfo set S_email='{}' where S_Id='{}' ".format(n,Sid))
          
     elif ch4.lower() == 'f':
          n = input("Enter the Address:")
          mycur.execute("UPDATE staffinfo set S_address='{}' where S_Id='{}' ".format(n,Sid))
     elif ch4.lower() == 'g':
          n = input("Enter the Salary:")
          mycur.execute("UPDATE staffinfo set S_salary='{}' where S_Id='{}' ".format(n,Sid))
     
     else:
          print("Wrong choice entered")

     mydb.commit()
