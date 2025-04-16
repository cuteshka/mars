from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/distribution')
def distribution():
    people = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Ванката Капур", "Тедди Сандерс"]
    return render_template('distribution.html', people=people)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')