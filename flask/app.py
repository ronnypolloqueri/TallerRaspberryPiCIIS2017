from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET'])

def index():
    #return render_template('./index.html')
    return '<h1>Hola Flask desde ciis Tacna 2017</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
