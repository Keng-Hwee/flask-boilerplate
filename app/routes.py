from flask import render_template, flash
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Successfully submitted the form!')
        return render_template('form.html', form=form)
    return render_template('form.html', form=form)