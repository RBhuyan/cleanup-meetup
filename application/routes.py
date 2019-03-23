from flask import render_template, flash, redirect, url_for, request, send_file, make_response
from application import app, bootstrap
import geocoder
import json

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    g = geocoder.ip('me')
    print(g.json)
    print(g.latlng)
    data_list = []
    data_list.append(g.latlng[0])
    data_list.append(g.latlng[1])
    #Following 2 parameters are just testing placeholders
    data_list.append("Dummy Event Name")
    data_list.append("Dummy Event ID")
    print(json.dumps(data_list))
    return render_template('home.html')
