
import tables_database as tbdb
import update_rec as upd
import disp_indrec as ind
import disp_rec as rec
import ins_rec as ins
import del_rec as delt

import choices as ch

##tbdb.create()

#------------->MAIN PROGRAM STARTS HERE<------------------------------##################$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^&&&&&&&&&&&&&&&&&&&&&

print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
print()
print("Welcome to Nakheel Properties!!")
print()
print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")
#------------------->MAIN MENU<--------------------------
print('''Are you a :
      a) Resident
      b) Staff
      c) Administrators
      q) Quit''')
print()
ch1 = input("Enter your choice:")
print("－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－－O－")

print()
ch.program(ch1)
