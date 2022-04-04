from flask import Flask, render_template
a = Flask(__name__)


@a.route("/")
def sla():
    return render_template("slas.html")


@a.route("/register")
def regis():
    return render_template("reg.html")


if __name__ == "__main__":
    a.run()
