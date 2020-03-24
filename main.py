from flask import Flask,request,render_template,redirect,session
from controller import MainController
from database_connector import dao
import smtplib
import twilio
from twilio.rest import Client

app = Flask(__name__,static_url_path='')

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
smtpObj.login('Your Email Id','Your Password')


acc= "Your Twilio Account "
token = "Your Twilio Account token"
twilioClient = Client(acc,token)

MainController.MainController(app, request, dao, render_template,redirect,session,smtpObj)

UPLOAD_FOLDER = 'datasets'
app.secret_key = '12344sefsrfsrg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__=='__main__':
    app.run('localhost',debug=True)
