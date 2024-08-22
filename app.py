from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # O Flask no ambiente de produção deve usar o servidor WSGI e a porta configurada pelo Render.
    port = int(os.environ.get('PORT', 5000))  # Porta padrão 5000 se não estiver definida
    app.run(host='0.0.0.0', port=port)
