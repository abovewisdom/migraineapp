from django.shortcuts import render
from web.forms import RegisterForm
#from helpers import apology

# Create your views here.
def index(request):
   return render(request, 'index.html')

def entry(request):
   return render(request, 'entry.html')
# Change below to handle post requests
def posts(request):
   return render(request, 'index.html')

def register(request):
   if request.method =='GET':
       return render(request, 'register.html', {'form': RegisterForm()})
   if request.method =='POST':
#       # Ensure username was submitted
#        if not request.form.get("username"):
#            return apology("must provide username", 403)
#
#        # Ensure password was submitted
#        elif not request.form.get("password"):
#            return apology("must provide password", 403)
#
#        # Ensure password was submitted 2nd time and it is the same as first
#        elif not request.form.get("confirmation"):
#            return apology("must enter the same password twice ", 403)
#        elif not request.form.get("password") == request.form.get("confirmation"):
#            return apology("must enter the same password twice ", 403)
#        # Check for username already existing in table. if it does present apology
#        else:
#            #Hash password
#            pwhash = encrypt_password(request.form.get("password"))
#            #Insert new row in database
#            db.execute("INSERT INTO customers(username,pwhash) VALUES(:username, :pwhash)", username = request.form.get("username"), pwhash=pwhash)
#            #Get user infor
#            rows = db.execute("SELECT * FROM customers WHERE username = :username", username = request.form.get("username"))
#            #log the user in
#            session["user_id"] = rows[0]["id"]
#            #back to home page
            return redirect("/")
def login(request):
   return render(request, 'login.html')
