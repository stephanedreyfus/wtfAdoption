from flask_sqlalchmey import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    ''' Table for pet information '''

    __tablename__ = "pets"

    id = db.Column(db.Interger,
                   primarykey=True,
                   autoincrement=True)

    name = db.Column(db.Text,
                     nullable=False)

    species = db.Column(db.Text,
                        nullable=False,
                        default='Unknown')

    photo_url = db.Column(db.Text)

    age = db.Column(db.Interger,
                    nullable=False)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
