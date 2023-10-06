from flask import Flask, render_template, request, redirect, url_for
from website import app
from website.models import User
from flask_login import login_user, login_required, logout_user

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        attempUser = User.query.filter_by(username=username).first()
        if attempUser:
            if(attempUser.password == password):
                login_user(attempUser)
                return redirect(url_for('content'))

    return render_template('login.html')

@app.route('/content')
@login_required
def content():
    return render_template('content.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))