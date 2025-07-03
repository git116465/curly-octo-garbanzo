from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 初始化Flask应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'temp-key'  # 临时密钥
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库和登录管理器
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# 必须在app初始化后导入路由（关键！）
from routes import *

# 导入用户模型并配置登录加载器
from models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 启动应用
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建数据库表
    app.run(debug=True)