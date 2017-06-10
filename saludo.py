import resources as res
app = res.app
@app.route('/api/web-bot/saludar')
def index():
	return "Hello World!!!"