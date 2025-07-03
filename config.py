import os

class Config:
    SECRET_KEY = 'your-secret-key-here'  # 用于会话加密
    SQLALCHEMY_DATABASE_URI = 'sqlite:///diabetes.db'  # SQLite数据库路径
    SQLALCHEMY_TRACK_MODIFICATIONS = False