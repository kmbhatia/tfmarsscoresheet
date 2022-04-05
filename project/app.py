from flask import Flask, render_template, request, redirect, session, Blueprint
from flask_wtf import FlaskForm


bp = Blueprint('urlshort',__name__)

@bp.route('/home', methods=['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')

@bp.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		elementarray = ['terraformrating','award','milestone','gameboard','cards']
		return render_template('index2.html', playercount=int(request.form.get('playercount')), elementarray=elementarray)

@bp.route('/submit', methods=['GET','POST'])
def submit():
	if request.method == 'POST':
		print(request.form)
		formdict =  request.form.to_dict(flat=False)
		formdict2 = dict((k, [((str(s))) for s in v] [0] ) for k,v in formdict.items())
		print(formdict2)
		playercount = int(len(formdict2.keys())/5)
		for x in range(playercount-1):
			formdict2['total'+str(x+1)] = int(request.form.get("terraformrating"+str(x+1)))+int(request.form.get("award"+str(x+1)))+int(request.form.get("milestone"+str(x+1)))+int(request.form.get("gameboard"+str(x+1)))+int(request.form.get("cards"+str(x+1)))
			print(formdict2['total'+str(x+1)])
		scoreitems =['TerraformRating','Award', 'Milestone','Gameboard','Cards', 'Total']

		return render_template("submit.html", form=formdict2, scoreitems=scoreitems, playercount=playercount)


