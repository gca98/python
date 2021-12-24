from flask import Flask,request,render_template
from markupsafe import escape



app = Flask(__name__)

@app.route('/')
def index():    
    return 'Index Page'

@app.route("/<name>")
def hello1(name):    
    return f"Hello, {escape(name)}!"
@app.route('/home')
def hello():    
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):    
    # show the user profile for that user    
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    # show the post with the given id, the id is an integer    
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):    
    # show the subpath after /path/    
    return f'Subpath {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':        
        return do_the_login()    
    else:        
        return show_the_login_form()
def do_the_login():
    return f'Do login :: used htpp request is {request.method}'
def show_the_login_form():
    return f'Do show :: used htpp request is {request.method}'
# url_for('static', filename='style.css')

@app.route('/hello/')
@app.route('/hello/<name>')
def helloo(name=None):    
    age = 10
    petname = ['d', 'a']
    pets = {'cat', 'anjing'}
    return render_template('hello.html', tamplatename=name, age=age, petname=petname, pets=pets)

if __name__ == '__main__':    
    app.run(debug=True)


