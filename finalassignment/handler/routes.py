from flask import request,render_template
import json

def configure_routes(connex_app):
    @connex_app.route("/")
    def home():
        return render_template("home.html")


    # Create a URL route in our application for "/people"
    @connex_app.route("/director")
    @connex_app.route("/director/<int:id>")
    def people(id=""):
        return render_template("directors.html", id=id)


    @connex_app.route("/director/<int:director_id>")
    @connex_app.route("/director/<int:director_id>/movies")
    @connex_app.route("/director/<int:director_id>/movies/<int:movie_id>")
    def movie(director_id, movie_id=""):
        return render_template("movie.html", director_id=director_id, movie_id=movie_id)