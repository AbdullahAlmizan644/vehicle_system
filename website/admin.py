from flask import Blueprint, render_template,request,flash,redirect, session
from .settings import info
from .__init__ import db,create_app
import os
from werkzeug.utils import secure_filename
from datetime import datetime



admin=Blueprint('admin',__name__)
app=create_app()



@admin.route("/admin_login",methods=["GET","POST"])
def admin_login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")

        if email==info["admin_email"] and password==info["admin_password"]:
            session["admin"]=email
            return redirect("/dashboard")
        else:
            flash("Wrong email or password.",category="error")
    return render_template("admin/login.html")



@admin.route("/admin_logout")
def admin_logout():
    session.pop("admin", None)
    flash("Admin Logged out!")
    return redirect("/")



@admin.route("/dashboard")
def dashboard():
    if "admin" in session:

        cur=db.connection.cursor()  
        cur.execute("SELECT count(post_id) from posts ")
        total_posts=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(sno) from users")
        total_users=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(product_id) from products ")
        total_products=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(repair_id) from repairs where active=%s",(0,))
        total_pending=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(rent_id) from rents ")
        total_rents=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(order_id) from orders")
        total_orders=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(id) from insurance")
        total_insurance=cur.fetchone()

        cur=db.connection.cursor()  
        cur.execute("SELECT count(id) from review_comments")
        total_comment=cur.fetchone()


        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        return render_template("admin/index.html",users=users,total_posts=total_posts,total_products=total_products,total_users=total_users,total_pending=total_pending,total_comment=total_comment,total_orders=total_orders,total_rents=total_rents,total_insurance=total_insurance)

    else:
        return redirect("/admin_login")





@admin.route("/all_user")
def all_user():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(sno) from users ")
        total_users=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        return render_template("admin/all_user.html",users=users,total_users=total_users)

    else:
        return redirect("/admin_login")



@admin.route("/delete_user/<int:id>")
def delete_user(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM users WHERE sno=%s",(id,))
        db.connection.commit()
        flash("You Blocked a user!",category="error")
        return redirect("/all_user")
    
    else:
        return redirect("/admin_login")



@admin.route("/all_review")
def all_review():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(post_id) from posts ")
        total_posts=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM posts")
        posts=cur.fetchall()
        return render_template("admin/all_review.html",posts=posts,total_posts=total_posts)

    else:
        return redirect("/admin_login")


@admin.route("/delete_review/<int:id>")
def delete_review(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM posts WHERE post_id=%s",(id,))
        db.connection.commit()
        flash("Delete review!",category="error")
        return redirect("/all_review")
    
    else:
        return redirect("/admin_login")






@admin.route("/all_product")
def all_product():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(product_id) from products")
        total_products=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM products")
        products=cur.fetchall()
        return render_template("admin/all_product.html",products=products,total_products=total_products)

    else:
        return redirect("/admin_login")


@admin.route("/delete_product/<int:id>")
def delete_product(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM products WHERE product_id=%s",(id,))
        db.connection.commit()
        flash("Delete product!",category="error")
        return redirect("/all_product")
    
    else:
        return redirect("/admin_login")



@admin.route("/add_product",methods=["GET","POST"])
def add_product():
    if "admin" in session:
        if request.method=="POST":
            name=request.form.get("name")
            description=request.form.get("description")
            price=request.form.get("price")
            category=request.form.get("category")
            type=request.form.get("type")
            image = request.files['image']
            if image.filename == '':
                flash('No selected file', category="error")
                return redirect(request.url)
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
                cur=db.connection.cursor()
                cur.execute("INSERT INTO products(name,description,price,image,date,category,type) VALUES (%s,%s,%s,%s,%s,%s,%s)",(name,description,price,image.filename,datetime.now(),category,type))
                db.connection.commit()
                return redirect("/all_product")

        return render_template("admin/add_product.html")
    else:
        return redirect("/admin_login")



@admin.route("/edit_product/<int:id>",methods=["POST","GET"])
def edit_produt(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM products WHERE product_id=%s",(id,))
        product=cur.fetchone()
        if request.method=="POST":
            name=request.form.get("name")
            description=request.form.get("description")
            price=request.form.get("price")
            category=request.form.get("category")
            type=request.form.get("type")
            image = request.files['image']

            if image.filename == '':
                flash('No selected file', category="error")
                return redirect(request.url)
            else:
                cur=db.connection.cursor()
                cur.execute("update products set name=%s,description=%s,price=%s,category=%s,image=%s,type=%s where product_id=%s",(name,description,price,category,image.filename,type,id,))
                db.connection.commit()

            return redirect("/all_product")
        return render_template("admin/Edit_product.html",product=product)
    else:
        return redirect("/admin_login")



@admin.route("/all_repair")
def all_repair():
    if "admin" in session:
        a=0
        cur=db.connection.cursor()  
        cur.execute("SELECT count(repair_id) from repairs where active=%s",(a,))
        total_pending=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM repairs")
        repairs=cur.fetchall()
        return render_template("admin/all_repair.html",repairs=repairs,total_pending=total_pending)

    else:
        return redirect("/admin_login")


@admin.route("/delete_repair/<int:id>")
def delete_repair(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM repairs WHERE repair_id=%s",(id,))
        db.connection.commit()
        flash("Delete repair!",category="error")
        return redirect("/all_repair")
    
    else:
        return redirect("/admin_login")


@admin.route("/accept_repair/<int:id>")
def accept_repair(id):
    a=1
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("UPDATE repairs set active=%s WHERE repair_id=%s",(a,id,))
        db.connection.commit()
        flash("accept repair!",category="success")
        return redirect("/all_repair")
    
    else:
        return redirect("/admin_login")





@admin.route("/all_rent")
def all_rent():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(rent_id) from rents")
        total_rent=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM rents")
        rents=cur.fetchall()
        return render_template("admin/all_rent.html",rents=rents,total_rent=total_rent)

    else:
        return redirect("/admin_login")



@admin.route("/delete_rent/<int:id>")
def delete_rent(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM rents WHERE rent_id=%s",(id,))
        db.connection.commit()
        flash("Delete rent!",category="error")
        return redirect("/all_rent")
    
    else:
        return redirect("/admin_login")




@admin.route("/all_order")
def all_order():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(order_id) from orders")
        total_order=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM orders")
        orders=cur.fetchall()
        return render_template("admin/all_order.html",orders=orders,total_order=total_order)

    else:
        return redirect("/admin_login")


@admin.route("/delete_order/<int:id>")
def delete_order(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM orders WHERE order_id=%s",(id,))
        db.connection.commit()
        flash("Delete order!",category="error")
        return redirect("/all_order")
    
    else:
        return redirect("/admin_login")




@admin.route("/all_insurance")
def all_insurance():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(id) from insurance")
        total_insurance=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM insurance")
        insurance=cur.fetchall()
        return render_template("admin/all_insurance.html",total_insurance=total_insurance,insurance=insurance)

    else:
        return redirect("/admin_login")



@admin.route("/delete_insurance/<int:id>")
def delete_insurance(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM insurance WHERE id=%s",(id,))
        db.connection.commit()
        flash("Delete insurance!",category="error")
        return redirect("/all_insurance")
    
    else:
        return redirect("/admin_login")




@admin.route("/all_comment")
def all_comment():
    if "admin" in session:
        cur=db.connection.cursor()  
        cur.execute("SELECT count(id) from review_comments")
        total_comment=cur.fetchone()

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM review_comments")
        comments=cur.fetchall()
        return render_template("admin/all_comment.html",comments=comments,total_comment=total_comment)

    else:
        return redirect("/admin_login")



@admin.route("/delete_comment/<int:id>")
def delete_comment(id):
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("DELETE FROM review_comments WHERE id=%s",(id,))
        db.connection.commit()
        flash("Delete comment!",category="error")
        return redirect("/all_comment")
    
    else:
        return redirect("/admin_login")

