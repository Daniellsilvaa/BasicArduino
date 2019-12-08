
from flask import Flask, render_template, redirect, url_for, request, session
from forms import LoginForm, CadastrarForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, UserMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubd.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SECRET_KEY'] = '8d39132b1bfec3225ad1aa46df64deee'

db = SQLAlchemy(app)
login_manager = LoginManager(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) 
    nome = db.Column(db.String(25), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    senha = db.Column(db.String(80), nullable = False)

    def __repr__(self):
        return '<User %r>' % self.nome



@app.route('/logout')
def logout():
    session.clear()
    logout_user()   
    return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
   
    form = CadastrarForm()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        repetir = form.repetir.data
        usuario = User.query.filter_by(email=email).first()
        if usuario:
            return redirect(url_for('cadastro'))

        novo = User(email = email, nome = nome, senha=senha)
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('cadastro.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
        
    if form.validate_on_submit():
        usuario = User.query.filter_by(email=form.email.data).first()
        if usuario and usuario.senha == form.senha.data:
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', form=form) 

@app.route('/nivel_1')
def niv1():
    return render_template('niveis/nivel_1.html')

@app.route('/nivel_2')
def niv2():
    return render_template('niveis/nivel_2.html')

@app.route('/nivel_3')
def niv3():
    return render_template('niveis/nivel_3.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')




if(__name__ == '__main__'):
    app.run(debug=True)
    
