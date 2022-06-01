#------------->TO DELETE A RECORD<-----------------------------
#####################
#resident info table#
#####################


def delete_resrecord(R_id):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()
     
     mycur.execute("DELETE  from residentinfo where Res_Id='{}'".format(R_id))
     mydb.commit()

######################
#complaint info table#
######################

def delete_comrecord(R_id):

     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()
     
     mycur.execute("DELETE  from COMPLAINT where Res_Id='{}'".format(R_id))
     mydb.commit()

     
########################
#comsumption info table#
########################


def delete_consrecord(R_id):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()
     
     mycur.execute("DELETE  from CONSUMPTION where Res_Id='{}'".format(R_id))
     mydb.commit()

########################
#maintenance info table#
########################
     

def delete_maintrecord(B_id):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()
     
     mycur.execute("DELETE  from MAINTENANCE where Bldg_Id='{}'".format(B_id))
     mydb.commit()

##################
#staff info table#
##################


def delete_srecord(Sid):
     import mysql.connector as sqltor
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764",database="Nakheel")
     mycur = mydb.cursor()
     
     mycur.execute("DELETE  from staffinfo where S_Id='{}'".format(Sid))
     mydb.commit()
