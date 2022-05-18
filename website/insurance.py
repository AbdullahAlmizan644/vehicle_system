from flask import Blueprint, redirect, render_template,request,flash,session, url_for
from .__init__ import db,create_app
import os
from werkzeug.utils import secure_filename
from datetime import datetime,timedelta


insurance=Blueprint('insurance', __name__)
app=create_app()


@insurance.route("/pricing")
def pricing():
    return render_template("insurance/pricing.html")



@insurance.route("/payment/<int:days>/<int:price>",methods=["GET","POST"])
def payment_method(days,price):
    if "user" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where username=%s",(session["user"],))
        user=cur.fetchone()
        if request.method=="POST":
            address=request.form.get("address")
            card=request.form.get("card")
            card_number=request.form.get("card_number")
            card_cvv=request.form.get("card_code")
            validity=datetime.now()+timedelta(days=days)

            cur=db.connection.cursor()
            cur.execute("INSERT INTO insurance(username,card,car_number,address,validity,date,price) VALUES(%s,%s,%s,%s,%s,%s,%s)",(user[1],card,card_number,address,validity,datetime.now(),price,))
            db.connection.commit()
            return redirect(f"/confirm/{validity}")
        return render_template("insurance/payment_method.html",days=days,price=price)
    else:
        return redirect("/login")



@insurance.route("/confirm/<string:days>")
def confirm(days):
    return render_template("insurance/confirm.html",days=days)