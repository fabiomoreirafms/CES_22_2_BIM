# Feito com base no material didático e no exemplo disponível em http://cs.wellesley.edu/cs304app/cookies/
# todavia sem acesso ao código do exemplo

from flask import Flask, make_response, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    if not request.cookies.get('name'):
        return render_template('home.html')
    else:
        return redirect(url_for('cookies'))


@app.route("/cookies", methods=['POST', 'GET'])
def cookies():

    if not request.cookies.get('name'):
        name = request.form['name']
        count = str(1)
        message = "Parabens, {0}! Você está usando um cookie {1} vez!".format(name, count)
        resp = make_response(render_template('home1.html', msg=message))
        resp.set_cookie('name', name)
        resp.set_cookie('count', count)
    else:
        name = request.cookies.get('name')
        count = str(int(request.cookies.get('count')) + 1)
        message = "Parabens, {0}! Você está usando um cookie {1} vezes!".format(name, count)
        resp = make_response(render_template('home1.html', msg=message))
        resp.set_cookie('count', count)
    return resp


@app.route("/delcookie", methods =['POST', 'GET'])
def delcookies():
    resp = make_response(render_template('home.html'))
    if request.cookies.get('name'):
        resp.set_cookie('name', '', max_age=0)
        resp.set_cookie('count', '', max_age=0)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
