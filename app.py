from flask import Flask, render_template 

app = Flask(__name__)


app.route('/')
def home():
    return render_template('index.html') 


app.route('/form1nico')
def formpage():
    return render_template('form1nico') 