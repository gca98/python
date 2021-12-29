from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema

def read_all():
    movies = Movie.query.order_by(Movie.id).limit(100)
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def read_one(director_id,movie_id):
    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )
    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data
    else:
        abort(404, f"Movie not found for Id: {movie_id}")

def create(director_id, movie):
    director = Director.query.filter(Director.id == director_id).one_or_none()
    if director is None:
        abort(404, f"Movie not found for Id: {director_id}")
    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)
    director.movies.append(new_movie)
    db.session.commit()
    data = schema.dump(new_movie)

    return data, 201

def update(director_id, movie_id, movie):
    update_movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    if update_movie is not None:
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)
        update.director_id = update_movie.director_id
        update.id = update_movie.id
        db.session.merge(update)
        db.session.commit()
        data = schema.dump(update_movie)
        return data, 200
    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def delete(director_id, movie_id):

    movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie {movie_id} deleted".format(movie_id=movie_id), 200
        )
    else:
        abort(404, f"Movie not found for Id: {movie_id}")

def top5Movie():
    movies = Movie.query.order_by(Movie.popularity.desc()).limit(5)
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def top5Budget():
    movies = Movie.query.order_by(Movie.budget).limit(5)
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data