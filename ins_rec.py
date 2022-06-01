#<-------------------------->to insert a new record<----------------------------->

####################
#in complaint table#
####################
def insertcomp(R_id,R_Bid,R_FName,R_LName,R_Pno,R_CMtype,R_Cm,date_i,cm_rem,date_r):

     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     
     #print("values are:",R_id,R_Bid,R_FName,R_LName,R_Pno,R_CMtype,R_Cm,date_i,cm_rem,date_r)
     clause = "INSERT INTO COMPLAINT (Res_Id , Bldg_Id ,Res_FirstName,Res_LastNAme,Res_Pno,Complaint_Type ,Res_Complaint ,Date_Issued ,Complt_Remarks,Date_Resolved) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(R_id,R_Bid,R_FName,R_LName,R_Pno,R_CMtype,R_Cm,date_i,cm_rem,date_r)
     
     #print(val)
     
     try:  
              
          mycur.execute(clause)
          mydb.commit()

          
     except:
          
          mydb.rollback()
          mycur.close()
          mydb.close()
          
     print("The provided records have been added to the table")


#####################
#resident info table#
#####################


def insertres(R_id,R_Bid,R_FName,R_LName,R_Age,R_gen,R_fam,R_Veh,R_Email,R_Occ,R_Pno,R_type,R_bn,R_an,R_rent):

     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     
     #print("values are:",R_id,R_Bid,R_FName,R_LName,R_Age,R_gen,R_fam,R_Veh,R_Email,R_Occ,R_Pno,R_type,R_bn,R_an,R_rent)
     clause = "INSERT INTO residentinfo (Res_Id,Bldg_Id,Res_FirstName ,Res_LastName ,Res_Age ,Res_Gender,Res_Family, Res_Vehicles,Res_Email,Res_Occupation,Res_Pno ,Res_Type,Res_BldgNo,Res_AptNo,Res_Rent) VALUES('{}','{}','{}','{}',{},'{}',{},{},'{}','{}','{}','{}',{},{},{})".format(R_id,R_Bid,R_FName,R_LName,R_Age,R_gen,R_fam,R_Veh,R_Email,R_Occ,R_Pno,R_type,R_bn,R_an,R_rent)
     val = (R_id,R_Bid,R_FName,R_LName,R_Age,R_gen,R_fam,R_Veh,R_Email,R_Occ,R_Pno,R_type,R_bn,R_an,R_rent)
     #print(val)
     
     
     try:  
              
          mycur.execute(clause)
          mydb.commit()

          
     except:
          
          mydb.rollback()
          mycur.close()
          mydb.close()
          
     print("The provided records have been added to the table")


########################
#comsumption info table#
########################


def insertcons(R_id,R_Bid,R_FName,R_LName,R_Pno,R_Elc,R_ElcP,R_Wat,R_WatP,R_LPG,R_LPGP,R_tot):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     
     clause = "INSERT INTO residentinfo (Res_Id ,Bldg_Id ,Res_FirstName , Res_LastNAme,Res_Pno,Elctry_Cons, Elctry_Price, Water_Cons,Water_Price,LPG_Cons, LPG_Price,Total_Res_Cons) VALUES('{}','{}','{}','{}',{},'{}',{},{},'{}','{}','{}','{}')".format(R_id,R_Bid,R_FName,R_LName,R_Pno,R_Elc,R_ElcP,R_Wat,R_WatP,R_LPG,R_LPGP,R_tot)
     val = (R_id,R_Bid,R_FName,R_LName,R_Pno,R_Elc,R_ElcP,R_Wat,R_WatP,R_LPG,R_LPGP,R_tot)
     #print(val)
     
     
     try:  
              
          mycur.execute(clause)
          mydb.commit()

          
     except:
          
          mydb.rollback()
          mycur.close()
          mydb.close()
          
     print("The provided records have been added to the table")


########################
#maintenance info table#
########################
def insertmaint(B_id,B_no,S_GName,L_check,L_date ,F_check,F_date ,AC_check ,AC_date ,W_check ,W_date):
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     
     clause = "INSERT INTO MAINTENANCE(Bldg_Id,Res_BldgNo,Sec_Guard_Name,Lift_check ,Lift_Date ,Fire_check ,Fire_Date ,AC_check,AC_Date,WASTE_CHECK,WASTE_DATE) VALUES ('{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(B_id,B_no,S_GName,L_check,L_date ,F_check,F_date ,AC_check ,AC_date ,W_check ,W_date)
     val = (B_id,B_no,S_GName,L_check,L_date ,F_check,F_date ,AC_check ,AC_date ,W_check ,W_date)
     #print(val)
     
     
     try:  
              
          mycur.execute(clause)
          mydb.commit()

          
     except:
          
          mydb.rollback()
          mycur.close()
          mydb.close()
          
     print("The provided records have been added to the table")


##################
#staff info table#
##################


def inserts_record(Id,fname,lname,desig,pno,email,add,sal):
     
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()

     
     clause = "INSERT INTO staffinfo(S_Id,S_Fname, S_Lname,S_Desig ,S_Pno,S_email, S_address, S_salary) VALUE('{}','{}','{}','{}','{}','{}','{}',{})".format(Id,fname,lname,desig,pno,email,add,sal)
     
     val = (Id,fname,lname,desig,pno,email,add,sal)
     #print(val)
     
     try:  
              
          mycur.execute(clause)
          mydb.commit()

          
     except:
          
          mydb.rollback()
          mycur.close()
          mydb.close()
          
     print("The provided records have been added to the table")
