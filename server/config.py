"""
flask_sqlalchemy: config.py
"""
SQLALCHEMY_DATABASE_URI = "postgresql://ase4156:dbpass@localhost/eventscalendar"
#Flask-SQLAlchemy will log all the statements issued to stderr
SQLALCHEMY_ECHO = True
#Flask-SQLAlchemy will track modifications of objects and emit signals.
SQLALCHEMY_TRACK_MODIFICATIONS = True
