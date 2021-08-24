from flask import Blueprint ,render_template
auth=Blueprint("auth",__name__)

@auth.route("/signup")
def signup():
    return "Sign UP"

@auth.route("/login")
def login():
    return "Login"

@auth.route("/logout")
def logout():
    return "Logout"