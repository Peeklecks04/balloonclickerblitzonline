from flask import *
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///biscord.db')
@app.route('/chatroom')
def index ():
    return render_template('caht.html', posts=db['posts'])

@app.route('/create_post', methods=['post'])
def create_post():
    post_dictionary = {
        'message' : request.form['message']
    }
    db['posts'].insert(post_dictionary)

    return redirect('/chatroom')

@app.route('/leaderboard')
def index ():
    return render_template('leaderboard.html')


if __name__ == '__main__':
    app.run(debug=True)

