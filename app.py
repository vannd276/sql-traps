from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

try:
    connection = sqlite3.connect("static/database/database-abc.sqlite", check_same_thread=False)
    cursor = connection.cursor()
except:
    exit()


@app.route('/')
def hello_world():
    return render_template("index.html", title="Never Give Up");


@app.route("/characters")
def character():
    return render_template("character.html", title="Characters")


@app.route("/file", methods=["GET"])
def fileSearch():
    if "file" in request.args.keys():
        path = request.args.get("file")
        if "../../etc/passwd" in path:
            with open("static/etccccccc.txt") as f:
                content = f.read()
            return f"<div style='white-space: pre-line !important'>{content}</div"
        elif "log.txt" in path:
            with open("static/loggggggg.txt") as f:
                content = f.read()
            return f"<div style='white-space: pre-line !important'>{content}</div>"
        else:
            return "<h1 style='text-align: center !important'>404 - File not found</h1>"
    else:
        return "<h3 style='text-align: center !important'>File parameter is required!!!</h3>"

@app.route("/about")
def about():
    if "search" in request.args.keys():
        search = request.args.get('search')
    else:
        search = ""
    query = f"select * from characters where name like '%{search}%';"
    cursor.execute(query)
    result = cursor.fetchall()
    return render_template("about.html", characters=result, title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us")

if __name__ == '__main__':
    app.run()
