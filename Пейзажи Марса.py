from flask import Flask, url_for

app = Flask(__name__)

@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
    <html lang="ru">
    <head>
        <!-- Required meta tags -->
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" 
                  integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" 
                  crossorigin="anonymous">
        <title>Пейзажи Марса</title>
    </head>
    <body>
    <h1 align=center>Пейзажи Марса</h1>
    <div class="container">
            <div id="carousel-basic" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                    <li data-target="carousel-basic" data-slide-to="1"></li>
                    <li data-target="carousel-basic" data-slide-to="2"></li>
                    <li data-target="carousel-basic" data-slide-to="3"></li>
                </ol>
                <div class="carousel-inner" role="listbox">
                    <div class="carousel-item active">
                        <img src="{url_for('static', filename='img/mars1.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/mars2.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/mars3.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                    </div>
                    <div class="carousel-item">
                        <img src="{url_for('static', filename='img/mars4.jpg')}" class="d-block w-100" alt="" class="img-fluid">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Назад</span>
                </a>
                <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Вперед</span>
                </a>
            </div>
        </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" 
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" 
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" 
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')