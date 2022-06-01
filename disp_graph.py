import matplotlib.pyplot as plt

     
def graph():





     import mysql.connector as sqltor
     mydb = sqltor.connect(host = "localhost", user = "root", password = "mysqlpython3.764", database = "Nakheel",port=3306)
     mycur = mydb.cursor()
     res=[]
     elecc=[]
     watp=[]
     lpgp=[]
     mycur.execute("SELECT * from CONSUMPTION")
     info = mycur.fetchall()


     print("Choose from the following to see data:\na)Electricity Consumption\nb) Water Consumption\nc) LPG Consumption\n")
     ch=input()

     
     for i in info:
          
          
          res.append(i[1])
          elecc.append(i[6])
          
          watp.append(i[8])
          
          lpgp.append(i[10])

     
     
     
     if ch=='a':
##          print(res,'\n',elecc)
          plt.title('Electricity Consumption')
          plt.plot(res,elecc)
          plt.xlabel('Resident Id')
          plt.ylabel('Consumption')
          plt.show()
          
     if ch=='b':
##          print(res,'\n',watp)
          plt.title('Water Consumption')
          plt.plot(res,watp)
          plt.xlabel('Resident Id')
          plt.ylabel('Consumption')
          plt.show()
          
     if ch=='c':
##          print(res,'\n',lpgp)
          plt.title('LPG Consumption')
          plt.plot(res,lpgp)
          plt.xlabel('Resident Id')
          plt.ylabel('Consumption')
          plt.show()
       
          
     

     mydb.commit()
     print()  


