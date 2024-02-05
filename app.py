from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_

app = Flask(__name__)

# Defining database connection
uri = ''
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Defining initial table
class cap_hits(db.Model):
    __tablename__ = 'player_cap_hits'

    player_name = db.Column(db.String(255), primary_key = True)
    team_loc = db.Column(db.String(255), primary_key = True)
    cap_hit = db.Column(db.String(255))
    cap_int = db.Column(db.Integer)

# Dummy route to see if database and website are properly linked
@app.route('/show_data')
def show_data():
    data = cap_hits.query.all()
    return render_template('show_data.html', data = data)

# Homepage
@app.route('/')
def hello_world():
    return render_template('index.html', message = 'Within The Cap')

# Processing team choice
@app.route('/process_form', methods = ["POST"])
def process_form():
    team = request.form.get('team_choice')
    return redirect(url_for('show_team_page', team_choice = team))

NFLTeams = {'BUF':'buffalo-bills',     'MIA':'miami-dolphins',    'NE':'new-england-patriots',   'NYJ':'new-york-jets',
            'BAL':'baltimore-ravens',  'CIN':'cincinnati-bengals', 'CLE':'cleveland-browns',     'PIT':'pittsburgh-steelers',
            'HOU':'houston-texans',    'IND':'indianapolis-colts', 'JAX':'jacksonville-jaguars', 'TEN':'tennessee-titans', 
            'DEN':'denver-broncos',    'KC':'kansas-city-chiefs',  'LV':'las-vegas-raiders',     'LAC':'los-angeles-chargers',
            'DAL':'dallas-cowboys',    'NYG':'new-york-giants',    'PHI':'philadelphia-eagles',  'WSH':'washington-commanders',
            'CHI':'chicago-bears',     'DET':'detroit-lions',      'GB':'green-bay-packers',     'MIN':'minnesota-vikings',
            'ATL':'atlanta-falcons',   'CAR':'carolina-panthers',  'NO':'new-orleans-saints',    'TB':'tampa-bay-buccaneers',
            'ARI':'arizona-cardinals', 'LAR':'los-angeles-rams',  'SF':'san-francisco-49ers',    'SEA':'seattle-seahawks'
            }

# Querying database and displaying team page
@app.route('/team/<team_choice>')
def show_team_page(team_choice):
    players = cap_hits.query.filter_by(team_loc = team_choice).order_by(cap_hits.cap_int.desc()).all()
    team_name = NFLTeams[team_choice].replace("-", " ").title()
    return render_template('team.html', team = team_name, data = players)

if __name__ == '__main__':
    app.run(debug = True)
