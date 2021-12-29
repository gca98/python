from flask import make_response, abort
from marshmallow import schema
from sqlalchemy.orm import session
from config import db
from models import Director, DirectorSchema, Movie


def read_all():
    directors = Director.query.order_by(Director.id).limit(100)
    directors_schema = DirectorSchema(many=True)
    data  = directors_schema.dump(directors)
    return data

def create(directors):
    name = directors.get("name")
    gender = directors.get("gender")
    uid = directors.get("uid")
    id = directors.get("id")
    department = directors.get("department")
    
    existing_id = (
        Director.query.filter(Director.id==id).filter(Director.id == id).one_or_none()
    )

    if existing_id is None:
        schema = DirectorSchema()
        new_director = schema.load(directors, session=db.session)

        db.session.add(new_director)
        db.session.commit()

        data =schema.dump(new_director)
        return data, 201
    else:
        abort(409, f"Director id {id} exists already")


def read_one(id):
    director = (
        Director.query.filter(Director.id== id).outerjoin(Movie).one_or_none()
    )

    if director is not None:
        director_schema = DirectorSchema()
        data = director_schema.dump(director)
        return data
    else:
        abort(404, f"director not found for Id: {id}")

def update(id,director):
    update_director = Director.query.filter(
        Director.id == id
    ).one_or_none()
    if update_director is not None:
        schema = DirectorSchema()
        update = schema.load(director, session=db.session)
        update.id = update_director.id

        db.session.merge(update)
        db.session.commit()
        data = schema.dump(update_director)
        return data,200
    else:
        abort(404, f"director not found for Id: {id}")

def delete(id):


    director = Director.query.filter(Director.id == id).one_or_none()


    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {id} deleted", 200)

    else:
        abort(404, f"Director not found for Id: {id}")