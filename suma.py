import resources as res
from flask import Flask, request, abort, redirect,url_for
app = res.app
@app.route('/api/web-bot/sumar',methods=['POST'])
def sumar():
	print ("sumando")
	if request.method == 'POST' and request.form.has_key('op1') and request.form.has_key('op2'):
		suma = float(request.form['op1'])+float(request.form['op2'])
		return "La suma es "+str(suma)
	else:
		abort(400)

if __name__ == '__main__':
	app.run()
