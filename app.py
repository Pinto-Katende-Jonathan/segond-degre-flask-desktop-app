from flask import Flask, request, render_template, jsonify
import time
import webview

app = Flask(__name__)

window = webview.create_window('Katende app',app,width= 1200, height=700, confirm_close=True)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('segond.html')

@app.route('/output', methods=['GET','POST'])
def segond():
	try:
		a = request.json['nb1']
		b = request.json['nb2']
		c = request.json['nb3']

		if a=='' or b=='' or c=='': 
			time.sleep(1)
			return jsonify('Veuillez remplir tous les champs')

		else:
			a = float(request.json['nb1'])
			b = float(request.json['nb2'])
			c = float(request.json['nb3'])

			delta = (b**2)-4*a*c
			
			if a==0:
				time.sleep(1)
				return jsonify("a doit etre different de 0")
			elif delta < 0 :
				time.sleep(1)
				return jsonify('Pas de solution reelle')
			elif delta==0 :
				time.sleep(1)
				return jsonify(f"X1 = X2 = {round(-b/(2*a),2)}")
			else:
				time.sleep(1)
				return jsonify(f" X1 = {round((-b+delta**0.5)/(2*a),2)} et X2 = {round((-b-delta**0.5)/(2*a),2)}")
	except :
		time.sleep(1)
		return jsonify('Veuillez respecter le format')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def error_server(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	#app.run(debug=True)
    webview.start()