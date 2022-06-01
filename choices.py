import update_rec as upd
import disp_indrec as ind
import disp_rec as rec
import ins_rec as ins
import del_rec as delt
import information as info
import disp_graph as grp
import user_pass as usp
def program(ch1):
     #<---------------->CLIENT SIDE<--------------------------
     while ch1!='q':
          if ch1.lower() == 'a':
          
               print("WELCOME DEAR CUSTOMERS!!")
               print(" <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)>")
               print()
               print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
               print("a)Resident information")
               print("b)Register complaint")
               print("c)Consumption Data")
               print("q) Quit")
               print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
               print()
               ch2 = input("Enter the data you want to see or modify:")



               while ch2!='q':
                    
                    if ch2.lower() == 'a':
                         
                         print()
                         print("You have chose Resident information")
                         
                         print("Please choose from the following options:")
                         print()
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         print("a) Update Record")
                         print("b) Display Record")
                         print("q) Quit")
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         print()
                         ch3 = input("Enter:")

                         print()
                         while ch3!='q':
                              if ch3.lower() == 'a':
                                   
                                   print("You have chose to Update Record:")

                                   R_id = str(input("Enter Resident Id whose record to be updated:"))
                                   f=info.infores(R_id)

                                   if f:
                                        
                                        print()

                                        print("Choose the field you would like to update:")
                                        print()
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        print("a)First Name")
                                        print("b)Last Name")
                                        print("c)Age")
                                        print("d)Gender")
                                        print("e)Family")
                                        print("f)Vehicles")
                                        print("g)Email")
                                        print("h)Occupation")
                                        print("i)Phone Number")
                                        print("j)Resident Type")
                                        print("k)Building No.")
                                        print("l)Apartment No.")
                                        print("m)Building Id")
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        
                                        ch4 = str(input("Enter the option:"))

                                        print()
                                        upd.update_recordres(R_id,ch4)
                                        print()

                                        print("a) Update Record")
                                        print("b) Display Record")
                                        print("q) Quit")
                                        ch3=input("Enter another option or 'q' to quit:")

                                   else:

                                        print("Invalid resident id")
                                        continue
                                   
                                        

                              elif ch3.lower() == 'b':
                                   print()
                                   print("You have chosen to see the record")
                                   rid=input("Enter the resident id:")
                                   f=info.infores(rid)
                                   if f:
                                        ind.display_riesrecord(rid)

                                        print()
                                        print("a) Update Record")
                                        print("b) Display Record")
                                        print("q) Quit")
                                        ch3=input("Enter another option or 'q' to quit:")

                                   else:
                                        print("Invalid resident id")
                                        continue

                              else:
                                   print()
                                   print("you have entered wrong option")
                                   print()
                                   print("a) Update Record")
                                   print("b) Display Record")
                                   print("q) Quit")
                                   ch3=input("Enter another option or 'q' to quit:")
                                   
                         else:
                              print("Exiting resident data table")
                              break

                              

                    elif ch2.lower() == 'b':
                         print()
                         print("You have chose to register a complaint")
                         print()
                         print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                         
                         R_id = input("Enter the Resident Id:")

                         f=info.infores(R_id)
                         if f:
                              R_Bid = str(input("Enter the building Id:"))
                              R_FName = str(input("Enter the first name:"))
                              R_LName = input("Enter the last name:")
                              R_Pno = input("Enter the phone number:")
                              R_CMtype = str(input("Enter the complaint type (ELECTRICAL or CIVIL or PLUMBING):"))
                              R_Cm = str(input("Enter your complaint:"))
                              date_i = str(input("Enter the date (YYYY/MM/DD) issued:"))
                              cm_rem = str(input("Enter the complaint remarks resolved:"))
                              date_r = str(input("Enter the date (YYYY/MM/DD) it got resolved:"))
                              
                              print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                              print()
                              ins.insertcomp(R_id,R_Bid,R_FName,R_LName,R_Pno,R_CMtype,R_Cm,date_i,cm_rem,date_r)
                              print()

                              
                              print("a)Resident information")
                              print("b)Register complaint")
                              print("c)Consumption Data")
                              print("q) Quit")
                              ch2=input("Enter another option or 'q' to quit:")

                         else:
                              print("Resident id does not exist")
                              continue
                         
                    elif ch2.lower() == 'c':
                         print()
                         print("you have chose to see consumption data")
                         R_id=input("Enter your resident id to display data:")
                         f=info.infores(R_id)
                         if f:
                              print()
                              ind.display_consirecord(R_id)
                              print()

                              
                              print("a)Resident information")
                              print("b)Register complaint")
                              print("c)Consumption Data")
                              print("q) Quit")
                              ch2=input("Enter another option or 'q' to quit:")

                         else:
                              print("Resident id does not exist")
                              continue
                         


                    else:
                         print()
                         print("You have chosen the wrong choice")
                         print("a)Resident information")
                         print("b)Register complaint")
                         print("c)Consumption Data")
                         print("q) Quit")
                         ch2=input("Enter another option or 'q' to quit:")
               else:
                    print("Exiting the resident portal")
                    break

               
          #<--------------------------------------->STAFF SIDE<----------------------------------->
          elif ch1.lower() == 'b':
               print()
               print("Welcome to your staff hub!!")
               print(" <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)>")
               
               print()
               
               print("Enter the data you want to see or modify:")
               print()
               
               print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
               print("a)Resident information")
               print("b)View complaint")
               print("c)Consumption Data")
               print("d)Maintenance data")
               print("e) Search for staff")
               print("q) Quit")
               print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")

               print()
               ch2 = input("Enter the option:")
               while ch2!='q':
                    if ch2.lower() == 'a':
                         print()
                         print("You have chose Resident information")
                         print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                         print("Please choose from the following options:")
                         print()
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         print("a) Update Record")
                         print("b) Insert Record")
                         print("c) Display Record")
                         print("q) Quit")
                         print()
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         ch3 = input("Enter the option:")
                         print()

                         while ch3!='q':
                              if ch3.lower() == 'a':
                                   print()
                                   print("You have chose to Update Record:")

                                   R_id = str(input("Enter Resident Id whose record to be updated:"))
                                   f=info.infores(R_id)
                                   if f:
                                        print()
                                        print("Choose the field you would like to update:")
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        print("a)First Name")
                                        print("b)Last Name")
                                        print("c)Age")
                                        print("d)Gender")
                                        print("e)Family")
                                        print("f)Vehicles")
                                        print("g)Email")
                                        print("h)Occupation")
                                        print("i)Phone Number")
                                        print("j)Resident Type")
                                        print("k)Building No.")
                                        print("l)Apartment No.")
                                        print("m)Building Id")
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        
                                        ch4 = str(input("Enter Option:"))
                                        print()
                                        
                                        upd.update_recordres(R_id,ch4)
                                        print()
                                        print("a) Update Record")
                                        print("b) Insert Record")
                                        print("c) Display Record")
                                        print("q) Quit")
                                        ch3=input("Enter another option or 'q' to quit:")
                                   else:
                                        print("Resident id does not exist")
                                        continue

                              elif ch3.lower()=='b':
                                   print()
                                   print("You have chosen to enter a new record")
                                   print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                   R_id = input("Enter the allocated Resident Id:")
                                   R_Bid = str(input("Enter the allocated building Id:"))
                                   R_FName = str(input("Enter the first name:"))
                                   R_LName = input("Enter the last name:")
                                   R_Age = int(input("Enter the age:"))
                                   R_gen = input("Enter gender:")
                                   R_fam = int(input("Enter the No of Family Members:"))
                                   R_Veh = int(input("Enter the No of Vehicles:"))
                                   R_Email = input("Enter the Email Address:")
                                   R_Occ = input("Enter Occupation:")
                                   R_Pno = input("Enter the phone number:")
                                   R_type = str(input("Enter the resident type:"))
                                   R_bn = int(input("Enter building no:"))
                                   R_an = int(input("Enter apartment no:"))
                                   R_rent = float(input("Enter the rent:"))
                                   print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                   print()
                                   ins.insertres(R_id,R_Bid,R_FName,R_LName,R_Age,R_gen,R_fam,R_Veh,R_Email,R_Occ,R_Pno,R_type,R_bn,R_an,R_rent)
                                   print()
                                   print("a) Update Record")
                                   print("b) Insert Record")
                                   print("c) Display Record")
                                   print("q) Quit")
                                   
                                   ch3=input("Enter another option or 'q' to quit:")


                                   
                              elif ch3.lower() == 'c':
                                   print()
                                   print("You have chosen to see the record")
                                   
                                   rec.display_resrecord()
                                   print()
                                   print("a) Update Record")
                                   print("b) Insert Record")
                                   print("c) Display Record")
                                   print("q) Quit")
                                   ch3=input("Enter another option or 'q' to quit:")
                       


                              else:
                                   print()
                                   print("you have entered wrong option")
                                   print()
                                   print("a) Update Record")
                                   print("b) Insert Record")
                                   print("c) Display Record")
                                   print("q) Quit")
                                   ch3=input("Enter another option or 'q' to quit:")

                         else :
                            print("exited residence table")
                            break
                                   
                              

                              
                    elif ch2.lower() == 'b':
                         print()
                         print("You have chosen to the complaints")
                         print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                         print("Please choose from the following options:")
                         print()
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         print("a) Update Record")
                         print("b) Display Record")
                         print("c) Quit")
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         print()
                         ch3=input("Enter option: ")
                         print()
                         while ch3!='q':
                              if ch3.lower() == 'a':
                                   print()
                                   print("You have chose to Update Record:")

                                   R_id = str(input("Enter Resident Id whose record to be updated:"))
                                   f=info.infores(R_id)
                                   if f:

                                        print("Choose the field you would like to update:")
                                        print()
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        print("a) Give remarks to complaint")
                                        print("b)Date resolved")
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        
                                        ch4 = str(input("Enter the option"))
                                        print()
                                        upd.update_recordcomp(R_id,ch4)

                                        print()
                                        print("a) Update Record")
                                        print("b) Display Record")
                                        print("c) Quit")
                                        ch3=input("Enter another option or 'q' to quit:")

                                   else:
                                        print("Resident id does not exist")
                                        continue
                                        
                                        
                              elif ch3.lower()=='b':
                                   print()
                                   print("You have chosen to see the record")
                                   rec.display_comrecord()

                                   print()
                                   print("a) Update Record")
                                   print("b) Display Record")
                                   print("c) Quit")
                                   ch3=input("Enter another option or 'q' to quit:")
                         

                              else:
                                   print()
                                   print("you have entered wrong option")

                                   print()
                                   print("a) Update Record")
                                   print("b) Display Record")
                                   print("c) Quit")
                                   ch3=input("Enter another option or 'q' to quit:")

                         else:
                              print("exited complaint table")
                              break
                              

                    elif ch2.lower()=='c':
                          print()
                          print("You have chosen the consumption data")
                          print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                          print("Please choose from the following options:")
                          print()
                          print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                          
                          print("a) Add Record")
                          print("b) Update Record")
                          print("c) Delete Record")
                          print("d) Display Record")
                          print("e) Display Graph")
                          print("q) quit")
                          print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                          
                          ch3 = input("Enter Option:")

                          print()

                          while ch3!='q':
                               if ch3.lower()=='a':

                                    print()
                                    print("You have chosen to enter a new record")
                                    print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                    R_id = input("Enter the allocated Resident Id:")
                                    R_Bid = str(input("Enter the allocated building Id:"))
                                    R_FName = str(input("Enter the first name:"))
                                    R_LName = input("Enter the last name:")
                                    R_Pno = input("Enter the phone number:")
                                    R_Elc = str(input("Enter the Electricity Consumption:"))
                                    R_ElcP= int(input("Enter Electricity Price:"))
                                    R_Wat = str(input("Enter the Water Consumption:"))
                                    R_WatP= int(input("Enter Water Price:"))
                                    R_LPG = str(input("Enter the LPG Consumption:"))
                                    R_LPGP= int(input("Enter LPG Price:"))
                                    R_tot = float(input("Enter the total price"))
                                    print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                    print()
                                    ins.insertcons(R_id,R_Bid,R_FName,R_LName,R_Pno,R_Elc,R_ElcP,R_Wat,R_WatP,R_LPG,R_LPGP,R_tot)

                                    print()
                                    
                                    print("a) Add Record")
                                    print("b) Update Record")
                                    print("c) Delete Record")
                                    print("d) Display Record")
                                    print("e) Display Graph")
                                    print("q) quit")
                                    ch3=input("Enter another option or 'q' to quit:")

                                    
                               elif ch3.lower()=='b':
                                    print()
                                    print("You have chose to Update Record:")

                                    R_id = str(input("Enter Resident Id whose record to be updated:"))
                                    f=info.infores(R_id)
                                    if f:

                                         print()
                                         print("Choose the field you would like to update:")
                                         print()
                                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                         print("a)Electricity Consumption (KW/hr):")
                                         print("b)Electricity Price (Dhs):")
                                         print("c)Water Consumption (L/hr):")
                                         print("d)Water Price (Dhs):")
                                         print("e)LPG Consumption (gallon):")
                                         print("f)LPG Price (Dhs):")
                                         print("g)Total Consumption Price:")
                                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                         
                                         ch4 = str(input("Enter Option:"))
                                         print()
                                         upd.update_recordcons(R_id,ch4)
                                         
                                         print()
                                         
                                         print("a) Add Record")
                                         print("b) Update Record")
                                         print("c) Delete Record")
                                         print("d) Display Record")
                                         print("e) Display Graph")
                                         print("q) quit")
                                         ch3=input("Enter another option or 'q' to quit:")
                                    else:
                                         print("Resident id does not exist")
                                         continue



                               elif ch3.lower()=='c':
                                    print()
                                    print("you have chose to delete a record")
                                    R_id=input("Enter the resident id whose consumption records are to be deleted:")
                                    print()
                                    f=info.infores(R_id)
                                    if f:
                                         delt.delete_consrecord(R_id)
                                         

                                         print()
                                         
                                         print("a) Add Record")
                                         print("b) Update Record")
                                         print("c) Delete Record")
                                         print("d) Display Record")
                                         print("e) Display Graph")
                                         print("q) quit")

                                         
                                         ch3=input("Enter another option or 'q' to quit:")
                                         
                                    else:
                                         print("Resident id does not exist")
                                         continue
                                        



                               elif ch3.lower()=='d':
                                    print()
                                    print("You have chosen to see the records")
                                    rec.display_consrecord()
                                    print()
                                    


                                    print()
                                    
                                    print("a) Add Record")
                                    print("b) Update Record")
                                    print("c) Delete Record")
                                    print("d) Display Record")
                                    print("e) Display Graph")
                                    print("q) quit")

                                    
                                    ch3=input("Enter another option or 'q' to quit:")



                               elif ch3.lower()=='e':
                                    print()
                                    print("you have chosen to see graphical data")
                                    grp.graph()

                                    print()
                                    


                                    print()
                                    
                                    print("a) Add Record")
                                    print("b) Update Record")
                                    print("c) Delete Record")
                                    print("d) Display Record")
                                    print("e) Display Graph")
                                    print("q) quit")

                                    ch3=input("Enter another option or 'q' to quit:")


                               else:
                                   print()
                                   print("you have entered wrong option")

                                   print()
                                    
                                   print("a) Add Record")
                                   print("b) Update Record")
                                   print("c) Delete Record")
                                   print("d) Display Record")
                                   print("e) Display Graph")
                                   print("q) quit")
                                   ch3=input("Enter another option or 'q' to quit:")
                                   
                          else:
                               print("Exiting consumption table")
                               break
               

                    elif ch2.lower()=='d':
                         print()
                         print("You have chosen the MAINTENANCE data")
                         print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                         print("Please choose from the following options:")
                         print()
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         print("a) Insert Record")
                         print("b) Update Record")
                         print("c) Delete Record")
                         print("d) Display Record")
                         print("q) Quit")
                         print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                         
                         ch3=input("Enter option: ")

                         print()

                         
                         while ch3!='q':
                              if ch3.lower()=='a':
                                   
                                   print()
                                   print("You have chosen to enter records")
                                   print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                   B_id = str(input("Enter the allocated building Id:"))
                                   B_no=int(input("Enter the building No:"))
                                   S_GName = str(input("Enter the Security Guard name:"))
                                   L_check = input("Is the lift check DONE or DUE?:")
                                   L_date = input("Enter the date (YYYY/MM/DD) when lift check was done:")
                                   F_check = input("Is the Fire check DONE or DUE?:")
                                   F_date = input("Enter the date (YYYY/MM/DD) when Fire check was done:")
                                   AC_check = input("Is the AC check DONE or DUE?:")
                                   AC_date = input("Enter the date (YYYY/MM/DD) when AC check was done:")
                                   W_check = input("Is the Waste check DONE or DUE?:")
                                   W_date = input("Enter the date (YYYY/MM/DD) when Waste check was done:")
                                   
                                   print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                   print()
                                   ins.insertmaint(B_id,B_no,S_GName,L_check,L_date ,F_check,F_date ,AC_check ,AC_date ,W_check ,W_date)

                                   print()
                                   print("a) Insert Record")
                                   print("b) Update Record")
                                   print("c) Delete Record")
                                   print("d) Display Record")
                                   print("q) Quit")
                                   ch3=input("Enter another option or 'q' to quit:")





                              elif ch3.lower()=='b':
                                   print()
                                   print("You have chose to Update Record:")
                                   B_id = str(input("Enter Building Id whose record to be updated:"))

                                   f=info.infobldgm(B_id)
                                   if f:
                                         
                                        print()
                                        print("Choose the field you would like to update:")
                                        print()
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                        print("a) Lift Check")
                                        print("b) Lift Check Date")
                                        print("c) Fire Check")
                                        print("d) Fire Check Date")
                                        print("e) AC Check")
                                        print("f) AC Check Date")
                                        print("g) Waste Check")
                                        print("h) Waste Check Date")
                                        print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                         
                                        ch4 = str(input("Enter Option:"))
                                        print()
                                        upd.update_recordmaint(B_id,ch4)

                                        print()
                                        print("a) Insert Record")
                                        print("b) Update Record")
                                        print("c) Delete Record")
                                        print("d) Display Record")
                                        print("q) Quit")

                                        
                                        ch3=input("Enter another option or 'q' to quit:")

                                   else:
                                        print("Invalid Building id")
                                        continue
                                        

                              elif ch3.lower()=='c':
                                   print()
                                   print("You have chosen to Delete a record")
                                   B_id=input("Enter the building id whose maintenance records are to be deleted:")
                                   f=info.infobldgm(B_id)
                                   if f:
                                        print()
                                        delt.delete_maintrecord(B_id)

                                        print()
                                        print("a) Insert Record")
                                        print("b) Update Record")
                                        print("c) Delete Record")
                                        print("d) Display Record")
                                        print("q) Quit")

                                        
                                        ch3=input("Enter another option or 'q' to quit:")
                                   else:
                                        print("Invalid Building Id")
                                        continue


                              elif ch3.lower()=='d':
                                   print()
                                   print("you have chosen to view the records")
                                   
                                   print()
                                   rec.display_mainrecord()

                                   print()
                                   print("a) Insert Record")
                                   print("b) Update Record")
                                   print("c) Delete Record")
                                   print("d) Display Record")
                                   print("q) Quit")

                                   
                                   ch3=input("Enter another option or 'q' to quit:")
                              


                              else:
                                   print()
                                   print("you have entered wrong option")
                                   print()
                                   print("a) Insert Record")
                                   print("b) Update Record")
                                   print("c) Delete Record")
                                   print("d) Display Record")
                                   print("q) Quit")

                                   
                                   ch3=input("Enter another option or 'q' to quit:")
                                   
                         else:
                              print("exited maintenance table")
                              break         
                              

                    
                    elif ch2.lower()=='e':
                         print()
                         print("You have chosen to search for staff")
                         
                         
                         s_pos=input("Enter position of staff : ")
                         f=info.infostaffp(s_pos)
                         if f:
                              ind.display_staff(s_pos)

                              print("a)Resident information")
                              print("b)View complaint")
                              print("c)Consumption Data")
                              print("d)Maintenance data")
                              print("q) Quit")
                              
                              ch2=input("Enter another option or 'q' to quit:")
                              
                              print()

                         else:
                              print("Invalid staff position")
                              continue

                         
                    else:
                         print()
                         print("you have entered wrong option:")

                         print()

                         
                         print("a)Resident information")
                         print("b)View complaint")
                         print("c)Consumption Data")
                         print("d)Maintenance data")
                         print("q) Quit")
                         
                         ch2=input("Enter another option or 'q' to quit:")
               else:
                    print("exiting staff portal")
                    break



     #-------------------------------->ADMINISTRATOR SIDE<----------------------------------------------


          elif ch1.lower()=='c':
               print("PLEASE CLICK EXIT WHEN DONE")
               login=usp.adminlogin()
               if login:
                    
               
               
                    print()
                    print("Welcome ADMIN!!")
                    print(" <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)> <(^-^)>")
                    
                    print()
                    
                    print("Enter the data you want to see or modify:")
                    print()
                    
                    print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                    print("a)Resident information")
                    print("b)View complaint")
                    print("c)Consumption Data")
                    print("d)Maintenance data")
                    print("e) Staff data")
                    print("q) Quit")
                    print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")

                    print()
                    ch2 = input("Enter the option:")
                    while ch2!='q':
                         if ch2.lower() == 'a':
                              print()
                              print("You have chosen Resident information")
                              print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                              print("Please choose from the following options:")
                              print()
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              print("a) Display Record")
                              print("b) Delete Record")
                              print("q) Quit")
                              print()
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              ch3 = input("Enter the option:")
                              print()

                              while ch3!='q':
                                   if ch3.lower() == 'a':
                                        print()
                                        print("You have chosen to see the record")
                                        rec.display_resrecord()
                                        
                                        print()

                                        print("a) Display Record")
                                        print("b) Delete Record")
                                        print("q) quit")
                                        ch3=input("Enter another option or 'q' to quit:")

                                        
                                   elif ch3.lower() == 'b':
                                        print()
                                        print("you have chose to delete a record")
                                        R_id=input("Enter the resident id whose records are to be deleted:")
                                        f=info.infores(R_id)
                                        if f:
                                             print()
                                             delt.delete_resrecord(R_id)

                                             
                                             print()

                                             print("a) Display Record")
                                             print("b) Delete Record")
                                             print("q) quit")

                                              
                                             ch3=input("Enter another option or 'q' to quit:")

                                        else:
                                             print("Invalid Resident Id")
                                             continue


                                   else:
                                        print()
                                        print("you have entered wrong option")
                                        
                                        print()

                                        print("a) Display Record")
                                        print("b) Delete Record")
                                        print("q) quit")

                                        
                                        ch3=input("Enter another option or 'q' to quit:")

                              else :
                                 print("exited residence table")
                                 break
                                        
                                   

                                   
                         elif ch2.lower() == 'b':
                              print()
                              print("You have chosen to the complaints")
                              print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                              print("Please choose from the following options:")
                              print()
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              print("a) Update Record")
                              print("b) Display Record")
                              print("c) Quit")
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              print()
                              ch3=input("Enter option: ")
                              print()
                              while ch3!='q':
                                   if ch3.lower() == 'a':
                                        print()
                                        print("You have chose to Update Record:")

                                        R_id = str(input("Enter Resident Id whose record to be updated:"))
                                        f=info.infores(R_id)
                                        if f:

                                             print("Choose the field you would like to update:")
                                             print()
                                             print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                             print("a) Give remarks to complaint")
                                             print("b)Date resolved")
                                             print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                             
                                             ch4 = str(input("Enter the option"))
                                             print()
                                             upd.update_recordcomp(R_id,ch4)

                                             print()
                                             print("a) Update Record")
                                             print("b) Display Record")
                                             print("c) Quit")
                                             ch3=input("Enter another option or 'q' to quit:")

                                        else:
                                             print("Invalid Resident id")
                                             continue
                                        
                                   elif ch3.lower()=='b':
                                        print()
                                        print("You have chosen to see the record")
                                        rec.display_comrecord()

                                        print()
                                        print("a) Update Record")
                                        print("b) Display Record")
                                        print("c) Quit")
                                        ch3=input("Enter another option or 'q' to quit:")
                              

                                   else:
                                        print()
                                        print("you have entered wrong option 1")

                                        print()
                                        print("a) Update Record")
                                        print("b) Display Record")
                                        print("c) Quit")
                                        ch3=input("Enter another option or 'q' to quit: 1")

                              else:
                                   print("exited complaint table")
                                   break
                                   

                         elif ch2.lower()=='c':
                              print()
                              print("You have chosen the consumption data")
                              print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                              print("Please choose from the following options:")
                              print()
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              
                              print("a) Delete Record")
                              print("b) Display Record")
                              print("c) Display Graph")
                              print("q) quit")
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                               
                              ch3 = input("Enter Option:")

                              print()

                              while ch3!='q':
                                   if ch3.lower()=='a':
                                        print()
                                        print("you have chose to delete a record")
                                        R_id=input("Enter the resident id whose consumption records are to be deleted:")
                                        f=info.infores(R_id)
                                        if f:
                                             print()
                                             delt.delete_consrecord(R_id)
                                             print()
                                             print("a) Delete Record")
                                             print("b) Display Record")
                                             print("c) Display Graph")
                                             print("q) quit")
                                             
                                             ch3=input("Enter another option or 'q' to quit:")
                                        else:
                                             print("Invalid resident id")
                                             continue



                                   elif ch3.lower()=='b':
                                        print()
                                        print("You have chosen to see the records")
                                        
                                        print()
                                        rec.display_consrecord()
                                        print()
                                        print("a) Delete Record")
                                        print("b) Display Record")
                                        print("c) Display Graph")
                                        print("q) quit")
                                        
                                        ch3=input("Enter another option or 'q' to quit:")

                                   elif ch3.lower()=='c':
                                        print()
                                        print('You have chosen to see the graphical data')

                                        grp.graph()

                                        print()

                                        print("a) Delete Record")
                                        print("b) Display Record")
                                        print("c) Display Graph")
                                        print("q) quit")
                                        
                                        ch3=input("Enter another option or 'q' to quit:")




                                   else:
                                       print()
                                       print("you have entered wrong option")
                                       
                                       print()

                                       print("a) Delete Record")
                                       print("b) Display Record")
                                       print("c) Display Graph")
                                       print("q) quit")
                                         
                                       ch3=input("Enter another option or 'q' to quit:")
                                        
                              else:
                                   print("Exiting consumption table")
                                   break
                    

                         elif ch2.lower()=='d':
                              print()
                              print("You have chosen the MAINTENANCE data")
                              print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                              print("Please choose from the following options:")
                              print()
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              print("a) Delete Record")
                              print("b) Display Record")
                              print("q) Quit")
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              
                              ch3=input("Enter option: ")

                              print()

                              
                              while ch3!='q':
                                   if ch3.lower()=='a':
                                        print()
                                        print("You have chosen to Delete a record")
                                        B_id=input("Enter the building id whose maintenance records are to be deleted:")
                                        f=info.infobldgm(B_id)
                                        if f:
                                             print()
                                             delt.delete_maintrecord(B_id)

                                             print()
                                             print("a) Delete Record")
                                             print("b) Display Record")
                                             print("q) Quit")

                                             ch3=input("Enter another option or 'q' to quit:")

                                        else:
                                             print("Invalid Building Id entered")
                                             continue


                                   elif ch3.lower()=='b':
                                        print()
                                        print("you have chosen to view the records")
                                        
                                        print()
                                        rec.display_mainrecord()
                                        print()
                                        print("a) Delete Record")
                                        print("b) Display Record")
                                        print("q) Quit")

                                        
                                        ch3=input("Enter another option or 'q' to quit:")
                                   


                                   else:
                                        print()
                                        print("you have entered wrong option1")

                                        print()
                                        print("a) Delete Record")
                                        print("b) Display Record")
                                        print("q) Quit")

                                        
                                        ch3=input("Enter another option or 'q' to quit:")
                                        
                              else:
                                   print("exited maintenance table")
                                   break         


                         elif ch2.lower()=='e':
                              print("You have chosen the staff data")
                              print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                              print("Please choose from the following options:")
                              print()
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                              print("a) Insert Record")
                              print("b) Update Record")
                              print("c) Delete Record")
                              print("d) Display Record")
                              print("q) Quit")
                              print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")

                              
                              print()

                              ch3=input("Enter your choice:")
                              while ch3!='q':
                                   if ch3.lower()=='a':
                                        print()

                                        
                                        print("You have chosen to enter records")
                                        print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                        #S_Id ,S_Fname, S_Lname ,S_Desig ,S_Pno,S_email, S_address, S_salary
                                        Id=input("Enter Staff id:")
                                        fname=input("Enter first name:")
                                        lname=input("Enter last name:")
                                        desig=input("Enter designation:")
                                        pno=input("Enter phone number:")
                                        email=input("Enter email id:")
                                        add=input("Enter address:")
                                        sal=float(input("Enter the salary:"))
                                        print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
                                        print()
                                        ins.inserts_record(Id,fname,lname,desig,pno,email,add,sal)

                                        
                                        print()
                                        print("a) Insert Record")
                                        print("b) Update Record")
                                        print("c) Delete Record")
                                        print("d) Display Record")
                                        print("q) Quit")
                                        
                                        ch3=input("Enter another option or 'q' to quit:")
                                   if ch3.lower()=='b':
                                        print()
                                        print("You have chose to Update Record:")

                                        Sid = str(input("Enter Staff Id whose record to be updated:"))

                                        f=info.infostaff(Sid)
                                        if f:
                              
                                             print()
                                             print("Choose the field you would like to update:")
                                             print()
                                             print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                             print("a) First Name")
                                             print("b) Last Name")
                                             print("c) Designation")
                                             print("d) Phone Number")
                                             print("e) Email Address ")
                                             print("f) Address")
                                             print("g) Salary")
                                             print("￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣▽￣")
                                              
                                             ch4 = str(input("Enter Option:"))
                                             print()
                                             upd.update_records(Sid,ch4)
                                             
                                             print()
                                             print("a) Insert Record")
                                             print("b) Update Record")
                                             print("c) Delete Record")
                                             print("d) Display Record")
                                             print("q) Quit")
                                             
                                             ch3=input("Enter another option or 'q' to quit:")
                                        else:
                                             print("Invalid Staff id")
                                             continue


                                   if ch3.lower()=='c':
                                        print()
                                        print("You have chosen to Delete a record")
                                        Sid=input("Enter the staff id whose records are to be deleted:")
                                        f=info.infostaff(Sid)
                                        if f:
                                             print()
                                             delt.delete_srecord(Sid)
                                             print()
                                             print("a) Insert Record")
                                             print("b) Update Record")
                                             print("c) Delete Record")
                                             print("d) Display Record")
                                             print("q) Quit")

                                             
                                             ch3=input("Enter another option or 'q' to quit:")

                                        else:
                                             print("Invalid Staff id")
                                             continue


                                   elif ch3.lower()=='d':
                                        print()
                                        print("you have chosen to view the records")
                                        
                                        print()
                                        rec.display_srecord()

                                        print()
                                        print("a) Insert Record")
                                        print("b) Update Record")
                                        print("c) Delete Record")
                                        print("d) Display Record")
                                        print("q) Quit")
                                        
                                        ch3=input("Enter another option or 'q' to quit:")
                                   


                                   else:
                                        print()
                                        print("you have entered wrong option")

                                        print()
                                        print("a) Insert Record")
                                        print("b) Update Record")
                                        print("c) Delete Record")
                                        print("d) Display Record")
                                        print("q) Quit")

                                        
                                        ch3=input("Enter another option or 'q' to quit:")
                                        
                              else:
                                   print("exited staff info table")
                                   break 
                         
                                        
                         else:
                              print()
                              print("you have entered wrong option")
                              print()
                              
                              print("a)Resident information")
                              print("b)View complaint")
                              print("c)Consumption Data")
                              print("d)Maintenance data")
                              print("e) Staff data")
                              print("f) Building information")
                              print("q) Quit")
                              ch2=input("Enter another option or 'q' to quit:")
                    else:
                         print("exiting admin portal")
                         break




                    
               else:
                    print("Wrong password or username")
                    print('''Are you a :
                     a) Resident/
                     b) Staff
                     c) Administrators
                     q) Quit''')
                    ch1=input("Enter another option or 'q' to quit:")



          
               
               
               

          else :
               print()
               print("you have entered wrong option")
               print('''Are you a :
                a) Resident/
                b) Staff
                c) Administrators
                q) Quit''')
               ch1=input("Enter another option or 'q' to quit:")
     else:
          print("Exiting the Nakheel Portal")
          print()
     print("Hope you have a great day ahead")
     print("  (\￣︶￣*\)   (\￣︶￣*\)   (\￣︶￣*\)   (\￣︶￣*\)   (\￣︶￣*\) ")
