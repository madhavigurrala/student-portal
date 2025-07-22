# app.py
from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_portal.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)

class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')
def index():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form['password'])
        user = User(username=request.form['username'], password=hashed_pw, role=request.form['role'])
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    user = User.query.get(session['user_id'])
    if user.role == 'admin':
        students = User.query.filter_by(role='student').all()
        return render_template('admin_dashboard.html', students=students)
    marks = Mark.query.filter_by(user_id=user.id).all()
    avg = sum(mark.score for mark in marks)/len(marks) if marks else 0
    return render_template('dashboard.html', user=user, marks=marks, average=round(avg, 2))

@app.route('/add-marks/<int:id>', methods=['GET', 'POST'])
def add_marks(id):
    student = User.query.get(id)
    if request.method == 'POST':
        new_mark = Mark(subject=request.form['subject'], score=int(request.form['score']), user_id=id)
        db.session.add(new_mark)
        db.session.commit()
        return redirect('/dashboard')
    return render_template('add_marks.html', student=student)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
# other routes above...

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

