from flask import Flask, render_template, request, redirect, session
from flask_wtf import FlaskForm

from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		elementarray = ['terraformrating','award','milestone','gameboard','cards']
		return render_template('index2.html', playercount=int(request.form.get('playercount')), elementarray=elementarray)

@app.route('/submit', methods=['GET','POST'])
def submit():
	if request.method == 'POST':
		print(request.form)
		formdict =  request.form.to_dict(flat=False)
		formdict2 = dict((k, [((str(s))) for s in v][0]) for k,v in formdict.items())
		print(formdict2)
		playercount = int(len(formdict2.keys())/5)
		scoreitems =['TerraformRating','Award', 'Milestone','Gameboard','Cards']

		return render_template("submit.html", form=formdict2, scoreitems=scoreitems, playercount=playercount)

#ImmutableMultiDict([('player1', 'karan'), ('terraformrating1', '1'), ('award1', '1'), ('milestone1', '1'), ('gameboard1', '1'), ('cards1', '1'), ('player2', 'aashish'), ('terraformrating2', '1'), ('award2', '1'), ('milestone2', '1'), ('gameboard2', '1'), ('cards2', '1')])

#{'terraformrating1': 1, 'award1': 1, 'milestone1': 1, 'gameboard1': 1, 'cards1': 1, 'terraformrating2': 1, 'award2': 1, 'milestone2': 1, 'gameboard2': 1, 'cards2': 1}
