from flask import Flask, render_template, request, redirect
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
secret_key = os.getenv("SECRET_KEY")
app.secret_key = secret_key

@app.route("/")
def home():
    return render_template("home.html", active_page="home")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    maximum = 1000
    if request.method == "POST":
        nachricht = request.form.get("nachricht", "").strip()
        zeichenanzahl = len(nachricht)
        if zeichenanzahl > maximum:
            return redirect("/contact")
        return redirect("/contact")
    return render_template("contact.html", active_page="contact", max_Zeichen=maximum)

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", active_page="portfolio")

@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

@app.route("/impressum")
def impressum():
    return render_template("impressum.html", active_page="impressum")

@app.route("/EJApp")
def app1():
    return render_template("EJApp.html", active_page="app1", layout_mode="minimal")

@app.route("/WetterApp")
def app2():
    return render_template("WetterApp.html", active_page="app2", layout_mode="minimal")


app.run(debug=True)
