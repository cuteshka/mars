from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
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
                            <link rel="stylesheet" type="text/css" href="{url_for(
            'static', filename='css/load_photo_style.css')}" />
                            <title>Отбор космонавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h3>для участия в миссии</h3>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Приложите фотографию </label>
                                    <h4></h4>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                    <h4></h4>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''

    elif request.method == 'POST':

        file = request.files['file'].read()
        form = request.files['file'].filename.split('.')[-1]
        with open(f'static/img/img.{form}', 'wb') as f:
            f.write(file)
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for(
            'static', filename='css/load_photo_style.css')}" />
                            <title>Отбор космонавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h3>для участия в миссии</h3>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Приложите фотографию </label>
                                     <h4></h4>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                     <h4></h4>
                                </div>
                                <img src="/static/img/img.{form} " alt="здесь должна была быть ваша картинка">
                                <div>
                                 <h4></h4>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                                </div>
                                
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
