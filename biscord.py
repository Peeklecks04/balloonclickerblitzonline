from flask import *
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///biscord.db')
@app.route('/')
def index ():
    return render_template('index.html', posts=db['posts'])

@app.route('/create_post', methods=['post'])
def create_post():
    post_dictionary = {
        'message' : request.form['message']
    }
    db['posts'].insert(post_dictionary)

    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
