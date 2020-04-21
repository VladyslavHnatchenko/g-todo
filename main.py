import datetime
import os

from flask import Flask, render_template, redirect, url_for, request
from google.cloud import datastore

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
client = datastore.Client()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or \
                           "b'\xe3\xa3\xb0\xd6Q<\x144\xa2\xd5\xd0IN \xf4\\\x16\x1b\x1e\xf0\xe8\x92:\xd3'"


class MainForm(FlaskForm):
    text = StringField('text', validators=[DataRequired()])


@app.route('/')
def main():
    form = MainForm()
    query = client.query(kind='task')
    query.add_filter('done', '=', "In Progress")
    query.order = ['done']
    incomplete = query.fetch()

    query1 = client.query(kind='task')
    query1.add_filter('done', '=', "Done")
    query1.order = ['done']
    complete = query1.fetch()
    return render_template('index.html', incomplete=incomplete, complete=complete, form=form)


@app.route("/add", methods=["POST"])
def add():
    form = MainForm()

    if form.validate_on_submit():
        task = datastore.Entity(key=client.key('task'))
        task.update({
            "created": datetime.datetime.utcnow(),
            "text": request.form["text"],
            "done": "In Progress"
        })
        client.put(task)
        return redirect(url_for("main"))
    return render_template('index.html', form=form)


@app.route("/complete/<int:id>")
def complete(id):
    form = MainForm()
    with client.transaction():
        key = client.key('task', id)
        task = client.get(key)

        if not task:
            raise ValueError(
                f'Task {id} does not exist.')

        task['done'] = "Done"
        client.put(task)

        return redirect(url_for("main"))
    return render_template('index.html', form=form)


@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    key = client.key('task', id)
    client.delete(key)
    return redirect(url_for("main"))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
