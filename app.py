from flask import Flask, render_template,request
import Subject as sub

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')

df = sub.readSubjects()

@app.route('/add', methods=['GET', 'POST'])
def add():

    show = 0;

    if request.method == 'POST':
        nameSubject = request.form['name']
        note = request.form['note']
        sub.addSubjects(df,nameSubject,note)

        return render_template('menu.html')

    return render_template('updateData.html',show=show)

@app.route('/update', methods=['GET', 'POST'])
def update():

    df = sub.readSubjects()

    show = 1

    subjects = df['Nombre'].tolist()

    if request.method == 'POST':
        nameSubject = request.form.get('name')
        note = request.form['note']
        print(note)
        sub.updateSubjects(df,nameSubject,note)
        return render_template('menu.html')

    return render_template('updateData.html', show=show, subjects=subjects)

if __name__ == '__main__':
    app.run()
