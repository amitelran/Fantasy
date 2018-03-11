# =============================================================================
#                               IMPORTS
# =============================================================================


from flask import Flask, render_template, session, request, redirect, url_for, flash
from database import init_db
import user

# =============================================================================
#                               CONFIGURATION
# =============================================================================

#db = SQLAlchemy()

# Initialize an "app" variable, using the __name__ attribute

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:remi1985@localhost/fantasy_db'
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:remi1985@localhost:5432/fantasy_db'

# Initialize Database connection

#db = SQLAlchemy(app)

init_db()


# =============================================================================
# =============================================================================
#                               ROUTING
# =============================================================================
# =============================================================================



# The @app.route is a Python decorator.
# It takes the function directly below it and modifies it.
# In this case, we use this to route traffic from a specific URL to the function directly below.
# Using different @app.route calls, we can 'trigger' different parts of the code when the user visits
# different parts of our application.


# =============================================================================
#                       INDEX - login\registration page
# =============================================================================


@app.route('/')
@app.route('/<user>')
def index():
    if 'username' in session:
        return render_template('home.html', user=session['username'])
    return render_template('home.html', user=None)


# =============================================================================
#                                   LOGIN
# =============================================================================


@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verification = user.User(username, password).verify_user()

        if verification:
            session['username'] = username
            flash('You were successfully logged in')
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password. Please try again!'
            return render_template('home.html', message=error)


# =============================================================================
#                                   LOGOUT
# =============================================================================


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)                                   # pop\remove the username from session
    return render_template('home.html', message="Logged Out!")



# =============================================================================
#                            REGISTER NEW USER
# =============================================================================



@app.route('/register', methods=['POST'])
def register():
    password_repeat = request.form['password_register_repeat']
    message = user.User(request.form['username_register'], request.form['password_register']).register_user(password_repeat)
    return render_template('home.html', message=message)


# =============================================================================
#                            MY TEAM ROUTE
# =============================================================================


@app.route('/myTeam', methods=['GET', 'POST'])
def my_team():
    return render_template('myTeam.html')


# =============================================================================
#                            MY LEAGUES ROUTE
# =============================================================================


@app.route('/myLeagues', methods=['GET', 'POST'])
def my_leagues():
    return render_template('myLeagues.html')


# =============================================================================
#                                   STATS
# =============================================================================


@app.route('/stats', methods=['GET', 'POST'])
def stats():
    return render_template('stats.html')


# =============================================================================
#                                   TOURNAMENT
# =============================================================================


@app.route('/tournament', methods=['GET', 'POST'])
def tournament():
    return render_template('tournament.html')


# =============================================================================
#                                   RULES
# =============================================================================


@app.route('/rules', methods=['GET', 'POST'])
def rules():
    return render_template('rules.html')


# =============================================================================
#                            DEBUG RENDER
# =============================================================================


def debug_render(details=None):
    return render_template('debugRender.html', details=details)


# This is normal Python boilerplate to make sure we don't run anything automatically if our code is
# imported by another Python script.
# Calls the run() method of the app we initialized. This starts the development server for Flask and allows us to
# visit our web application from our local machine by visiting localhost.

if __name__ == "__main__":
    app.run(debug=True)


