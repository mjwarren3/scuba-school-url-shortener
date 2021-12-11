from flask import Flask, render_template, request, flash, redirect, url_for
import string
import random

app = Flask(__name__)

urls_db = {} # This stores all URL to Tiny URL combos. We would want a DO managed database for this so that it persists past running the application.


@app.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST": # If data submitted through form
        url = request.form["url"]

        if not url:
            flash("The URL is required!")
            return redirect(url_for("index"))

        id = "".join(random.choices(string.ascii_letters, k=6)) # Create random ID

        short_url = request.host_url + id #Generate new URL
        urls_db[id] = request.form["url"] #Generate new URL
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")


@app.route("/<id>")
def url_redirect(id):
    url = urls_db.get(id, None)
    if url is not None:
        return redirect(url) #This does the redirect
    else:
        flash("Invalid URL")
        return redirect(url_for("index")) #This does the redirect


app.run(host="0.0.0.0", port=8080)
