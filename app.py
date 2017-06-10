#!flask/bin/python

from flask import Flask, request, abort, redirect,url_for,jsonify,flash
from pymongo import MongoClient
import random
import datetime
import sys
import os
import resources as res
import importlib



importlib.reload(sys)
#sys.setdefaultencoding('utf-8')
#conexion mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.robotExample
app = res.app


UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['py'])  # conjunto de extension de archivo permitida .py.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #Aqui es el folder se almacenará los archivos subidos
l_conoc = [] #matriz donde se inserta elConocimiento

def allowed_file(filename): #revisa si la extesion es valida
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def cargar_conocimientos():
	print ("Cargando conocimientos....")
	rs_conoc = db['conocimientos'].find({},{'nombre':1,'_id':0})  #datos(documentos) de la collection de 'conocimientos'.
	for rs in rs_conoc: # recorre los conocimientos
		print (rs)
		try:
			conocim = __import__(rs['nombre'])
			l_conoc.append(conocim) #introduce el conocimiento en el arreglo
		except:
			pass



@app.route('/api/web-bot/mostrar/estados',methods=['GET'])
def mostrar_estados():
	los_estados = [] #matriz que almacena los estados
	res_estados = db['estados'].find({}) # datos(documentos) de la collection de 'estados'.
	for rst in res_estados: #ciclo que recorre los documentos de 'estados'
		los_estados.append(rst)  # una vez se recorre el ciclo se insertan datos en matriz l_estados
	return jsonify({'estados':los_estados}) #retorna los estados em formato json



@app.route('/api/web-bot/mostrar/memoria',methods=['GET'])
def mostrar_memorias():
	la_memoria = [] #matriz que almacena la memoria
	res_conoc = db['conocimientos'].find({}) # datos(documentos) de la collection de 'conocimientos'.
	for rst in res_conoc: #ciclo que recorre los documentos de 'conocimientos'
		la_memoria.append(rst) # una vez se recorre el ciclo se insertan datos en matriz l_memoria
	return jsonify({'conocimientos':la_memoria})#muesta memoria(conocimiento) bot



@app.route('/api/web-bot/mostrar/desaprender/<userid>/<nombre>',methods=['DELETE'])
def desaprender(userid,nombre):
    estado = {
		'_id':random.getrandbits(16), # genera random hash(16)
		'user':userid,
		'date':datetime.datetime.now(),
		'action':'desaprender('+nombre+')'
	}
    db['conocimientos'].delete_one({'nombre':nombre}) # elimina el 'conocimiento' de esa collection que referencia el documento nombre
    db['estados'].insert(estado) # inserta el log(info desaprendida) en collection estados
    return 'Conocimiento desaprendido. Permanecera disponible hasta que se reinicie el servidor.'''



@app.route('/api/web-bot/aprender', methods=['POST'])
def upload_file():
	#Para aprender,primero subimos el fichero donde esta la funcion de aprendizaje.
    if request.method == 'POST' and request.form.has_key('nombre') and request.form.has_key('user') and request.form.has_key('creador'):
        #Compruebe si la solicitud de POST tiene la parte de archivo
        print (request.files)
        print (request.form)
        print (request.form.keys())
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Si el usuario no selecciona el archivo, el navegador también envía una parte vacía sin nombre de archivo
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print ("Fichero subido...")
            conocimiento = {}
            vNombre = request.form['nombre']
            vCreador = request.form['creador']
            vUser = request.form['user']
            print (vNombre, vCreador)
            #Ahora que ya se tiene  el fichero, cargamos los datos en base de datos
            conocimiento = {
            	'_id':random.getrandbits(16), #ramdom hash(16)
				'nombre':vNombre,
				'creador':vCreador,
				'fecha': datetime.datetime.now()
			}
            estado = {
				'_id':random.getrandbits(16),
				'user':vUser,
				'date':datetime.datetime.now(),
				'action':'aprender: '+request.form['nombre']+' ('+file.filename+')'

			}
            db['conocimientos'].update({'nombre':conocimiento['nombre']},conocimiento,upsert=True)
            db['estados'].insert(estado) #inserto en la collection 'estados' el log del user
            return '''Conocimiento adquirido. Disponible la proxima vez que se reinicie el servidor'''

    else:
    	abort(400)


if __name__ == '__main__':
	cargar_conocimientos() #Carga conocimientos cuando se inicia el server
	app.run()
