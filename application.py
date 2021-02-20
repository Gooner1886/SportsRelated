import os

import time
from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response




# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///sportsrelated.db")



@app.route("/")
@app.route("/home")
@login_required
def index():
    posts = db.execute("SELECT * FROM posts ORDER BY dateandtime DESC")
    return render_template("index.html", posts=posts, title='Home')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    """Register a user"""

    if request.method == "POST":

        counter = 0
        username = request.form.get("username")
        for c in username:
            counter = counter + 1;

        # Ensure username was submitted
        if not request.form.get("username"):
            error = 'Must Provide Username'

        # Ensure that username is between 2 and 15 characters
        elif counter < 2 or counter > 15:
            error = 'Username requirements are not met'

        # Ensure that password was submitted
        elif not request.form.get("password"):
            error = 'Must Provide Password'

        # Ensure that confirmation password was submitted
        elif not request.form.get("confirmation"):
            error = 'Must Provide Confirmation'


        # Ensuring confirmation password matches password
        elif request.form.get("confirmation") != request.form.get("password"):
            error = 'Confirmation does not match Password'


        else:
            # Inserting username and password into database
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"),
                        generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8))

            return redirect(url_for('login'))

        return render_template('register.html', error=error)

    else:
        return render_template("register.html", title="Register")

@app.route("/login", methods = ['POST', 'GET'])
def login():

    """Log user in"""

    # Forget any user_id
    session.clear()


    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username was submitted
        if not request.form.get("username"):
            error = 'Must Provide Username'

        # Ensure password was submitted
        elif not request.form.get("password"):
            error = 'Must Provide Password'

        # Ensure username exists and password is correct
        elif len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            error = 'Invalid Credentials'

        else:
            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]

            # Redirect user to home page
            return redirect("/")

        return render_template("login.html", error = error)


    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", title = "Log In")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

@app.route("/about")
def about():
    """About Page"""

    return render_template("about.html", title = "About")

@app.route("/newpost", methods = ['GET', 'POST'])
def newpost():
    if request.method == "POST":

        # Ensure title was submitted
        if not request.form.get("title"):
            error = 'Must Provide Title'

        # Ensure Author was submitted
        elif not request.form.get("author"):
            error = 'Must Provide Author''s name'


        # Ensure content was submitted
        elif not request.form.get("content"):
            error = 'Must Provide Blog Content'

        else:
            title = request.form.get("title")
            author = request.form.get("author")
            content = request.form.get("content")
            db.execute("INSERT INTO posts(user_id, title, author, content, dateandtime) VALUES (?, ?, ?, ?, ?)", session["user_id"], title, author, content, datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

            return redirect("/")

        return render_template("newpost.html", error=error)

    else:
        return render_template("newpost.html", title = "New Post")

@app.route("/myblogs", methods = ['POST', 'GET'])
def myblogs():
    """Show user their blogs"""
    if request.method == "POST":
        if request.form.get("button") == "update":
            blogtitle = request.form.get("blogtitle")
            blogauthor = request.form.get("blogauthor")
            blogcontent = request.form.get("blogcontent")
            return render_template("update.html", blogtitle=blogtitle, blogauthor=blogauthor, blogcontent=blogcontent)
        elif request.form.get("button") == "delete":
            blogtitle = request.form.get("blogtitle")
            db.execute("DELETE FROM posts WHERE title = ?", blogtitle)
            return redirect("/myblogs")


    else:
        posts = db.execute("SELECT * FROM posts WHERE user_id = ?", session["user_id"])
        return render_template("myblogs.html", title="My Blogs", posts=posts)

@app.route("/update", methods = ['POST', 'GET'])
def update():
    if request.method == "POST":

        # Ensure title was submitted
        if not request.form.get("title"):
            error = 'Must Provide Title'

        # Ensure Author was submitted
        elif not request.form.get("author"):
            error = 'Must Provide Author''s name'


        # Ensure content was submitted
        elif not request.form.get("content"):
            error = 'Must Provide Blog Content'

        else:
            originaltitle = request.form.get("originaltitle")
            title = request.form.get("title")
            author = request.form.get("author")
            content = request.form.get("content")
            db.execute("UPDATE posts SET title = ?, content = ?, author = ?, dateandtime = ? WHERE user_id = ? AND title = ?", title, content, author, datetime.now().strftime('%d-%m-%Y %H:%M:%S'), session["user_id"], originaltitle)

            return redirect("/")

        return render_template("update.html", error=error)

    else:
        return render_template("update.html", title = "Update Post")


@app.route("/account", methods = ['POST', 'GET'])
def account():

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            error = 'Must Provide Username'

        # Ensure Author was submitted
        elif not request.form.get("favsport"):
            error = 'Must Provide Favorite Sport'


        # Ensure content was submitted
        elif not request.form.get("description"):
            error = 'Must Provide Description'

        else:
            originalusername = request.form.get("originalusername")
            username = request.form.get("username")
            favsport = request.form.get("favsport")
            description = request.form.get("description")
            originalfavsportrows = request.form.get("originalfavsport")
            originaldescriptionrows = request.form.get("originaldescription")


            db.execute("UPDATE users SET username = ? WHERE id = ? AND username = ?", username, session["user_id"], originalusername)
            if originalfavsportrows == '[]' and originaldescriptionrows == '[]':
                db.execute("INSERT INTO account (account_id, favsport, description) VALUES (?, ?, ?)", session["user_id"], favsport, description)
            else:
                db.execute("UPDATE account SET account_id = ?, favsport = ?, description = ? WHERE favsport = ? AND description = ?", session["user_id"], favsport, description, originalfavsportrows, originaldescriptionrows)

            return redirect("/")

        return render_template("account.html", error=error)

    else:
        usernamerows = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
        username = usernamerows[0]["username"]
        favsport = db.execute("SELECT favsport FROM account WHERE account_id = ?", session["user_id"])
        description = db.execute("SELECT description FROM account WHERE account_id = ?", session["user_id"])
        return render_template("account.html", title = "Your Account", username=username, favsport=favsport, description=description)

@app.route("/socials")
def socials():
    return render_template("socials.html")

@app.route("/announcements")
def announcements():
    return render_template("announcements.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/usage")
def usage():
    return render_template("usage.html")