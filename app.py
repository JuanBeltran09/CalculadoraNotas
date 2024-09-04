from flask import Flask, render_template
import Subject as sub

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/add')
def add():
    return render_template('updateData.html')

@app.route('/update')
def update():
    show = 1
    return render_template('updateData.html', show=show)

if __name__ == '__main__':
    app.run()
