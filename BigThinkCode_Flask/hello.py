from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


# @app.route('/hello/<user>')
# def home(user):
#     return render_template('hello.html', name=user)


@app.route('/admin')
def hello_admin():
    return 'Hello admin!'


@app.route('/guests/<guest>')
def hello_guest(guest):
    return 'Hello %s!' % guest


# @app.route('/hello/<name>')
# def hello_name(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_user', guest=name))


@app.route('/hello/<int:score>')
def hello_result(score):
    return render_template('hello.html', marks=score)


if __name__ == '__main__':
    app.run(debug=True)
