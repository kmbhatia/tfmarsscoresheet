from flask import Flask, render_template, request, redirect, session
from flask_wtf import FlaskForm

from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
	if request.method == 'POST':
		form =request.form
		formdict =  form.to_dict(flat=False)
		formdict2 = dict((k, [(int(str(s))) for s in v][0]) for k,v in formdict.items())

		#print(formdict2[tr1])
		formdict2['total1'] = int(request.form.get("terraformrating1"))+int(request.form.get("award1"))+int(request.form.get("milestone1"))+int(request.form.get("gameboard1"))+int(request.form.get("cards1"))
		formdict2['total2'] = int(request.form.get("terraformrating2"))+int(request.form.get("award2"))+int(request.form.get("milestone2"))+int(request.form.get("gameboard2"))+int(request.form.get("cards2"))
		formdict2['total3'] = int(request.form.get("terraformrating3"))+int(request.form.get("award3"))+int(request.form.get("milestone3"))+int(request.form.get("gameboard3"))+int(request.form.get("cards3"))
		scoreitems =['TerraformRating','Award', 'Milestone','Gameboard','Cards']

		print(formdict2)
		return render_template("submit.html", form=formdict2, scoreitems=scoreitems)


					

