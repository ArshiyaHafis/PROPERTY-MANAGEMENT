from tkinter import *
from functools import partial


def adminlogin():
     def validateLogin(username, password):
          a=username.get()
          b=password.get()

          
          
          if a=='Arshiya2004' and b=='dpsdubai':
               x=True
          else:

               x=False
          return x
           

     def quits():
             tkWindow.destroy()
     #window
     tkWindow = Tk()  
     tkWindow.geometry('210x80')  
     tkWindow.title('NAKHEEL Login Form')

     #username label and text entry box
     usernameLabel = Label(tkWindow, text="User Name : ").grid(row=0, column=0)
     username = StringVar()                                           #like a normal variable - used to specify the kind of input , intVar, boolVar

     usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

     #password label and password entry box
     passwordLabel = Label(tkWindow,text="Password : ").grid(row=1, column=0)  
     password = StringVar()
     passwordEntry = Entry(tkWindow, textvariable=password, show='•').grid(row=1, column=1)
##     validateLogin(username, password)

     validateLogin = partial(validateLogin, username, password)            #partial -  seperate functions into functions with lesser arguments(0,2)


     loginButton = Button(tkWindow, text="LOGIN", command=validateLogin).grid(row=4, column=0) #cpmmand calls the function 

     exitButton=Button(tkWindow,text="exit",command=quits).grid(row=5, column=0)
     
     
     tkWindow.mainloop()

     return validateLogin()
     

