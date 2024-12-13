from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def db_init(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "description": self.description
        }
