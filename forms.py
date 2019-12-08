from flask_wtf import FlaskForm 
from wtforms.validators import DataRequired, Length, Email, EqualTo    
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError


class CadastrarForm(FlaskForm):
    nome = StringField('Nome do usuário',validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    senha = PasswordField('Digite a senha',validators=[DataRequired(), Length(min=6, max=80)])
    repetir = PasswordField('Repita a senha',validators=[DataRequired(), EqualTo('repetir')])
    cadastrar = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=80)])
    logar = SubmitField('Logar')

