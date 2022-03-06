from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route("/submit", methods=["GET","POST"])
def submit():
	if request.method == 'POST':
		req = request.form
		print(request.form)


		total1 = int(req.get("tr1"))+int(req.get("award1"))+int(req.get("milestone1"))+int(req.get("gameboard1"))+int(req.get("cards1"))
		total2 = int(req.get("tr2"))+int(req.get("award2"))+int(req.get("milestone2"))+int(req.get("gameboard2"))+int(req.get("cards2"))
		total3 = int(req.get("tr3"))+int(req.get("award3"))+int(req.get("milestone3"))+int(req.get("gameboard3"))+int(req.get("cards3"))
		
	return render_template("submit.html", t1=total1, t2=total2, t3=total3)