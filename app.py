import mainList
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    
    myvariable = request.form.get("teamDropdown")

    if myvariable == 'randon':
        companycode = 1
        print('passou randon')
    elif myvariable == 'soprano':
        companycode = 2
    elif myvariable == 'totvs':
        companycode = 3
    elif myvariable == 'promob':
        companycode = 4
    else:
        companycode = 0
    
    if companycode >0:
        print('entrou')
        print(companycode)
        mlista = mainList.consultaVagas(companycode) # EMPRESA QUE VAI SER LISTADA 
        your_list_as_json = json.dumps(mlista,indent=1, sort_keys=True, ensure_ascii=False) 

        y = json.loads(your_list_as_json)
        empresa = ['randon', 'soprano', 'totvs', 'promob']
        
        return render_template('index.html', tasks=y,empresa=empresa, myvariable=myvariable)
    else:
        empresa = ['randon', 'soprano', 'totvs', 'promob']
        return render_template('index.html', empresa=empresa, myvariable=myvariable)
    #else:
    #    tasks = Todo.query.order_by(Todo.date_created).all()
    #    print('refresh')
    #    return render_template('index.html', tasks=tasks)


#@app.route("/submitted", methods=['POST'])
#def hello():
#   myvariable = request.form.get("teamDropdown")
#   print('passou aquiiiiiiiiiii')
#   return myvariable


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
