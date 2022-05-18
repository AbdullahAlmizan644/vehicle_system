from flask import Blueprint, redirect,render_template,request, session,flash
from .__init__ import db,create_app
from datetime import datetime
import os
from werkzeug.utils import secure_filename




review=Blueprint("review", __name__)

app=create_app()
@review.route("/review")
def blog():
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM posts")
    posts=cur.fetchall()
    return render_template("shop/blog.html",posts=posts)



@review.route("/review_details/<int:id>",methods=["GET","POST"])
def blog_details(id):
    cur=db.connection.cursor()
    cur.execute("SELECT * FROM posts where post_id=%s",(id,))
    post=cur.fetchone()

    cur=db.connection.cursor()
    cur.execute("SELECT * FROM review_comments where post_id=%s",(id,))
    comment=cur.fetchall()

    cur=db.connection.cursor()  
    cur.execute("SELECT count(post_id) from review_comments where post_id=%s",(id,))
    total_comments=cur.fetchone()

    # print(comment)
    
    if request.method=="POST":
        comment=request.form.get("comment")

        if "user" in session:
            cur=db.connection.cursor()
            cur.execute("SELECT * FROM users where username=%s",(session["user"],))
            user=cur.fetchone()


            cur=db.connection.cursor()
            cur.execute("INSERT INTO review_comments(username,image,message,post_id,date) VALUES(%s,%s,%s,%s,%s)",(user[1],user[3],comment,id,datetime.now(),))
            db.connection.commit()
            return redirect(request.url)
        
        else:
            return redirect("/login")


    return render_template("shop/blog_details.html",post=post,comment=comment,total_comments=total_comments)





@review.route("/add_review", methods=["GET","POST"])
def add_review():
    if "user" in session:
        if request.method=="POST":
            title=request.form.get('title')
            content=request.form.get('content')
            image = request.files['file']
            if image.filename == '':
                flash('No selected file', category="error")
                return redirect(request.url)
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))

            cur=db.connection.cursor()
            cur.execute("INSERT INTO posts(title,content,writer,date,image) values(%s,%s,%s,%s,%s)",(title,content,session["user"],datetime.now(),image.filename))
            db.connection.commit()
            return redirect("/review")

    else:
        return redirect("/login")


            
        
@review.route("/search_review",methods=["GET","POST"])
def search_product():
    if request.method=="POST":
        search_name=request.form.get("search")
        cur=db.connection.cursor()
        cur.execute(f"SELECT * FROM posts WHERE title LIKE '%{search_name}%'")
        s_result=cur.fetchall()
        
        return render_template("shop/search_review.html",s_result=s_result)