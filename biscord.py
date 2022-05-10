from flask import *
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///biscord.db')
app.secret_key = "Regigigas (Japanese: レジギガス Regigigas) is a Normal-type Legendary Pokémon introduced in Generation IV. Regigigas is a large, white, golem-like Pokémon with seven black circular eyes arranged in a specific pattern. The pattern is Regigigas's way of showing its anger; its eyes glow red when it is provoked. It has six spots that are apart from its eyes, which appear to be gemstones. These gemstones seem to represent the original three Legendary titans, with red gems representing Regirock, blue gems indicating Regice, and silver gems representing Registeel. Regigigas has long arms, with three fairly human-like white fingers, and short legs that end in large mossy bushes instead of feet. Regigigas has large yellow bands on its shoulders and wrists, with a sloping section on its chest that appears to be its head and is also yellow. Its body is covered in black stripes, and it has moss growing in its back and feet. Regigigas is a skilled craftsman. It created golems out of inanimate objects and elemental energies, bringing them to life. Regigigas is also capable of controlling these Legendary titans, even if they already belong to a different Trainer. It can also survive extreme conditions as it is able to work with the boiling temperatures of magma (1300-2400 °F [700-1300 °C]) as well as frigid ice (-328 °F [-200 °C]). When Regigigas is disturbed from its slumber, it goes on a rampage and shoots powerful beams of energy. When it is befriended, however, it is calm and gentle, as seen in Pillars of Friendship!. It is able to crush targets by using its signature move, Crush Grip. According to Sinnoh legend, Regigigas's strength enables it to move continents."


@app.route('/chatroom')
def chatroom ():
    return render_template('caht.html', posts=db['posts'])


@app.route('/leaderboard')
def leaderboard ():
    return render_template('leaderboard.html', scores=db['leaderboard'])

@app.route('/login')
def login ():
    return render_template('login.html')

@app.route('/login_post', methods=['post'])
def login_post ():
    session['username']= (request.form['username'])
    return redirect('/')

@app.route('/logout')
def logout():
    if 'username' in session:
      del session ['username']
    return render_template('login.html')

@app.route('/theme')
def theme ():
    session['theme']
    return 



@app.route('/create_score', methods=['post'])
def create_score():
    score_dictionary = {
        'sendscore' : request.form['sendscore'],
        'username' : session['username'],
        'picture' : session['profilepic']
    }
    db['leaderboard'].insert(score_dictionary)
    return redirect ('/leaderboard')


@app.route('/')
def home ():
    return render_template('home.html')

@app.route('/myaccount')
def myaccount ():
    return render_template('myaccount.html')

@app.route('/game')
def game ():
    return render_template('game.html')

@app.route('/create_post', methods=['post'])
def create_post():
    post_dictionary = {
        'message' : request.form['message'],
        'username' : session['username'],
        'picture' : session['profilepic']
    }
    db['posts'].insert(post_dictionary)

    return redirect('/chatroom')

@app.route('/setpfp', methods=['post'])
def setpfp():
    file = request.files['file']
    filename_to_save = 'static/uploads/' + file.filename

    file.save(filename_to_save)

    session['profilepic'] = filename_to_save

    return render_template('myaccount.html')


if __name__ == '__main__':
    app.run(debug=True)

