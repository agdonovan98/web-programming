#serves as the basis for all other code
from bottle import route, get, post 
from bottle import run, debug
from bottle import request, response, redirect, template
from bottle import static_file
import dataset
import json
from bottle import default_app
import random
import string
import hashlib
import os
import codecs
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#encrypts passwords, storing them securely
def bytes_to_str(b):
    s = str(codecs.encode(b,"hex"),"utf-8")
    assert type(s) is str
    return s

def str_to_bytes(s):
    b = codecs.decode(bytes(s,"utf-8"),"hex")
    assert type(b) is bytes
    return b

def generate_credentials(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    print(salt)
    print(key)
    return {
        'salt':bytes_to_str(salt), 
        'key' :bytes_to_str(key),
    }

def verify_password(password, credentials):
    salt = str_to_bytes(credentials['salt'])
    key  = str_to_bytes(credentials['key'])
    print(salt)
    print(key)
    new_key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    return new_key == key

def write(key, data):
    assert type(data) is dict
    with open(f"data/session.{key}.json", "w") as f:
        json.dump(data,f)
    return

def read(key):
    with open(f"data/session.{key}.json", "r") as f:
        data = json.load(f)
    assert type(data) is dict
    return data

def create_token(k=32):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))

#generates sessions for new and returning users accessing atlas
def new_session_id():
    return create_token()

def get_session(request):
    
    def new_session():
        session_id = new_session_id()
        print("new session id = ", session_id)
        session = {
            "session_id" : session_id,
            "username" : ''
        }
        return session

    session_id = request.get_cookie("session_id", default=None)
    if session_id == None:
        session = new_session()
    else:
        try:
            session = read(session_id)
        except: 
            session = new_session()
    print("loaded session = ", [session])
    return session

#keeps users logged in
def save_session(response, session):
    write(session['session_id'], session)
    print("saved session = ",[session])
    response.set_cookie("session_id", session['session_id'], path="/")

def get_user(name):
    try:
        with open(f"data/user.{name}.json", "r") as f:
            data = json.load(f)
        assert type(data) is dict
        return data
    except:
        return None

def save_user(name, data):
    assert type(data) is dict
    with open(f"data/user.{name}.json", "w") as f:
        json.dump(data,f)
    return
    print("saved user = ",[name])

#directs returning users to login page
@get("/login")
def get_login():
    return template("login")

@post("/login")
def post_login():
    session = get_session(request)
    username = request.forms.get('username')
    password = request.forms.get('password')
    user = get_user(username)
    if not user:
        print("invalid user")
        return redirect('/signup')
    if 'credentials' not in user:
        print("credentials missing")
        return redirect('/signup')
    if not verify_password(password, user['credentials']):
        print('failed verification')
        return redirect('/')
    print("login successful")
    session['username'] = username
    save_session(response, session)
    return redirect('/')

#sends email to verify user identity when creating account
def send_verification_email(username):
    user = get_user(username)
    if not user:
        print("failure to find user")
        return
    print(user)
    email = user['email']
    token = create_token()
    user['token'] = token
    save_user(username, user)
    print('user information with token has been saved')

    verify_url = f"http://localhost:8082/verify/{token}"

    # send_message(email, message)
    sender = "<app@example.com>"
    receiver = f"{username}<{email}>"

    text = f"""\
        Please verify your email by visiting this page in your browser. 
        
        {verify_url}

        Thanks! 

        - Team Atlas
    """

    html = f"""\
        <html>
        <body>
        <p>Please verify your email by clicking here.<br/></p>

        <p><a href="{verify_url}">{verify_url}</a><br/></p>

        <p>-Thanks!<br>- Team Atlas/></p>
        </body>
        </html>
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = "Please verify your email"
    message["From"] = sender
    message["To"] = receiver

    message.attach(MIMEText(text,"plain"))
    message.attach(MIMEText(html,"html"))

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("4e83cff9aba69f", "988d5260c1b156")
        server.sendmail(sender, receiver, message.as_string())

    return

#sends email to verify user identity when resetting password
def send_reset_email(username):
    user = get_user(username)
    if not user:
        print("failure to find user")
        return
    print(user)
    email = user['email']
    token = create_token()
    user['reset_token'] = token
    save_user(username, user)
    print('user information with reset token has been saved')

    reset_url = f"http://localhost:8082/reset/{username}/{token}"

    # send_message(email, message)
    sender = "<app@example.com>"
    receiver = f"{username}<{email}>"

    text = f"""\
        Please reset your password by visiting this page in your browser. 
        
        {reset_url}

        Thanks! 

        - Team Atlas
    """

    html = f"""\
        <html>
        <body>
        <p>Please reset your password by clicking here.<br/></p>

        <p><a href="{reset_url}">{reset_url}</a><br/></p>

        <p>Thanks!<br>- Team Atlas/></p>
        </body>
        </html>
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = "Password reset request"
    message["From"] = sender
    message["To"] = receiver

    message.attach(MIMEText(text,"plain"))
    message.attach(MIMEText(html,"html"))

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("4e83cff9aba69f", "988d5260c1b156")
        server.sendmail(sender, receiver, message.as_string())

    return

#directs new users to registration page
@get("/signup")
def get_signup():
    return template("signup")

@post("/signup")
def post_signup():
    session = get_session(request)
    username = request.forms.get('username')
    password = request.forms.get('password')
    password_confirm = request.forms.get('password_confirm')
    email = request.forms.get('email')
    if password != password_confirm:
        #TODO: suitable message in session
        save_session(response, session)
        return redirect('/')    
    save_user(username, {
        'username':username,
        'credentials':generate_credentials(password),
        'email':email,
        'email_verified':False
    })
    send_verification_email(username)
    session['username'] = username
    #TODO: suitable message in session
    save_session(response, session)
    return redirect('/')

#verifies user's identity
@get("/verify/<token>")
def get_verify(token):
    session = get_session(request)
    username = session['username']
    user = get_user(username)
    print(token)
    print(user)
    if token == user['token']:
        user['email_verified'] = True
        save_user(username, user)

#allows users to reset their passwords
@get("/forgot")
def get_signup():
    return template("forgot")

@post("/forgot")
def post_signup():
    session = get_session(request)
    username = request.forms.get('username')
    user = get_user(username)
    if user['email_verified']:
        send_reset_email(username)
    return redirect('/')

@get("/reset/<username>/<reset_token>")
def get_reset(username, reset_token):
    session = get_session(request)
    session['csrf_token'] = create_token()
    user = get_user(username)
    print(reset_token)
    print(user)
    if reset_token == user['reset_token']:
        save_session(response, session)
        return template("reset", username=username, reset_token=reset_token, csrf_token=session['csrf_token'])
    return redirect('/')

@post("/reset/<username>/<reset_token>")
def post_reset(username, reset_token):
    session = get_session(request)
    if 'csrf_token' not in session:
        redirect('/')
    # check the csrf token
    if request.forms.get('csrf_token') != session['csrf_token']:
        redirect('/')
    session['csrf_token'] = None
    user = get_user(username)
    print(reset_token)
    print(user)
    if reset_token != user['reset_token']:
        return redirect('/')
    user['reset_token'] = None
    # get new password
    password = request.forms.get('password')
    password_confirm = request.forms.get('password_confirm')
    if password != password_confirm:
        #TODO: suitable message in session
        save_session(response, session)
        return redirect('/') 
    user['credentials'] == generate_credentials(password)  
    save_user(username, user)
    return redirect('/login')

#logs user out of session
@get("/logout")
def get_logout():
    session = get_session(request)
    session['username'] = ''
    save_session(response, session)
    return redirect('/')

#links to css file in static
@route("/static/css/<filename:re:.*\.css>")
@route("/content/<filename:re:.*\.css>")
def get_css(filename):
    return static_file(filename=filename, root="static/content", mimetype="content/css")

#links to images in static
@route("/static/png/<filename:re:.*\.png>")
@route("/image/<filename:re:.*\.png>")
def get_image(filename):
    return static_file(filename=filename, root="static/images", mimetype="image/png")

@route("/static/<filename:path>")
def get_static(filename):
    return static_file(filename=filename, root="static")

#links to javascript drawing
@route("/drawing")
def get_drawing():
    return template('drawing')

#loads home page
@route("/")
def get_atlas_list():
    session = get_session(request)
    print("session = ", [session])
    username = session['username']
    atlas_list_db = dataset.connect('sqlite:///atlas_list.db')
    atlas_table = atlas_list_db.get_table('atlas')
    items = atlas_table.find()
    items = [ dict(x) for x in list(items) if x['user'] == username ]
    tpl = template("home", items=items, message="Logged in as " + username, status=None)
    save_session(response, session)
    return tpl

#allows users to insert new locations to atlas
@get("/insert")
def get_insert():
    global message
    message = "A place was added."
    return template("insert")

@post("/insert")
def post_insert():
    place = request.forms.get('place')
    print("place=", place)
    date = request.forms.get('date')
    print("date=", date)
    comments = request.forms.get('comments')
    print("comments=", comments)
    try:
        atlas_list_db = dataset.connect('sqlite:///atlas_list.db')
        atlas_table = atlas_list_db.get_table('atlas')
        atlas_table.insert({
            'place' : place.strip(),
            'date' : date.strip(),
            'comments' : comments.strip()
        })
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return redirect('/')

#allows users to edit locations already entered into atlas
@get("/edit/<id>")
def get_edit(id):
    try:
        atlas_list_db = dataset.connect('sqlite:///atlas_list.db')
        atlas_table = atlas_list_db.get_table('atlas')
        items = list(atlas_table.find(id=id))
        if len(items) != 1:
            response.status="404 Not Found:"+str(id)
            return
        items = [ dict(x) for x in items ]
        print(items)
        print(items[0])
    except Exception as e:
        print(e)
        response.status="409 Bad Request:"+str(e)
        return

    return template("edit", item=items[0])

@post("/edit")
def post_edit():
    id = request.forms.get('id')
    id = int(id)
    place = request.forms.get('place')
    print("place=", place)
    date = request.forms.get('date')
    print("date=", date)
    comments = request.forms.get('comments')
    print("comments=", comments)
    try:
        atlas_list_db = dataset.connect('sqlite:///atlas_list.db')
        atlas_table = atlas_list_db.get_table('atlas')
        atlas_table.update({
            'id' : id,
            'place' : place.strip(),
            'date' : date.strip(),
            'comments' : comments.strip()
        }, ['id'])
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return redirect('/')

#allows users to delete locations in atlas
@route("/delete/<id>")
def get_delete(id):
    id = int(id)
    try:
        atlas_list_db = dataset.connect('sqlite:///atlas_list.db')
        atlas_table = atlas_list_db.get_table('atlas')
        print(f"Time to delete #{id}.")
        atlas_table.delete(id=id)
    except Exception as e:
        response.status="409 Bad Request:"+str(e)
        return
    return template("deleted", id=id)

@route('/restricted')
def restricted_area():
    username = request.get_cookie("username")
    if username:
        return template("Welcome back, {{name}}!", name=username)
    else:
        return "Access denied. Please log in and try again."

#launches server
if __name__ == "__main__":
    debug(True)
    run(host="localhost", port=8082)
else:
    application = default_app()