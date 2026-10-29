from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/form1nico', methods=['GET', 'POST'])
def formpage():
    selected_brand = request.form.get('brand') if request.method == 'POST' else None
    return render_template('form1nico.html', selected_brand=selected_brand)