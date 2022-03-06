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
		print(request.form.to_dict())
		scorecomponent = ['tr','award', 'milestone', 'gameboard', 'cards']
		total = []
		players = ['aashish','karan','mohit']

		#{'tr1': '1', 'tr2': '1', 'tr3': '1', 'award1': '1', 'award2': '1', 'award3': '1', 'milestone1': '1', 'milestone2': '1', 'milestone3': '1', 'gameboard1': '1', 'gameboard2': '1', 'gameboard3': '1', 'cards1': '1', 'cards2': '1', 'cards3': '1'}

		for player in players:
			for i in range(1,4):
				for component in scorecomponent:
					key=component+str(i)
					try:
						playername = player
						if() 


		total1 = int(req.get("tr1"))+int(req.get("award1"))+int(req.get("milestone1"))+int(req.get("gameboard1"))+int(req.get("cards1"))
		total2 = int(req.get("tr2"))+int(req.get("award2"))+int(req.get("milestone2"))+int(req.get("gameboard2"))+int(req.get("cards2"))
		total3 = int(req.get("tr3"))+int(req.get("award3"))+int(req.get("milestone3"))+int(req.get("gameboard3"))+int(req.get("cards3"))

      # try:
      #    nm = request.form['nm']
      #    addr = request.form['add']
      #    city = request.form['city']
      #    pin = request.form['pin']
         
      #    with sql.connect("database.db") as con:
      #       cur = con.cursor()
      #       cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
      #       con.commit()
      #       msg = "Record successfully added"
      # except:
      #    con.rollback()
      #    msg = "error in insert operation"
      
      # finally:
      #    return render_template("result.html",msg = msg)
      #    con.close()
	return render_template("submit.html", t1=total1, t2=total2, t3=total3)