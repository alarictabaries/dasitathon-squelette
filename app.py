from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'dasitathon'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    file = request.files.get('file')
    filename = file.filename if file else None

    # vous pouvez implémenter votre traitement ici

    # vous pouvez stocker les résultats dans la session
    # par exemple, la variable text stocke le texte saisi par l'utilisateur
    session['text'] = text
    session['filename'] = filename

    return redirect(url_for('result'))

@app.route('/result')
def result():
    # vous récupérez les résultats stockés dans la session
    text = session.get('text', '')
    filename = session.get('filename', '')
    pdf_text = session.get('pdf_text', '')
    # et vous les passez au template pour pouvoir les afficher
    return render_template('result.html', text=text, filename=filename)


if __name__ == '__main__':
    app.run(debug=True)