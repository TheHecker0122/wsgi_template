from flask import Flask, render_template, redirect, request, session
import os
import uuid
import random


_dir = os.getcwd()

html = _dir + '/html'
static = _dir + '/css'

app = Flask(__name__, static_folder=static, template_folder=html)


sk = uuid.uuid4().hex + str(random.randint(0,99999999999))
app.secret_key = 'sk-'+sk


def index():
    
    if request.method == "GET":
        return render_template('index.html')
    
    
    if request.method == "POST":
        name = request.form.get('name')
        famil = request.form.get('famil')
        email = request.form.get('email')
        phone = request.form.get('phone')



        print(f'Клиент отправил данные!\nИмя:{name}\nФамилия:{famil}\nEmail:{email}\nTelephone:{phone}')
        return render_template('index.html')

def about():
    return render_template('about.html')

def login():
    if request.method == "GET":
        return render_template('login.html')
    
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('pass')
        print(f'Пользователь {login} ввел пароль {password}')


        return render_template('login.html')


app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/about', 'about', about, methods=['GET'])


if __name__ == '__main__':
    
    app.run(debug=True)
