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

    if request.method == 'POST':
        nameSubject = request.form['name']
        note = request.form['note']

        sub.addSubjects(df,nameSubject,note)

    return render_template('updateData.html')

@app.route('/update', methods=['GET', 'POST'])
def update():

    show = 1

    subjects = df['Nombre'].tolist()

    subjectForm = sub.subjectForm(request.form)

    return render_template('updateData.html', show=show, subjects=subjects, subjectForm=subjectForm)

if __name__ == '__main__':
    app.run()
