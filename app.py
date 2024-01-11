from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

uri = ''
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class cap_hit(db.Model):
    __tablename__ = 'player_cap_hits'

    player_name = db.Column(db.String(255), primary_key = True)
    team_loc = db.Column(db.String(255), primary_key = True)
    cap_hit = db.Column(db.String(255))

@app.route('/show_data')
def show_data():
    data = cap_hit.query.all()
    return render_template('show_data.html', data = data)

@app.route('/')
def hello_world():
    return render_template('index.html', message = 'Within The Cap')

@app.route('/process_form', methods = ["POST"])
def process_form():
    team = request.form.get('team_choice')
    return redirect(url_for('show_team_page', team_choice = team))

@app.route('/team/<team_choice>')
def show_team_page(team_choice):
    return render_template('team.html', team = team_choice)

if __name__ == '__main__':
    app.run(debug = True)
