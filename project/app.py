from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', game_id = 111)


@app.route("/submit", methods=["GET","POST"])
def submit():
	if request.method == 'POST':
		req = request.form
		print(request.form)
		

		total1 = req.get("tr1")+req.get("award1")+req.get("milestone1")+req.get("gameboard1")+req.get("cards1")
		print(total1)
		return redirect(request.url)

	return render_template("submit.html")
