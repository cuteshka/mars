from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    if sex == "male" and age <= 21:
        color = "boy_color.JPG"
        photo = "boy.JPG"
    elif sex == "male" and age > 21:
        color = "man_color.JPG"
        photo = "man.JPG"
    elif sex == "female" and age > 21:
        color = "woman_color.JPG"
        photo = "woman.JPG"
    elif sex == "female" and age <= 21:
        color = "girl_color.JPG"
        photo = "girl.JPG"
    room_color = url_for("static", filename=f"img/{color}")
    pict = url_for("static", filename=f"img/{photo}")
    css = url_for("static", filename="css/room_style.css")
    return render_template('room_decoration.html', room_color=room_color, pict=pict, css=css)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
