import resources as res
from flask import Flask, request, abort, redirect,url_for
import requests
app = res.app
@app.route('/api/web-bot/temperature', methods=['POST'])
def temperature():
    city = request.form['city']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+',us&appid=fd38d62aa4fe1a03d86eee91fcd69f6e')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    #temp_f = (temp_k - 273.15) * 1.8 + 32
    temp_c = temp_k-273.15
    return 'La temperatura en '+city+' es '+str(temp_c)+' Grados centigrados '

if __name__ == '__main__':
	app.run()