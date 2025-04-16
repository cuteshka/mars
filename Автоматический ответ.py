from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/auto_answer')
@app.route('/answer')
def list_prof():
    info = {'Фамилия': 'Watny', 'Имя': 'Mark', 'Образование': 'выше среднего',
              'Профессия': 'штурман марсохода', 'Пол': 'мужской', 'Мотивация': 'Вcегда мечтал застрять на Марсе',
              'Готов остаться на Марсе?': 'True'}
    css_file = url_for("static", filename='css/answer_style.css')
    return render_template('auto_answer.html', title="Анкета", info=info, css=css_file)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')