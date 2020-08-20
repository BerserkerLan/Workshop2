from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
app.config.from_object('flask_config.Config')

app_id = "c1dea549"
app_key = "8f83f01b898c530248be5d7de38cda21"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/findByPostcode')
def find_by_postcode():
    postcode = request.values.get('postcode')
    postcode_url = "https://api.postcodes.io/postcodes/"
    postcode_url = postcode_url + postcode
    return requests.get(postcode_url)

    

if __name__ == '__main__':
    app.run()
