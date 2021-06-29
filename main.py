from flask import Flask, render_template, redirect, url_for, flash, abort, request, send_from_directory
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = "3*##$!d2dsfhx_sdafsafa23156sdasf''''fasf&&1;;'&"


@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/about-us')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/contact-form')
def contactForm():
    return render_template("contact2.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run(debug=True)