import resources as res
from flask import Flask, request, abort, redirect,url_for
app = res.app
@app.route('/api/web-bot/dividir',methods=['POST'])
def dividir():
	print ("dividiendo")
	if request.method == 'POST' and request.form.has_key('op1') and request.form.has_key('op2'):
		divide = float(request.form['op1'])/float(request.form['op2'])
		return "El cociente es "+str(divide)
	else:
		abort(400)

if __name__ == '__main__':
	app.run()
