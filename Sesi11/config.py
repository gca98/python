import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + os.path.join(basedir, 'people.db')\
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jxvtxouzqpkyja:793d27257f563f8a0f95fd5da88ca38ebfcdddfee2ce749754ccf41feb95ce76@ec2-3-221-109-30.compute-1.amazonaws.com:5432/d31p51umh6fpgs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)