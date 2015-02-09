from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/recent')
def recent():
    return render_template("recent_project.html")


if __name__ == '__main__':
    app.run(debug=True)
