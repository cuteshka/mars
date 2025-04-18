from flask import Flask, url_for

app = Flask(__name__)

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    from flask import request
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                  filename='css/style1.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align=center>Анкета претендента</h1>
                            <h2 align=center>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder=
                                    "Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя"
                                     name="name">
                                    <div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                         placeholder="Введите адрес почты" name="email">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                          <option>Кандидат наук</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Какие у вас есть профессии?</label>
                                        </div>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                   <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male"
                                           checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female"
                                           value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться
                                         на Марсе?</label>
                                        <label for="classSelect"></label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                    </div>
                                </form>
                            </div>
                          </body>
                        </html>'''
    # elif request.method == 'POST':
    #     print(request.form['email'])
    #     print(request.form['password'])
    #     print(request.form['class'])
    #     print(request.form['file'])
    #     print(request.form['about'])
    #     print(request.form['accept'])
    #     print(request.form['sex'])
    #     return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')