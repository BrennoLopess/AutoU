from flask import Flask, render_template, request
from models.zero_shot_classifier import classify_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inicio')
def index():
    return render_template('index.html')

@app.route('/analise', methods=['GET', 'POST'])
def analise():
    if request.method == 'POST':
        texto = request.form.get('texto', '')
        resultado = classify_text(texto)
        return render_template('analysis.html', resultado=resultado, texto=texto)
    else:
        return render_template('analysis.html', resultado=None, texto=None)

if __name__ == '__main__':
    app.run(debug=True)
