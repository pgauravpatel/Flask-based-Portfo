from flask import Flask, render_template,request, url_for, redirect
import sqlite3

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/savedetails",methods = ["POST","GET"])  
def user():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            subject = request.form["subject"]
            message = request.form["message"]
            with sqlite3.connect("userDB.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into user(name, email, subject, message) values (?,?,?,?)",(name,email,subject,message))  
                con.commit()  
                msg = "Your details Successfully Added, we will connect with you soon"  
        except:  
            con.rollback()  
            msg = "Sorry for inconvenience"  
        finally:  
            return render_template("Thank.html") 
            con.close() 

if __name__ == "__main__":  
    app.run(debug = True)  