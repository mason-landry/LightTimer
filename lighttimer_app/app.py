from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import sqlite3
from ast import literal_eval
import datetime

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if session.get("user_id") is None:
        session["user_id"]=[]
    #Get settings
    conn = sqlite3.connect('my_database.db')
    settings = conn.execute("select start,stop from settings order by rowid DESC limit 1").fetchone()
    try:
        start = literal_eval(settings[0])
        stop = literal_eval(settings[1])
        start = datetime.time(start[0],start[1],start[2])
        stop = datetime.time(stop[0],stop[1],stop[2])

        recent_settings = (str(start),str(stop))
        conn.close()
        print(recent_settings)
        return render_template('index.html', username=session["user_id"], settings=recent_settings)
    except:
        return render_template('index.html', username=session["user_id"])



@app.route('/login', methods=["POST", "GET"])
def login():
    if session.get("user_id") is None:
        session["user_id"]=[]

    if request.method == 'POST':
        conn = sqlite3.connect('my_database.db')
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')
 
        if conn.execute("SELECT * FROM users WHERE user=?", (username,)).fetchone() is None:
            return render_template("login.html", message="Username not found.", username=session["user_id"])
        else:  # Username exists, check pw
            user = conn.execute("SELECT * FROM users where user=?", (username,)).fetchone()
            print(user, user[0], user[1])
            if user[1] == password:
                session["user_id"] = user[0]
                print(session["user_id"],'test')
                return render_template("login.html", message=f"Logged in as {user[0]}.", username=session["user_id"])
            else:
                return render_template("login.html", message="Incorrect password, try again", username=session["user_id"])
    else:
        return render_template("login.html", username=session["user_id"])


@app.route('/update', methods=["POST", "GET"])
def update_settings():
    if session.get("user_id") is None:
        session["user_id"]=[]
    #Get current settings
    conn = sqlite3.connect('my_database.db')
    message = ''

    if request.method == 'POST':
        start_time = request.form.get('start_time').split(':')  # access the data inside 
        stop_time = request.form.get('stop_time').split(':')
        print(start_time)
        try:
            start_time = [int(i) for i in start_time]
            stop_time = [int(i) for i in stop_time]
            conn.execute("insert into settings(start, stop) values (?,?)", (str(start_time), str(stop_time)))
            conn.commit()
            message="Updated successfully"
            times = (start_time,stop_time)

        except:
            message = "Failed to split into datetime format, make sure to use format HH:MM:SS"
 
    settings = conn.execute("select start,stop from settings order by rowid DESC limit 1").fetchone()
    try:
        start = literal_eval(settings[0])
        stop = literal_eval(settings[1])
        start = datetime.time(start[0],start[1],start[2])
        stop = datetime.time(stop[0],stop[1],stop[2])

        current_settings = (str(start),str(stop))
        print(current_settings)
        conn.close()

        return render_template("update_settings.html", username=session["user_id"], settings=current_settings, message=message)
    except:
        return render_template("update_settings.html", username=session["user_id"], message=message)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


 