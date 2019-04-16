from flask import Flask, request, redirect, render_template
import re
import cgi



app = Flask(__name__)
app.config['DEBUG'] = True
 

               
@app.route("/")
def display_form():
    
    return render_template("forms.html",username="",username_error="",password="",password_error="",
                       verifypassword="",verifypassword_error="",email="",email_error="")
def is_notempty(string1):
  if string1 != "":
    return True
  else:
    return False
def no_space(string1):
   spacechar=" "
   if spacechar not in string1:
     return True
   else:
     return False
def validate_email(string1):
    valid_email = re.compile("[a-zA-Z0-9_]+\.?[a-zA-Z0-9_]+@[a-z]+\.[a-z]+")
    if valid_email.match(string1):
       return True
    else:
       return False
@app.route("/validate-form",methods=["POST"])
def validate():
   Username = request.form['username']
   Password = request.form['password'] 
   Verifypassword = request.form['verifypassword']
   Email= request.form['email']
   Username_error = ""
   Password_error = ""
   Verifypassword_error = ""
   Email_error= ""
   if not is_notempty(Username):
      Username_error="That's not a valid username"
      Username=""
   else:
      Username_len = len(Username)
      if  Username_len > 20 or Username_len < 3:
          Username_error ="That's not a valid username" 
          Username = ""
      else:
          if not no_space(Username):
             Username_error ="That's not a valid username"  
             Username = ""
   if not is_notempty(Password):
        Password_error = "That's not a valid password"  
        password_input = ""
   else:
       Password_len = len(Password)
       if Password_len > 20 or Password_len < 3:
          Password_error = "That's not a password"  
          Password = ""
       else:
          if not no_space(Password):
               Password_error = "That's not a valid password"  
               Password = ""
   if not is_notempty(Verifypassword):
        Verifypassword_error = "Password's don't match"
        Verifypassword = ""
   else:

      if Verifypassword!= Password:
          Verifypassword_error = "Passwords don't match"
          Verifypassword = ""
      if is_notempty(Email):
          Email_len = len(Email)
          if Email_len > 20 or Email_len < 3:
             Email_error = "Invalid email"
             Email = ""
          else:
              if not validate_email(Email):
                 Email_error = "Not a valid email"
                 Email = ""  

   if not Username_error and not Password_error and not Verifypassword_error and not Email_error:
      
      return render_template("welcome.html",name=Username)
   else:
      
      return render_template('forms.html',username=Username,username_error=Username_error,password=Password,password_error=Password_error,
                       verifypassword=Verifypassword,verifypassword_error=Verifypassword_error,email=Email,email_error=Email_error)
        

   
app.run()

