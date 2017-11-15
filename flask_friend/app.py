from flask import Flask, render_template, request
from automate import inicializarBoard, definirPinoSalida, escribirPuerto

app = Flask(__name__)

inicializarBoard()
definirPinoSalida(7)
definirPinoSalida(11)

@app.route('/', methods=['GET'])
def index():
    return render_template('formulario.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    print(comando)

    if(comando == '1ON'):
       escribirPuerto(7,0) 
    if(comando == '1OFF'):
       escribirPuerto(7,1)
    if(comando == '2ON'):
       escribirPuerto(11,0)
    if(comando == '2OFF'):
       escribirPuerto(11,1)

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
