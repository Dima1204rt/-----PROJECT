from flask import Flask, render_template, request, redirect # импортируем фреймворк Flask для работы с простейшим веб-приложением и выбираем доп функции которые нам нужны
from app import App
import json

server = Flask(__name__, template_folder='templates') # создаем приложение сервера фласка
app = App()

@server.route('/') # декоратор (@ то что выполняется до запуска функция) при запуске сервера при вязывает функцию on_main главной странице
def on_main(): # создаем какую-то функцию 
    return render_template('index.html') # то что увидит пользователь

    
@server.route('/api/result')
def on_number():
    data=request.json
    return app.check_result(data['result'])

@server.route('/api/generate', methods=['POST'])
def on_generate():
    data=json.loads(request.data.decode())
    result=app.generate(data.get('sys'), data.get('direction'))
    app.convert(data.get('sys'), data.get('direction'))
    return {
        'result': result
        }

@server.route('/api/check', methods=['POST'])   
def on_check():
    data=json.loads(request.data.decode())
    return {
        'result': app.check(data.get('user_ans'))
        }


if __name__ == '__main__': # запускаем приложение если запущен server.py (защита от запуска через import)
    server.run('0.0.0.0', 4783, True) # запускаем приложения и указываем хост и порт для доступа из локальной сети