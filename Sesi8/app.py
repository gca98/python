from flask import render_template,Flask
import connexion


app = Flask(__name__, template_folder="templates")

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')
app = app.app


@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')




if __name__ == '__main__':
    app.run( debug=True)

