from flask import Flask, render_template, request
from pibot import mover_adelante, mover_derecha, mover_izquierda, mover_retro, mover_parar, setup_motor

app = Flask(__name__)
setup_motor()

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    print(comando)

    if(comando == 'w'):
        mover_adelante()
    if(comando == 'a'):
        mover_derecha()
    if(comando == 'd'):
        mover_izquierda()
    if(comando == 's'):
        mover_retro()
    if(comando == 'q'):
        mover_parar()

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
