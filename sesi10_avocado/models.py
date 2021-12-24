from datetime import datetime
from config import db, ma

# avocado/region/<region_id>
class avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.Date)
    avgprice = db.Column(db.Real)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Real)
    avo_c= db.Column(db.Real)
    type = db.Column(db.ForeigKey('avotype.typeid'))
    regionid = db.Column(db.ForeigKey('avoregion.regionid'))
    

class avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key = True)
    region = db.Column(db.String(32))
    avocados = db.relationship(
        'Avocado',
        backref='avoregion',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(avocado.avgprice)'
    )

class avotype (db.model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(32))
    avocados = db.relationship(
        'Avocado',
        backref='avotype',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(avocado.avgprice)'
    )


# class PersonSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Person
#         # sqla_session = db.session
#         load_instance = True