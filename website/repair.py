from functools import reduce
from pyexpat import model
from time import time
from flask import Blueprint, redirect,render_template,request, session,flash
from .__init__ import db,create_app
from datetime import datetime
import os
from werkzeug.utils import secure_filename




repair=Blueprint("repair", __name__)



@repair.route("/add_repair",methods=["GET","POST"])
def add_product():
    if "user" in session:
        if request.method=="POST":
            category=request.form.get("category")
            name=request.form.get("name")
            model=request.form.get("model")
            time=request.form.get("time")
            date=request.form.get("date")
            address=request.form.get("address")
            
            cur=db.connection.cursor()
            cur.execute("INSERT INTO repairs(category,vehicle_name,vehicle_model,service_date,service_time,address,date,username) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(category,name,model,date,time,address,datetime.now(),session["user"],))
            db.connection.commit()
            flash("your repair post submit successfully!! check repair history",category="success")
            return redirect("/profile")
    else:
        return redirect("/admin_login")


