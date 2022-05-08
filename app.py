from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    datos_obtenidos = requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    datos = datos_obtenidos.json()

    return render_template('index.html', datos=datos['list'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
