from flask import Blueprint, render_template, request, session, redirect, jsonify


# 创建蓝图
account = Blueprint('account', __name__)

mess_dict = {1: {'name': '张三', 'age': 18},
             2: {'name': '李四', 'age': 28},
             3: {'name': '王五', 'age': 38}, }


@account.route('/login', methods=['GET', 'POST'])
def login():
    print(111, request.method)
    if request.method == 'GET':
        return render_template('login.html', msg='', mess_dict=mess_dict)
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'admin' and pwd == 'admin':
            session['user_info'] = user
            return redirect('/index')
        else:
            return render_template('login.html', msg='用户名或者密码错误', mess_dict=mess_dict)


# 默认是将session保存在cookies中
# 可以将session保存到redis,只需要将key保存在客户端中
# 保存redis
# 方式一
# from redis import Redis
# from flask_session import RedisSessionInterface
# app.session_interface = RedisSessionInterface(
#     redis=Redis(host="localhost",port=6379), key_prefix='sssp')
#
# 方式二
# 先pip以下模块：flask-sqlalchemy、flask-login、flask-openid，等你需要的模块
# from flask_session import Session
# from redis import Redis
# app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_REDIS'] = Redis(host="localhost",port=6379)
# Session(app)

@account.route('/show1')
def show1():
    return '123'


@account.route('/x1')
def x1():
    session['k'] = {1: '1234', 2: '78910'}
    return '设置成功'


@account.route('/x2')
def x2():
    v = session.get('k')
    print(v)
    return v


@account.route('/show2')
def show2():
    return jsonify({'a': True, 'b': False})
