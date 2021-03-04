from flask import Flask, request, render_template, jsonify, abort, redirect, url_for
import json
import flag
import pycountry
from form import MyForm

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'independence-day'
countries = list(pycountry.countries)
with open('day.json', 'r') as f:
    days = json.load(f)

def get_key(val):
    for key, value in days.items():
        if val in value:
            return key
    return None

@app.route('/', methods=['GET','POST'])
def index():
    form = MyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            country = request.form['country']
            return redirect(url_for('get_day', country=country))
    return render_template('index.html', form=form)

@app.route('/api/<string:country>')
def get_day(country):
    iso = ""
    date = get_key(country)
    data = {"message":"Country not found"}
    if date is not None:
        for i in countries:
            if country.title() == i.name:
                iso += i.alpha_2
                data = {"Day": date, "Unicode flag": flag.flag(iso)}
                return jsonify(data), 200
    else:
            return jsonify(data), 404

@app.errorhandler(404)
def page_not_found(e):
    data = {"message":"Country not found"}
    return jsonify(data), 404

if __name__ == '__main__':
    app.run(port=5008)
