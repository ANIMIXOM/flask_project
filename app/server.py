from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from forms.user import RegisterForm, LoginForm
from data.users import User
from data import db_session

app = Flask(__name__, static_url_path='/static')
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/diploms/<play_id>', methods=["GET", 'POST'])
def diplom(play_id):
    print("проверка")
    if request.method == 'POST':
        print("проверка 2")
        return render_template(f"base.html")
    return render_template(f"gr_{play_id}.html")


@app.route("/diploms", methods=["GET", "POST"])
def diplom_sett():
    if request.method == "POST":
        if 'email_button' in request.form:
            return render_template("email_push.html")
        if 'push_email' in request.form:
            return f"{request.form['firstName']}, {request.form['lastName']}"


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/play/<int:fabric_id>")
@login_required
def play(fabric_id):
    return render_template(f"game_{fabric_id}.html")
    # для других фабрик нужно добавить пути


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    # Достаем из БД, параметр passed из отдельной таблицы, соединяющей user and fabric
    fabrics = [
        {"id": 1, "title": "ЛТЗ", "image": "ltz.jpg", "passed": True},
        {"id": 2, "title": "СЧЗ", "image": "schz.jpg", "passed": False},
        {"id": 3, "title": "Людиново-кабель", "image": "ludinovo_cabel.jpg", "passed": False},
    ]
    return render_template('main.html', title='Заводы Людиново', fabrics=fabrics)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data
        )
        db_sess.add(user)
        db_sess.commit()
        f = True
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user:
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_score', methods=['POST'])
def add_score():
    # здесь нужно отправить запрос к БД, в котором для фабрики, которую прошел пользователь, будет проставлено passed
    print(current_user)
    return 'OK'


def main():
    db_session.global_init("db/blogs.db")
    app.run(debug=True)


if __name__ == '__main__':
    main()
