from flask import Flask,Blueprint
from flask_mysqldb import MySQL
from flask_mail import Mail,Message

db=MySQL()
mail = Mail()

def create_app():
    UPLOAD_FOLDER = 'C:\\Users\\abdul\\Videos\\fahad-project\\website\\static\\img'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    app=Flask(__name__)
    app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
    app.config['SECRET_KEY']='FAHAD'
    app.config['MYSQL_HOST']='127.0.0.1'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']=''
    app.config['MYSQL_DB']='vehicle_system'

    app.config["MAIL_SERVER"]='smtp.gmail.com' 
    app.config["MAIL_PORT"] = 465
    app.config['MAIL_USE_TLS'] = False  
    app.config['MAIL_USE_SSL'] = True  
    app.config["MAIL_USERNAME"] = 'dekbovideo@gmail.com'  
    app.config['MAIL_PASSWORD'] = '5255452554'  


    db.init_app(app)
    mail.init_app(app)




    from .view import view
    from .review import review
    from .repair import repair
    from .shop import shop
    from .admin import admin
    from .auth import auth
    from .insurance import insurance


    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(review, url_prefix="/")
    app.register_blueprint(shop, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(repair, url_prefix="/")
    app.register_blueprint(insurance, url_prefix="/")

    return app