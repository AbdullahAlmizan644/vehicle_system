from flask import Blueprint, redirect, render_template,request,flash,session
from .__init__ import db,create_app
import os
from werkzeug.utils import secure_filename
from datetime import datetime,timedelta


shop=Blueprint('shop', __name__)
app=create_app()


@shop.route("/shop")
def shops():
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM products")
    products=cur.fetchall()
    return render_template("shop/shop.html",products=products)



@shop.route("/product_details/<int:id>")
def product_details(id):
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM products WHERE product_id=%s",(id,))
    product=cur.fetchone()
    return render_template("shop/product_details.html",product=product)



@shop.route("/checkout/<int:id>",methods=["GET","POST"])
def checkout(id):
    if "user" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM products WHERE product_id=%s",(id,))
        product=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s",(session["user"],))
        user=cur.fetchone()

        if request.method=="POST":
            address=request.form.get("address")
            city=request.form.get("city")
            zip=request.form.get("zip")
            state=request.form.get("state")
            phone=request.form.get("phone")
            card=request.form.get("card")
            card_number=request.form.get("card_number")
            card_code=request.form.get("card_code")

            cur=db.connection.cursor()
            cur.execute("INSERT INTO orders(product_name,product_price,product_image,address,city,state,zip,phone,card_type,card_number,card_cvv,username,email,date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(product[1],product[2],product[3],address,city,state,zip,phone,card,card_number,card_code,user[1],user[2],datetime.now()))
            db.connection.commit()
            flash("Your Order Taken.",category="success")
            return render_template("shop/thank_you.html")

        return render_template("shop/checkout.html",product=product)
    else:
        return redirect("/login")




@shop.route("/search_product",methods=["GET","POST"])
def search_product():
    if request.method=="POST":
        search_name=request.form.get("search")
        cur=db.connection.cursor()
        cur.execute(f"SELECT * FROM products WHERE name LIKE '%{search_name}%'")
        s_result=cur.fetchall()
        
        return render_template("shop/search_product.html",s_result=s_result,search_name=search_name)




@shop.route("/rent_checkout/<int:id>", methods=["GET","POST"])
def rent_checkout(id):
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM products WHERE product_id=%s",(id,))
    product=cur.fetchone()

    cur=db.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s",(session["user"],))
    user=cur.fetchone()

    if request.method=="POST":
        address=request.form.get("address")
        card=request.form.get("card")
        card_number=request.form.get("card_number")
        card_code=request.form.get("card_code")
        validity=datetime.now()+timedelta(days=31)

        cur=db.connection.cursor()
        cur.execute("INSERT INTO rents(username,email,address,product_name,rent_price,rent_date,validity,card,card_number,card_cvv) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user[1],user[2],address,product[1],product[2],datetime.now(),validity,card,card_number,card_code,))
        db.connection.commit()
        flash("Your rent taken sucessfully.",category="success")
        return redirect(f"/rent_confirm/{validity}")

    return render_template("rent/rent_checkout.html",product=product)


@shop.route("/rent_confirm/<string:days>")
def rent_confirm(days):
    return render_template("rent/rent_confirm.html",days=days)





