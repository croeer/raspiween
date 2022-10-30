from bottle import route, run, template, request, redirect
import os

@route('/hello/<name>')
def index(name):
    return template('<b>Huello {{name}}</b>!', name=name)

@route('/play/<index>')
def index(index):
    soundfile = 'sounds/sound' + str(index) + '.wav'
    os.system(' aplay -D bluealsa:DEV=00:1D:DF:6E:F5:C3,PROFILE=a2dp ' + soundfile)
 
    redirect("/")

@route('/')
def index():

    return template('main.tpl')

run(host='localhost', port=8080)