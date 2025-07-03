from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User

# 根路由（测试用）
@app.route('/')
def index():
    return "根路由正常，<a href='/register'>去注册</a>"

# 注册路由
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 简化版注册逻辑
        user = User(
            username=request.form['username'],
            email=request.form['email'],
            password_hash=generate_password_hash(request.form['password'])
        )
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect('/login')
    return render_template('register.html')

# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            return redirect('/dashboard')
        flash('登录失败')
    return render_template('login.html')

# 仪表盘路由
@app.route('/dashboard')
@login_required
def dashboard():
    return f"登录成功！用户名：{current_user.username}，<a href='/logout'>退出</a>"

# 登出路由
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')