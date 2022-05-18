from flask import Blueprint,render_template,session,flash,redirect,request
from .__init__ import db,create_app
from flask_mail import Mail,Message

view=Blueprint('view', __name__)
app=create_app()
mail=Mail()

@view.route("/")
def index():
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM posts")
    posts=cur.fetchall()

    cur=db.connection.cursor()
    cur.execute("SELECT * FROM products")
    products=cur.fetchall()
    return render_template("shop/index.html",posts=posts,products=products)



@view.route("/about")
def about():
    return render_template("shop/about.html")



@view.route("/contact",methods=["GET","POST"])
def contact():
    if "user" in session:
        if request.method=="POST":
            name=request.form.get("name")
            email=request.form.get("email")
            message=request.form.get("message")
            if len(message)<20:
                flash("please write greater than 20 alphabet.",category="error")
                return redirect(request.url)

            msg = Message(f'message from {name}',sender=email,recipients=['dekbovideo@gmail.com'])  
            msg.body = str(message)  
            mail.send(msg) 
            flash("thanks for your message we will reply soon",category="success")
            return redirect("/")
        return render_template("shop/contact.html")
    else:
        return redirect("/login")