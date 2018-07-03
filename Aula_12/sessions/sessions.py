from flask import Flask, session, render_template, redirect, url_for, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(10)


@app.route('/')
def home():
    if 'user' in session:
        name = session['user']
        return render_template('main.html', user=name)
    else:
        return render_template('login.html')


@app.route('/setsession', methods=['GET', 'POST'])
def setsession():
    if 'user' not in session.keys():
        session['user'] = request.form['user']
        session['password'] = request.form['password']
    user = session['user']
    return render_template('main.html', user=user)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    session.pop('password', None)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
