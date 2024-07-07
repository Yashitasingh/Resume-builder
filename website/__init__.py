from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key ='key_123'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
