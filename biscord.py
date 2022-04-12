from flask import *
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///biscord.db')
@app.route('/chatroom')
def chatroom ():
    return render_template('caht.html', posts=db['posts'])

@app.route('/create_post', methods=['post'])
def create_post():
    post_dictionary = {
        'message' : request.form['message']
    }
    db['posts'].insert(post_dictionary)

    return redirect('/chatroom')

@app.route('/leaderboard')
def leaderboard ():
    return render_template('leaderboard.html', posts=db['leaderboard'])

@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/create_score', methods=['post'])
def create_score():
    score_dictionary = {
        'sendscore' : request.form['sendscore']
    }
    db['leaderboard'].insert(score_dictionary)


@app.route('/')
def home ():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

