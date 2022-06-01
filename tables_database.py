def create():
     import mysql.connector as sqltor

     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764")

     mycur = mydb.cursor()
##     if mydb.is_connected():
##          print("Successfully connected to MySQl Database NAKHEEL")
##     else:
##          print("Not connected to MySQL Database NAKHEEL")

     #----------->CREATING DATABASE AND TABLE

     mycur.execute("DROP DATABASE IF EXISTS NAKHEEL")
     mycur.execute("CREATE DATABASE IF NOT EXISTS Nakheel")
     mycur.execute("USE Nakheel")
     mycur = mydb.cursor()

     ##
     mycur.execute("CREATE TABLE IF NOT EXISTS residentinfo(SNO INT UNIQUE KEY AUTO_INCREMENT,Res_Id VARCHAR(500),Bldg_Id VARCHAR(500),Res_FirstName CHAR(100) NOT NULL,Res_LastName CHAR(100) NOT NULL,Res_Age INT,Res_Gender CHAR(10),Res_Family INT DEFAULT 1, Res_Vehicles INT,Res_Email VARCHAR(100) UNIQUE,Res_Occupation VARCHAR(100),Res_Pno VARCHAR(50) NOT NULL UNIQUE,Res_Type CHAR(10),Res_BldgNo INT,Res_AptNo INT ,Res_Rent FLOAT)")


     mycur.execute("CREATE TABLE IF NOT EXISTS CONSUMPTION(SNO INT UNIQUE KEY AUTO_INCREMENT,Res_Id VARCHAR(500),Bldg_Id VARCHAR (500),Res_FirstName CHAR(100), Res_LastNAme CHAR(100),Res_Pno VARCHAR(50),Elctry_Cons FLOAT, Elctry_Price FLOAT, Water_Cons FLOAT,Water_Price FLOAT, LPG_Cons INT, LPG_Price FLOAT,Total_Res_Cons FLOAT)")

     ##
     mycur.execute(" CREATE TABLE IF NOT EXISTS MAINTENANCE (SNO INT UNIQUE AUTO_INCREMENT,Bldg_Id VARCHAR (500),Res_BldgNo INT,Sec_Guard_Name CHAR(100),Lift_check CHAR(10),Lift_Date DATE,Fire_check CHAR(10),Fire_Date DATE,AC_check CHAR(10),AC_Date DATE,WASTE_CHECK CHAR(10),WASTE_DATE DATE)")


     mycur.execute("CREATE TABLE IF NOT EXISTS COMPLAINT (SNO INT UNIQUE AUTO_INCREMENT,Res_Id VARCHAR(500), Bldg_Id VARCHAR (500),Res_FirstName CHAR(100),Res_LastNAme CHAR(100),Res_Pno VARCHAR(50),Complaint_Type CHAR(20),Res_Complaint CHAR(225),Date_Issued DATE,Complt_Remarks CHAR(225),Date_Resolved DATE)")

     #mycur.execute("DROP TABLE staffinfo")
     mycur.execute("CREATE TABLE IF NOT EXISTS staffinfo(SNO INT UNIQUE AUTO_INCREMENT, S_Id VARCHAR(500) UNIQUE,S_Fname VARCHAR(100), S_Lname VARCHAR(100),S_Desig VARCHAR(500),S_Pno VARCHAR(100),S_email VARCHAR(500), S_address VARCHAR(100), S_salary FLOAT)")


     
     
##     print("Table created")
     #---------->FOR RESIDENT INFO TABLE<=======


     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764")

     mycur = mydb.cursor()



     val = [
     ("R5547","B5424","Fahad","Shah",32,"Male",2,1,"fahad_shah@gmail.com","Exec. Manager","050-9636547","Lessee",5,24,12000),
     ("R2124","B2548","Feng", "Xixi",30,'Female',4,2,'fengxi@gmail.com','Teacher','050-5478124',"Lessee",2,12,13000),
     ("R3896","B3525",'Rahul', 'Jain',43,'Male',5,1,'rahul_jain@gmail.com','ENT specialist','050-2347896','Lessee',3,13,13500),
     ("R4452","B4523",'Fellah','Moumin',35,"Female",3,1,'fellah_1996@gmail.com','Civil Engnr','050-5789452',"Owner",4,19,12000),
     ("R2879",'B2548','Kasid', 'Fedath',42,'Male',5,3,'kasid.f@eim.ae',"Coorporate Lawyer","054-7454879","Lessee",2,5,15000),
     ("R4126",'B4523','Lara','Potts',26,'Female',3,2,'lara_uni@gmail.com','IBM-Intern',"050-8945126","Owner",4,14,12000),
     ("R7648","B7345","Yahed","Ahmed",34,"Male",3,2,'yahed_ah@eim.ae','DEWA engr','056-8475648','Owner',7,20,13000),
     ("R1569","B1689","Reem", "Tahnseen",28,"Female",1,1,"reem_tahseen@gmail.com","Facility Manager","050-2314569",'Owner',1,20,12200),
     ("R3636","B3525",'Sarah','Maria',29,'Female',1,1,'sarah2001@gmail.com','Masters Student','050-78452636','Lessee',3,21,11750),
     ("R4544","B4523",'Tim','Wazowski',33,'Male',1,3,'timmy@hotmail.com','Gen Sales Manager','050-7896544','Owner',4,22,11475),
     ("R6756","B6123","Topsy","Kale",34,"Female",1,2,"topsy@hotmail.com","Free Lancer-Author","056-4578756","Lessee",6,20,12550),
     ("R7649","B7345","Rida","Faheem",45,"Female",1,1,"rida_faheem@gmail.com","Nurse","055-6978649","Lessee",7,14,12000),
     ("R5897",'B5424',"Oum",'Rakesh',42,'Male',1,1,'oum_p1980@hotmail.com','surgeon',"056-2564789","Lessee",5,13,12500)
     ]
     for i in val:
          mycur.execute("USE nakheel")
          a,b,c,d,e,f,g,h,i,j,k,l,m,n,o=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14]
          mycur.execute("INSERT INTO residentinfo (Res_Id,Bldg_Id,Res_FirstName,Res_LastName,Res_Age,Res_Gender,Res_Family, Res_Vehicles,Res_Email,Res_Occupation,Res_Pno,Res_Type,Res_BldgNo,Res_AptNo,Res_Rent) VALUE('{}','{}','{}','{}',{},'{}',{},{},'{}','{}','{}','{}',{},{},{})".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o))                   #------------->ERROR IN THIS LINE
          mydb.commit()
##     print("All records inserted.")


     #----------->FOR CONSUMPTION TABLE<--------------
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764")

     mycur = mydb.cursor()

     val=[
     ("R5547","B5424","Fahad","Shah","050-9636547",1.5,75,300,150,650,500,1050),
     ("R2124","B2548","Feng", "Xixi",'050-5478124',1.8,90,250,125,600,460,1200),
     ("R3896","B3525",'Rahul', 'Jain','0502347896',1.4,70,200,100,675,490,1200),
     ("R4452","B4523",'Fellah','Moumin','050-5789452',1.6,80,275,132.5,620,480,1150),
     ("R2879",'B2548','Kasid', 'Fedath',"054-7454879",1.5,75,300,150,650,475,1200),
     ("R4126",'B4523','Lara','Potts',"050-8945126",1.8,90,260,130,600,460,1100),
     ("R7648","B7345","Yahed","Ahmed",'056-8475648',1.4,70,225,112.5,625,470,1500),
     ("R1569","B1689","Reem", "Tahnseen","050-2314569",1.6,80,230,115,600,460,1200),
     ("R3636","B3525",'Sarah','Maria','050-78452636',1.5,75,250,125,650,475,1250),
     ("R4544","B4523",'Tim','Wazowski','050-7896544',1.3,65,230,115,700,525,1200),
     ("R6756","B6123","Topsy","Kale","056-4578756",1.7,85,245,122.5,650,475,1000),
     ("R7649","B7345","Rida","Faheem","055-6978649",1.6,80,210,105,625,470,1100),
     ("R5897",'B5424',"Oum",'Rakesh',"056-2564789",1.8,90,250,125,700,525,1200)
     ]


     for i in val:
          mycur.execute("USE nakheel")
          a,b,c,d,e,f,g,h,i,j,k,l,=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]
          mycur.execute("INSERT INTO consumption (Res_Id,Bldg_Id ,Res_FirstName, Res_LastNAme ,Res_Pno ,Elctry_Cons , Elctry_Price , Water_Cons ,Water_Price , LPG_Cons , LPG_Price ,Total_Res_Cons) VALUE('{}','{}','{}','{}',{},'{}',{},{},'{}','{}','{}','{}')".format(a,b,c,d,e,f,g,h,i,j,k,l))    
          mydb.commit()
##     print("All records inserted.")



     #-------------> for maintenanace table
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764")

     mycur = mydb.cursor()

     val=[
     ("B1689",1,'Lary Duskin','Done','2020-11-24','Done','2020-08-17','Due','2019-05-04','Done','2020-12-20'),
     ('B2548',2,'Hamanpreet Singh','Due','2019-12-06','Done','2020-11-25','Done','2020-09-18','Due','2019-06-23'),
     ("B3525",3,'Saad Ali','Done','2020-10-04','Done','2020-09-12','Due','2019-03-23','Done','2020-03-12'),
     ("B4523",4,'Reema Javed','Done','2020-05-14','Due','2019-04-24','Done','2020-11-12','Done','2020-06-27'),
     ('B5424',5,'Rayees Khan','Done','2020-08-09','Done','2020-07-26','Due','2019-12-16','Done','2020-07-12'),
     ("B6123",6,'Shaun Bendet', 'Due','2019-05-14','Done','2020-04-24','Done','2020-10-23','Done','2020-10-07'),
     ("B7345",7,'Qareem Taha','Due','2019-11-04','Done','2020-10-13','Done','2020-05-23','Done','2020-10-03'),
     ("B8495",8,'Rafeeq Qader','Done','2020-08-09','Done','2020-07-26','Due','2019-12-16','Done','2020-07-12'),
     ("B9648",9,'Wayn Dams','Due','2019-12-06','Done','2020-11-25','Done','2020-09-18','Due','2019-06-23'),
     ("B10525",10,'Ashley Fily','Done','2020-10-04','Done','2020-09-12','Due','2019-03-23','Done','2020-03-12'),
     ("B11564",11,'Berts John','Done','2020-05-14','Due','2019-04-24','Done','2020-11-12','Done','2020-06-27')]

     for i in val:
          mycur.execute("USE nakheel")
          a,b,c,d,e,f,g,h,i,j,k=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]
          mycur.execute("INSERT INTO MAINTENANCE (Bldg_Id,Res_BldgNo,Sec_Guard_Name,Lift_check ,Lift_Date ,Fire_check ,Fire_Date ,AC_check,AC_Date,WASTE_CHECK,WASTE_DATE ) VALUE('{}',{},'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g,h,i,j,k))                   #------------->ERROR IN THIS LINE
          mydb.commit()
##     print("All records inserted.")


     #------------> for STAFF table
     mydb = sqltor.connect(host="localhost",user="root",password="mysqlpython3.764")

     mycur = mydb.cursor()

     #S_Id ,S_Fname, S_Lname ,S_Desig ,S_Pno,S_email, S_address, S_salary

     val=[
     ("S4234","Falak","Salam","Electrical Engineer","050-5412456","falak@nakheel.ae","12-2213-Jebel Ali" ,13000),
     ("S4134","Elizabeth","Connors","Customer Assistant","050-5651246","eliza@nakheel.ae","45-2353-JLT",12000),
     ("S8465","Susanne","Chu","Manager","055-6578952","susanne@nakheel.ae","98-1312-Barsha",14000),
     ("S5726","Amir","Mohammad","Senior HOD","050-4525895","amir@nakheel.ae","56-4795-Greens",15000),
     ("S3635","David","Grots","Relations Manager","056-6323458","david@nakheel.ae","25-4578-Karama",14000),
     ("S6570","Tim","Heets","Finance Manager","054-5612154","tim@nakheel.ae","56-3245-Qusais",14000),
     ("S5827","Catherine","Joanne","Design Engineer","050-5685478","catherine@nakheel.ae","54-7884-JBR",13000),
     ("S5309","Shafik","Munthal","Civil Engineer","055-6578956","shafik@nakheel.ae","28-5465-Jumeirah",13000),
     ("S9837","Hatim","Abdul","Deputy Head","055-6548326","hatim@nakheel.ae","24-5678-Qudra",15000)]

     for i in val:
          mycur.execute("USE nakheel")
          a,b,c,d,e,f,g,h=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]
          mycur.execute("INSERT INTO staffinfo(S_Id,S_Fname, S_Lname,S_Desig ,S_Pno,S_email, S_address, S_salary) VALUE('{}','{}','{}','{}','{}','{}','{}',{})".format(a,b,c,d,e,f,g,h))                   #------------->ERROR IN THIS LINE
          mydb.commit()
##     print("All records inserted.")



