from flask import Flask, render_template, redirect, request, flash
from firebase import firebase
import requests
import json
import creds

app = Flask(__name__)
app.secret_key = creds.SECRET_KEY

firebase = firebase.FirebaseApplication(creds.FIREBASE_URL, None)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.route('/sign_up', methods=['POST'])
def sign_up():
	email = request.form.get("email")

	result = firebase.post('/emails', data={"email":email}, params={'print': 'pretty'})

	flash("We'll keep you in the loop.")
	return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)

