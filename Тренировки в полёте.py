from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    if 'инженер' in prof or "строитель" in prof:
        training_type = "Инженерные тренажеры"
        pict = url_for('static', filename='img/schemeИТ.jpg')
    else:
        training_type = "Научные симуляторы"
        pict = url_for('static', filename='img/schemeHC.jpg')
    return render_template('training.html', training_type=training_type, pict=pict)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
