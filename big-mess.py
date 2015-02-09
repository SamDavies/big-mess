from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/contacts')
def hello_world():
    return render_template("contacts.html")


@app.route('/portfolio')
def hello_world():
    return render_template("portfolio.html")


@app.route('/services')
def hello_world():
    return render_template("services.html")


@app.route('/about_us')
def hello_world():
    return render_template("about_us.html")


if __name__ == '__main__':
    app.run(debug=True)
