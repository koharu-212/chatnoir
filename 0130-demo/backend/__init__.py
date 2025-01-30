from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    
    # データベースの設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_db_user:your_db_password@db:5432/your_db_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    # dbの初期化
    db.init_app(app)

    return app
