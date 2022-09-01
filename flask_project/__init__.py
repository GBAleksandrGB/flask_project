from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_pyfile('config.py')
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from flask_project.main.routes import main
    app.register_blueprint(main)

    from flask_project.users.routes import users
    app.register_blueprint(users)

    from flask_project.posts.routes import posts
    app.register_blueprint(posts)

    from flask_project.errors.handlers import errors
    app.register_blueprint(errors)

    return app
