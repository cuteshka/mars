from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    ast_username = StringField('id астронавта', validators=[DataRequired()])
    ast_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_username = StringField('id капитана', validators=[DataRequired()])
    cap_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     return redirect('/success')
    img = url_for('static', filename='img/emblem.jpg')
    css = url_for('static', filename='css/login_style.css')
    return render_template('login.html', title='Аварийный доступ', form=form, img=img, css=css)

# @app.route('/success')
# def login():
#     return render_template('success.html', title='Успешный вход')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')